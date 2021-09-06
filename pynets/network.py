import numpy as np


class Network:
    '''Generic network class.

    Currently, only undirected and unweighted networks are supported.

    Attributes:
        mat: an 2D ndarray for the adjacency matrix of the network
    '''

    def __init__(self, mat):
        self.mat = np.array(mat)
