import numpy as np


# get metadata from the datasets (e.g. how many unique nodes/persons are there in the dataset)
def getDatasetsMetadata(datasets):
    # the dictionary that will store key-value pairs accordingly to the metadata
    sizes = dict()
    for i in datasets.keys():
        # take each individual id and count the number of unique ids
        p1 = list(np.unique(datasets[i]['p1'].to_numpy()))
        p2 = list(np.unique(datasets[i]['p2'].to_numpy()))

        # take both columns and link them together
        p1.extend(p2)

        # put into the size metadata the actual size value
        sizes[i] = np.unique(p1).size

    # return the metadata as "json" - e.g. at the moment this example is an object into an object
    # further metadata can be added without changing the client implementation
    return {'sizes': sizes}
