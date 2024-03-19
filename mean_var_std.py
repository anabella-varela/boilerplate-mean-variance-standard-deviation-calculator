import numpy as np


def calculate (list):
    
#error message
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')
    else:
        d1 = np.array(list).reshape(3,3)
        mean = [d1.mean(axis=0).tolist(), d1.mean(axis=1).tolist(), d1.mean()]
        var = [d1.var(axis=0).tolist(), d1.var(axis=1).tolist(), d1.var()]
        std = [d1.std(axis=0).tolist(), d1.std(axis=1).tolist(), d1.std()]
        min = [d1.min(axis=0).tolist(), d1.min(axis=1).tolist(), d1.min()]
        max = [d1.max(axis=0).tolist(), d1.max(axis=1).tolist(), d1.max()]
        sum = [d1.sum(axis=0).tolist(), d1.sum(axis=1).tolist(), d1.sum()]

        return {
            'mean': mean,
            'variance': var,
            'standard deviation': std,
            'max': max,
            'min': min,
            'sum': sum
        }
