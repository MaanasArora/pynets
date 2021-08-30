import numpy as np


class DataRepr:
    def __init__(self, data):
        self.data = np.array(data)
        if not self.valid_shape():
            raise Exception('Invalid data shape')


class AdjList(DataRepr):
    def valid_shape(self):
        if not len(self.data.shape) == 2:
            return False

        if not self.data.shape[1] == 2:
            return False

        return True

    def make_nodes(self):
        nodes = np.unique(self.data)
        nodes = np.sort(nodes)

        dims = len(nodes)
        return nodes, dims


class AdjMat(DataRepr):
    def valid_shape(self):
        if not len(self.data.shape) == 2:
            return False

        if not self.data.shape[0] == self.data.shape[1]:
            return False

        return True

    def make_nodes(self):
        dims = self.data.shape[0]

        nodes = np.arange(dims)
        return nodes, dims
