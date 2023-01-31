from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel, Field
from typing import Optional
import pandas as pd
import json
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
import re
import numpy as np
from fastapi_redis_cache import FastApiRedisCache
from fastapi_redis_cache import cache_one_year
from fastapi.openapi.utils import get_openapi
from metadata_utilities import getDatasetsMetadata
from data_cache import returnCachedInstances, getDataCachedInstance
import pickle
import os

tags_metadata = [
    {
        "name": "sim",
        "description": "Request this api for simulation data.",
    },
    {
        "name": "dataset",
        "description": "Request for spesific datasets.",
    },
    {
        "name": "dataset_list",
        "description": "get datasets list."
    },
    {
        "name": "strategies_list",
        "description": "get strategies list."
    }
]

# create app with fast api
app = FastAPI(openapi_tags=tags_metadata)

LOCAL_REDIS_URL = "redis://127.0.0.1:6379"


# init the cache
@app.on_event("startup")
def startup():
    redis_cache = FastApiRedisCache()
    redis_cache.init(
        host_url=os.environ.get("REDIS_URL", LOCAL_REDIS_URL),
    )


origins = [
    "http://localhost:8080",
    "http://localhost:8000"
]
app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])
app.add_middleware(GZipMiddleware, minimum_size=0)

# preload the dataset to spead up the training process
work1 = pd.read_csv('Complex_network/datasets/work1.csv')
work2 = pd.read_csv('Complex_network/datasets/work2.csv')
hs11 = pd.read_csv('Complex_network/datasets/hs11.csv')
hs12 = pd.read_csv('Complex_network/datasets/hs12.csv')
mit1 = pd.read_csv('Complex_network/datasets/mit1.csv')
mit2 = pd.read_csv('Complex_network/datasets/mit2.csv')

# load 'node names'
names = open('names/names.txt')
names = names.readlines()
namesRes = []
for i in names:
    namesRes.append(re.sub('[^a-zA-Z]+', '', i).capitalize())
names = namesRes

# setup the datasets
datasets = {'High School 1': hs11, 'High School 2': hs12, 'Workplace 1': work1, 'Workplace 2': work2,
            'University 1': mit1, 'University 2': mit2}

datasets_verify = ['High School 1', 'High School 2', 'Workplace 1', 'Workplace 2', 'University 1', 'University 2']

# 13 mitigation strategies
modes = ['degree product', 'r degree product', 'strength product', 'r strength product',
         'betweeness', 'r betweeness', 'random', 'link weight', 'r link weight',
         'weighted eigen', 'r weighted eigen', 'unweighted eigen', 'r unweighted eigen']

# preload the datasets metadata
dataset_metadata = getDatasetsMetadata(datasets)

# prepare the cache
cached_data = None
print('Data Cache Initialized')
store_path = './cachedDatasets/'
if not os.path.isdir(store_path):
    os.mkdir(store_path)

# See if the data is already cached, if it is load the data on the disk
# if not compute it and store it
if len(os.listdir(store_path)) == 0:
    print('Cache will be saved on disk \n')
    cached_data = returnCachedInstances(datasets, modes)
    with open(store_path + 'cachedData.pickle', 'wb') as handle:
        pickle.dump(cached_data, handle, protocol=pickle.HIGHEST_PROTOCOL)
else:
    with open(store_path + 'cachedData.pickle', 'rb') as handle:
        print('Cache loaded from disk \n')
        cached_data = pickle.load(handle)

# get the proper indexed datasets
# put into the cached_data only the preprocessed simulations
datasets = cached_data[1]
cached_data = cached_data[0]


# setup open api custom style
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    # context of project
    openapi_schema = get_openapi(
        title="Covid-19 Spreading Simulation",
        version="1.0.0",
        description="""Covid-19 was found in Wuhan last year. It has caused a global pandemic for more than one year.
                       Transmission of this virus occurred mostly in close contact with another person. Researchers from
                       TU Delft developed a model that analyzes the spreading of Covid-19 with temporal networks.
                       To help researchers and society better understand this model, we decide to visualize it.
                       With the animation, we can help the society understand the importance of quarantine in the real life.
        """,
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


# create request model
class CovidModel(BaseModel):
    dataset: Optional[str] = Field("hs11", title="The dataset you want to run on.")
    block_prob: Optional[float] = Field(0.3, title="The blocking probability you want to set the simulator.")
    recovery: Optional[float] = Field(0.1, title="The recovery probability you want to set the simulator.")
    start_node: Optional[int] = Field(0, title="the start node you want to set.")
    infect_rate: Optional[float] = Field(0.2, title="the infect rate you want to set.")
    mode: Optional[str] = Field("degree product", title="The mode you want set the simulator.")


# verify that the api is working
@app.get("/")
async def root():
    return {"message": "The simulator is working. Please visit /doc for swagger page."}


# sim model from the algorithm
@app.post("/sim", tags=["sim"])
@cache_one_year()  # cache for one year
async def sim(model: CovidModel, response: Response):
    print(
        'Init simulation with: \n' + 'dataset: {0} block_prob: {1}  recovery: {2}  start_node: {3} infect_rate: {4} mode: {5}'.format(
            model.dataset, model.block_prob,
            model.recovery, model.start_node,
            model.infect_rate, model.mode))

    global names
    global dataset_metadata
    global cached_data
    # verify the parameters are correct to prevent server crash
    if model.mode not in modes:
        response.status_code = 400
        return jsonable_encoder(HTTPException(status_code=400, detail="mode is not supported"))

    if model.dataset not in datasets_verify:
        response.status_code = 400
        return jsonable_encoder(HTTPException(status_code=400, detail="dataset is not supported"))

    if model.block_prob > 1.0 or model.block_prob < 0:
        response.status_code = 400
        return jsonable_encoder(HTTPException(status_code=400, detail="block_prob out of range"))

    if model.infect_rate > 1.0 or model.infect_rate <= 0:
        response.status_code = 400
        return jsonable_encoder(HTTPException(status_code=400, detail="infect_rate out of range"))

    if model.recovery > 1.0 or model.recovery <= 0:
        response.status_code = 400
        return jsonable_encoder(HTTPException(status_code=400, detail="recovery out of range"))

    if model.start_node < 0 or model.start_node > dataset_metadata['sizes'][model.dataset] \
            or not float(model.start_node).is_integer():
        response.status_code = 400
        return jsonable_encoder(HTTPException(status_code=400, detail="start node out of range"))

    # generate the model
    s_model = getDataCachedInstance(cached_data, model.dataset, model.block_prob, model.recovery)
    # take the infect and rec model and compress with gzip
    nodes_count, seed, infect, rec = s_model.spread(
        beta=model.infect_rate, start_node=model.start_node)
    # rec shape {"rec": [28561, 126]} res shape
    if model.start_node < 0 or model.start_node >= nodes_count:
        return jsonable_encoder(HTTPException(status_code=400, detail="start node out of range"))

    nameChoice = list(np.random.choice(names, nodes_count + 1))

    nameSet = set()
    if len(nameChoice) >= 5:
        while len(nameSet) <= 5:
            nameSet.add(np.random.randint(0, len(nameChoice)))

    nameSet = list(nameSet)
    nameChoice[nameSet[0]] = names[0]
    nameChoice[nameSet[1]] = names[1]
    nameChoice[nameSet[2]] = names[2]
    nameChoice[nameSet[3]] = names[3]
    nameChoice[nameSet[4]] = names[4]

    return_result = {"seed": seed,
                     "infect": list(infect),
                     "rec": list(rec), "names": list(nameChoice),
                     "contact": list(datasets[model.dataset].values.tolist()),
                     "nodes_count": nodes_count
                     }

    return_result = json.dumps(return_result).encode('utf-8')
    # headers = {"Content-Encoding": "gzip"}
    return jsonable_encoder(return_result)


# data for a specific dataset
@app.get("/dataset/{dataset}", tags=["dataset"])
def getDatasetData(dataset: str, response: Response):
    # verify the parameter is correct to prevent server crash
    global datasets
    if dataset not in datasets_verify:
        response.status_code = 400
        return jsonable_encoder((HTTPException(status_code=400, detail="dataset is not supported")))
    return jsonable_encoder(datasets[dataset].values.tolist())


# names for all datasets
@app.get("/datasets", tags=["dataset_list"])
async def getDatasets():
    global datasets
    return jsonable_encoder(list(datasets.keys()))


# names for all strategies available
@app.get("/strategies", tags=["strategies_list"])
async def getStrategies():
    global modes
    return jsonable_encoder(list(modes))


# get the metadata about the datasets
@app.get("/datasetMetadata", tags=["dataset_metadata"])
async def datasetsMetadata():
    global dataset_metadata
    return jsonable_encoder(dataset_metadata)


app.openapi = custom_openapi
