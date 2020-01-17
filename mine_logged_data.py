import numpy as np

def generate_cpu_core_used(data, threshold_percent):
    cores = data.shape[1] - 5
    usage = np.where(data[:, 5:] > threshold_percent, 1, 0)
    usage = np.sum(usage, axis=-1)
    return usage
