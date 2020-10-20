import numpy as np

class singhplot():
    def __init__(
        self,
        c_struct=None,
        target_dist=None,
        true_param=None,
        n_samples=None):
        if not any([c_struct is None, target_dist is None, true_param is None, n_samples is None]):
            self.singhvals = singhvals


def singhvals(c_struct, target_dist, true_param, n_samples = 1000):
    assert n_samples >= 2, 'n_samples must be greater than 2.'
    n_samples = int(n_samples)
    #samples = target_dist(n_samples)
    if isinstance(c_struct(true_param, target_dist(1)[0]), (list, tuple, np.ndarray)):
        singhvals = [list(s) for s in [*zip(*map(c_struct, [true_param]*n_samples, target_dist(n_samples)))]]
        [s.sort() for s in singhvals]
    else:
        singhvals = [*map(c_struct, [true_param]*n_samples, target_dist(n_samples))]
        singhvals.sort()
    return  singhvals