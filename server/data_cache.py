from Covid_Sim import Covid_Sim
import copy

debug = True


# return a cached version of the datasets available on the backend
def returnCachedInstances(datasets, modes):
    global debug
    cached_results = dict()
    computedDatasets = dict()
    # Create a new instance for every dataset
    for i in datasets.keys():
        if debug:
            print('File: {0} started to cache.\n'.format(i))
        # index the dataset starting from index 0
        data = index_data(datasets[i])
        computedDatasets[i] = data
        # put the cached result into the dictionary
        cached_results[i] = Covid_Sim(data, modes)
        if debug:
            print('File: {0} cached\n'.format(i))
    # return the cached instances
    return [cached_results, computedDatasets]


# return a cache instance based on the dataset
def getDataCachedInstance(cache, dataset, block_prob=0.1, rec=0.1):
    # deepcopy the instance
    instance = copy.deepcopy(cache[dataset])
    # add the proper data into the copy
    instance.block_prob_val = block_prob
    instance.rec = rec
    # return the copied instance with proper data
    return instance


# index the persons starting from index 0
def index_data(dataset):
    # every person will start indexing at 0
    index = 0
    # the indexValidator will check if a node has already been assigned to an index
    indexValidator = dict()
    # take every row in the dataframe
    for i in range(0, dataset.shape[0]):
        # if the persons one or two were not assigned an index assign it
        if dataset['p1'][i] not in indexValidator:
            indexValidator[dataset['p1'][i]] = index
            index += 1

        if dataset['p2'][i] not in indexValidator:
            indexValidator[dataset['p2'][i]] = index
            index += 1

        # take the assigned index and store it into the dataframe
        dataset['p1'][i] = indexValidator[dataset['p1'][i]]
        dataset['p2'][i] = indexValidator[dataset['p2'][i]]

    # return the proper indexed dataset
    return dataset
