import numpy as np
import pyaudio as pa 
import struct 
import matplotlib.pyplot as plt 
from fft import dft
from scipy.fft import fft

CHUNK = 1024 * 2
FORMAT = pa.paInt16
CHANNELS = 1
RATE = 44100 # in Hz
YRANGE = 2 ** 15

p = pa.PyAudio()

stream = p.open(
    format = FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input=True,
    output=True,
    frames_per_buffer=CHUNK
)



fig,(ax1, ax2) = plt.subplots(2)
x = np.arange(0,2*CHUNK,2)
line1, = ax1.plot(x, np.random.rand(CHUNK),'r')

xf = np.linspace(0, RATE, CHUNK)     # frequencies (spectrum)
# create semilogx line for spectrum
line_fft, = ax2.semilogx(xf, np.random.rand(CHUNK), 'r')

ax1.set_ylim(-YRANGE, YRANGE)
ax1.set_xlim = (0,CHUNK)
ax2.set_xlim(20, RATE / 2)

fig.show()

while 1:
    data = stream.read(CHUNK)
    dataInt = struct.unpack(str(CHUNK) + 'h', data)
    line1.set_ydata(dataInt)
    fd = fft(dataInt)
    line_fft.set_ydata(np.abs(fd[0:CHUNK])  / (512 * CHUNK))
    
    stream.write(data)
    
    fig.canvas.draw_idle()
    fig.canvas.flush_events()