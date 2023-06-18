import numpy as np


def weighted_median(data: np.ndarray, weights: np.ndarray) -> int:
    """
    Args:
      data (list or numpy.array): data
      weights (list or numpy.array): weights
    """
    if not isinstance(data, np.ndarray):
        data = np.array(data)
    if not isinstance(weights, np.ndarray):
        weights = np.array(weights)

    s_data, s_weights = map(np.sort, [data, weights])
    midpoint = 0.5 * np.sum(s_weights)

    if s_weights[-1] > midpoint:
        return data[weights == np.max(weights)][0]
    cs_weights = np.cumsum(s_weights)
    idx = np.where(cs_weights <= midpoint)[0][-1]
    return (
        np.mean(s_data[idx : idx + 2])
        if cs_weights[idx] == midpoint
        else s_data[idx + 1]
    )
