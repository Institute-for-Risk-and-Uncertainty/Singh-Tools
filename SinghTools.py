import numpy as np
from tqdm import tqdm

def Singh(CStruct, TargetDist, TrueParam, SSamples = 1000, TQDM=False):
    assert SSamples >= 2 and isinstance(SSamples, int), 'SSamples must be an integer greater than 2.'
    Samples = TargetDist(SSamples)
    if isinstance(CStruct(TrueParam, Samples[0]), np.ndarray):
        assert len(CStruct(TrueParam, Samples[0])) == 2, 'Confidence Structure must have defined lower and upper limit distributions.'
        if TQDM:
            SinghVals = np.sort([[CStruct[0](TrueParam, S), CStruct[1](TrueParam, S)] for S in tqdm(Samples)], 0)
        else:
            SinghVals = np.sort([[CStruct[0](TrueParam, S), CStruct[1](TrueParam, S)] for S in Samples], 0)
    else:
        if TQDM:
            SinghVals = np.sort([CStruct(TrueParam, S) for S in tqdm(Samples)], 0)
        else:
            SinghVals = np.sort([CStruct(TrueParam, S) for S in Samples], 0)
    
    if len(np.shape(SinghVals)) > 1:
        if np.shape(SinghVals)[1] != SSamples:
            SinghVals = SinghVals.T
    return SinghVals

def SinghFast(CStruct, TargetDist, TrueParam, SSamples = 1000, TQDM=False):
    assert SSamples >= 2 and isinstance(SSamples, int), 'SSamples must be an integer greater than 2.'
    Samples = TargetDist(SSamples)
    if isinstance(CStruct(TrueParam, Samples[0]), np.ndarray):
        assert len(CStruct(TrueParam, Samples[0])) == 2, 'Confidence Structure must have defined lower and upper limit distributions.'
        if TQDM:
            SinghVals = [a for a in [[CStruct[0](TrueParam, S), CStruct[1](TrueParam, S)] for S in tqdm(Samples)].sort()]
        else:
            SinghVals = [a for a in [[CStruct[0](TrueParam, S), CStruct[1](TrueParam, S)] for S in Samples].sort()]
    else:
        if TQDM:
            SinghVals = np.sort([CStruct(TrueParam, S) for S in tqdm(Samples)], 0)
        else:
            SinghVals = np.sort([CStruct(TrueParam, S) for S in Samples], 0)
    
    if len(np.shape(SinghVals)) > 1:
        if np.shape(SinghVals)[1] != SSamples:
            SinghVals = SinghVals.T
    return SinghVals