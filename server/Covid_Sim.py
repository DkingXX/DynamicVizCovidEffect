import numpy as np
import pandas as pd
import networkx as nx
from tqdm import tqdm
import time

debug = False


def infect_time(infect, dataset):
    interval = np.linspace(min(dataset['time']), max(dataset['time']), num=10000)
    infect_frac = np.zeros(10000)
    for i in range(10000):
        infect_frac[i] = np.mean(infect[np.argmin(np.array(dataset['time']) < interval[i])])
    return infect_frac


# datasets = {'hs11':hs11,'hs12':hs12,'work1':work1,'work2':work2,'mit1':mit1,'mit2':mit2}
def iterate(dataset, i=0):
    dataset['time'] -= min(dataset['time'])
    dataset_ = dataset.copy()
    T = max(dataset['time'])
    for _ in range(i):
        dataset_['time'] += T
        dataset = pd.concat([dataset, dataset_])
    return dataset


class Covid_Sim():
    global debug

    def __init__(self, contacts, modes, block_prob_val=0.1, rec=0.1, time_w=None):
        self.contacts = contacts
        self.modes = modes
        print('time before unique {0}'.format(time.perf_counter()))
        self.people = np.unique(self.contacts[['p1', 'p2']])
        self.n = len(self.people)
        self.cure = rec / (3600 * 24)
        print('time before min {0}'.format(time.perf_counter()))
        self.startT = min(self.contacts['time'])
        self.endT = max(self.contacts['time'])
        self.T5 = self.startT + 0.5 * (self.endT - self.startT)
        self.block_prob = {}
        p2id = {}

        if debug:
            print('time before enumerate {0}'.format(time.perf_counter()))

        for i, p in enumerate(self.people):
            p2id[p] = i
        self.contacts['id1'] = self.contacts['p1'].apply(lambda row: p2id[row])
        self.contacts['id2'] = self.contacts['p2'].apply(lambda row: p2id[row])

        if debug:
            print('time before backbones {0}'.format(time.perf_counter()))

        # aggregate the contacts
        self.backbones = np.zeros([self.n, self.n])
        for i, c in self.contacts.iterrows():
            t, p1, p2 = c[['time', 'id1', 'id2']]
            self.backbones[p1, p2] += 1
            self.backbones[p2, p1] += 1

        self.agg_graph = nx.from_numpy_array(self.backbones)

        if debug:
            print('time before for modes {0}'.format(time.perf_counter()))

        for mode in self.modes:
            feature = 0
            if mode == 'degree product':
                adj = (self.backbones > 0)
                degree = np.sum(adj, axis=0)
                feature = np.outer(degree, degree)
            elif mode == 'r degree product':
                adj = (self.backbones > 0)
                degree = np.sum(adj, axis=0)
                feature = 1 / np.outer(degree, degree)
            elif mode == 'strength product':
                strength = np.sum(self.backbones, axis=0)
                feature = np.outer(strength, strength)
            elif mode == 'r strength product':
                strength = np.sum(self.backbones, axis=0)
                feature = 1 / np.outer(strength, strength)
            elif mode == 'betweeness':
                feature = np.zeros([self.n, self.n])
                bet = nx.algorithms.edge_betweenness_centrality(self.agg_graph)
                for k, v in bet.items():
                    feature[k] = v
                feature += feature.T
            elif mode == 'r betweeness':
                feature = np.zeros([self.n, self.n])
                bet = nx.algorithms.edge_betweenness_centrality(self.agg_graph)
                for k, v in bet.items():
                    if v > 0:
                        feature[k] = 1 / v
                feature += feature.T
            elif mode == 'link weight':
                feature = np.copy(self.backbones)
            elif mode == 'r link weight':
                feature = np.zeros([self.n, self.n])
                feature[self.backbones != 0] = 1 / self.backbones[self.backbones != 0]
            elif mode == 'weighted eigen':
                eigen = nx.eigenvector_centrality_numpy(self.agg_graph, weight='weight')
                feature = np.zeros([self.n, self.n])
                for i in range(self.n):
                    for j in range(self.n):
                        feature[i, j] = (eigen[i]) * (eigen[j])
            elif mode == 'r weighted eigen':
                eigen = nx.eigenvector_centrality_numpy(self.agg_graph, weight='weight')
                feature = np.zeros([self.n, self.n])
                for i in range(self.n):
                    for j in range(self.n):
                        feature[i, j] = 1 / (eigen[i] * eigen[j])
            elif mode == 'unweighted eigen':
                eigen = nx.eigenvector_centrality_numpy(self.agg_graph)
                feature = np.zeros([self.n, self.n])
                for i in range(self.n):
                    for j in range(self.n):
                        feature[i, j] = eigen[i] * eigen[j]
            elif mode == 'r unweighted eigen':
                eigen = nx.eigenvector_centrality_numpy(self.agg_graph)
                feature = np.zeros([self.n, self.n])
                for i in range(self.n):
                    for j in range(self.n):
                        feature[i, j] = 1 / (eigen[i] * eigen[j])
            elif mode == 'random':
                feature = np.ones([self.n, self.n])
            else:
                print('unsupported mode')
            block = feature * np.sum(self.backbones) / np.sum(feature * self.backbones) * block_prob_val
            self.block_prob[mode] = self._get_prob(block, time_w, block_prob_val)

    def _get_prob(self, block, time_w, block_prob):
        if time_w:
            b = np.zeros([2, self.n, self.n])
            for i, c in self.contacts.iterrows():
                t, p1, p2 = c[['time', 'id1', 'id2']]
                if t < self.T5:
                    b[0, p1, p2] += 1
                else:
                    b[1, p1, p2] += 1
            bl = np.zeros([2, self.n, self.n])
            bl[0] = block * time_w[0]
            bl[1] = block * time_w[1]
            while True:
                bl[bl > 1] = 1
                new = np.sum(b) * block_prob - np.sum(b[bl == 1])
                old = np.sum((bl * b)[bl < 1])
                bl[bl < 1] = bl[bl < 1] * new / old
                bl[bl > 1] = 1
                if abs(np.sum(b * bl) - np.sum(b) * block_prob) < 0.01:
                    break
            return bl
        else:
            while True:
                block[block > 1] = 1
                new = np.sum(self.backbones) * block_prob - np.sum(self.backbones[block == 1])
                old = np.sum((block * self.backbones)[block < 1])
                block[block < 1] = block[block < 1] * new / old
                block[block > 1] = 1
                if abs(np.sum(self.backbones * block) - np.sum(self.backbones) * block_prob) < 0.01:
                    break
            return [block, block, block]

    # repeat is the spreading possibilities
    # change repeat here to add more simulations
    def spread(self, beta=0.01, start_node=0, repeat=1):
        self.rec_result = []
        self.infect_result = []
        self.infect = np.zeros(self.n, dtype=bool)
        self.rec = np.zeros(self.n, dtype=bool)

        t = min(self.contacts['time'])
        node = start_node  # let users be able to choose the start node rather than generating one randomly
        for i, (_, c) in tqdm(enumerate(self.contacts.iterrows())):
            tmp_rec = np.logical_and((np.random.random(size=self.rec.shape) < self.cure * (c['time'] - t)), self.infect)
            self.rec = np.logical_or(tmp_rec, self.rec)  # recovery situation of a specific person (i.e., node)
            self.infect = np.logical_and(self.infect, np.logical_not(
                self.rec))  # infection situation of a specific person (i.e., node)
            self.infect_result.append(np.where(self.infect == True)[0].tolist())
            self.rec_result.append(np.where(self.rec == True)[0].tolist())  # randomly select a node to be the seed node
            if i == 0:
                self.infect[node] = 1
            t = c['time']
            t_int = 1
            if t < self.T5:
                t_int = 0
            p1 = c['id1']
            p2 = c['id2']

            if self.block_prob[self.modes[0]][t_int][p1, p2] < np.random.random():
                if self.infect[p1] or self.infect[p2]:
                    if beta > np.random.random():
                        self.infect[p1] = 1
                        self.infect[p2] = 1
        return self.n, node, self.infect_result, self.rec_result


'''
Dimensions of infect:
0: at i-th contact
1: with i-th strategy
2: with i-th infect rate
3: i-th experiment
4: i-th node as seed node

Dimensions of rec:
0: with i-th strategy
1: with i-th infect rate
2: i-th experiment
3: i-th node as seed node
4: whether i-th node is recovered
'''
