import numpy as np
import soundfile as sf

data, samplerate = sf.read("../samples/epiano.wav")
left = data[:, 0]

DEGREES_PER_OCTAVE = 2

STARTING_FREQUENCY = 10
