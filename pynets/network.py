import numpy as np


class Network:
    '''Generic network class.

    Currently, only undirected and unweighted networks are
    supported.

    Attributes:
        mat: an 2D ndarray for the adjacency matrix of the 
            network.
    '''

    from pynets.metrics._centrality import central_vertices

    def __init__(self, mat):
        if np.array(mat).shape[0] != np.array(mat).shape[1]:
            raise Exception('Invalid matrix shape')

        self.mat = np.array(mat)

    def adjlist(self):
        '''Retrieves an adjacency list representation of the
        network.

        For future compatibility, duplicate (reverse) edges
        for the undirected network are included in the list.

        Returns:
            A ndarray of shape (number of nodes, 2) representing
            the adjacency list matrix.
        '''
        return np.array(np.where(self.mat))

    def degree(self, indx):
        '''Get the degree of a vertex.

        Args:
            indx: vertex index

        Returns:
            Degree of given vertex.
        '''
        return np.count_nonzero(self.mat[indx])

    def neighbors(self, indx):
        '''Get the neighbors of a vertex.

        Args:
            indx: vertex index

        Returns:
            A list of indices of the neighbors of given
            vertex.
        '''
        return np.where(self.mat[indx] != 0)