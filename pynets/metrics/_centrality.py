import numpy as np


def central_vertices(self, metric='degree', num_top=None):
    '''Get central vertices by specified metric.

    Currently, multiple eigenvector centralities are not
    implemented, only the _first_ eigenvalue is considered.

    Args:
        metric: Optional; one of 'degree' for degree
            centrality or 'eigen' for eigenvector centrality.
            Default 'degree'.
        num_top: Optional; if provided and not None,
            return only given number of most central
            vertices. Default: None.
    '''
    if metric == 'degree':
        centralities = _degree_central_vertices(self.mat)
    elif metric == 'eigen':
        centralities = _eigenvector_central_vertices(self.mat)
    else:
        raise Exception('Invalid metric.')

    if num_top:
        top_indices = centralities.argsort()[::-1][:num_top]
        vertices = {i: d for i, d in enumerate(centralities) if
                    i in top_indices}
    else:
        vertices = {i: d for i, d in enumerate(centralities)}

    return vertices


def _degree_central_vertices(mat):
    return mat.sum(axis=1)


def _eigenvector_central_vertices(mat):
    _, v = np.linalg.eig(mat)
    return 1 + v[:, 0]
