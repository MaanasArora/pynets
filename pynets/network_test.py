import numpy as np
from network import Network


def test_network_init():
    network = Network(adjlist=[[4, 6], [5, 6], [6, 4]])
    assert all(network.nodes == np.array([4, 5, 6]))