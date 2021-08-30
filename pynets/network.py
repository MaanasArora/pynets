from datarepr import AdjList, AdjMat


class Network:
    def __init__(self, adjlist=None, adjmat=None,
                 directed=False):
        if adjlist is None == adjmat is None:
            raise Exception(
                'must pass only one of adjacency list and adjacency matrix')

        if adjlist is not None:
            self.mat = AdjList(adjlist)
        if adjmat is not None:
            self.mat = AdjMat(adjmat)

        self.directed = directed
        self.nodes, self.dims = self.mat.make_nodes()