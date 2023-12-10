import numpy as np
import numpy.typing as npt
from gaussian import get_gaussian_window
import matplotlib.pyplot as plt

SAMPLE_RATE = 44100
SAMPLE_TIME = 0.01
NUM_SAMPLES = int(SAMPLE_TIME * SAMPLE_RATE)
SAMPLE_INTERVAL = 1 / SAMPLE_RATE

def dft_iter(xs: npt.NDArray): 
    N = len(xs)
    
    
    
    
    
def dft(xs: npt.NDArray):
    N = len(xs)
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, xs)

def idft(fs: npt.NDArray):
    pass

if __name__ == "__main__":
    f = 100
    t = np.arange(0, SAMPLE_TIME, SAMPLE_INTERVAL)
    freqs = t / SAMPLE_INTERVAL
    signal = np.sin(2 * np.pi * f * t)
    fig, (ax1, ax2, ax3) = plt.subplots(3)
    ax1.plot(t, signal)
    dft_signal = dft(signal)
    ax2.plot(freqs[:NUM_SAMPLES // 2], np.abs(dft_signal)[0:NUM_SAMPLES // 2] / (NUM_SAMPLES // 2))
    plt.show()
    
