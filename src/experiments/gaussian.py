import numpy as np
import numpy.typing as npt

def gaussian(x, mu, sigma):
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.power(np.e, -(1/2) * np.power(((x - mu)/sigma), 2))

def get_gaussian_window(length, stdevs_from_mean=3):
    # TODO look into gaussian bell curve
    window = [gaussian(x, length / 2, length / (stdevs_from_mean * 2)) for x in range(length)]
    return np.array(window)