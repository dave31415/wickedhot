import numpy as np


def res_sample(stream, k=50):
    # Reservoir Sampling from the stream
    reservoir = []
    for i, element in enumerate(stream):
        if i+1 <= k:
            reservoir.append(element)
        else:
            probability = k/(i+1)
            if np.random.random() < probability:
                # Select item in stream and remove one of the k items already selected
                index = np.random.choice(range(0, k))
                reservoir[index] = element

    return reservoir


def streaming_median(stream, k=50):
    reservoir = res_sample(stream, k=k)
    return np.median(reservoir)
