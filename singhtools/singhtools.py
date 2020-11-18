import numpy as np

def singhvals(c_struct, target_dist, true_param=None, n_samples = 1000):
    assert n_samples >= 2, 'n_samples must be greater than 2.'
    n_samples = int(n_samples)
    if true_param is None:
        true_param = [T[0] for T in target_dist(n_samples)]
    else:
        true_param = [true_param]*n_samples
    if isinstance(c_struct(true_param[0], target_dist(1)[0]), (list, tuple, np.ndarray)):
        singhvals = [list(s) for s in [*zip(*map(c_struct, true_param, target_dist(n_samples)))]]
        [s.sort() for s in singhvals]
    else:
        singhvals = [*map(c_struct, true_param, target_dist(n_samples))]
        singhvals.sort()
    return  singhvals


def struct_to_consonant(c_struct, data):
    if isinstance(c_struct(domain[0], data), (list, tuple, np.ndarray)):
        return lambda x: 2 * c_struct(x, data)[1] if c_struct(x, data)[1] < 0.5 else 1 if c_struct(x, data)[0] < 0.5 else 2 * (1 - c_struct(x, data)[0])
    else:
        return lambda x: 2 * c_struct(x, data) if c_struct(x, data) < 0.5 else 2 * (1 - 2 * c_struct(x, data))
