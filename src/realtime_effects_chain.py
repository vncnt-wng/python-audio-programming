from audio_stream import AudioStream
import pyaudio as pa
import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft
import struct

CHUNK = 1024 * 2
FORMAT = pa.paInt16
CHANNELS = 1
RATE = 44100 # in Hz
YRANGE = 2 ** 15

if __name__ == "__main__":

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
    
    stream = AudioStream(
        chunk=CHUNK,
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE
    )


    while 1:
        data = stream.read_chunk_data()
        dataInt = struct.unpack(str(CHUNK) + 'h', data)
        line1.set_ydata(dataInt)
        fd = fft(dataInt)
        line_fft.set_ydata(np.abs(fd[0:CHUNK])  / (512 * CHUNK))
        
        stream.write_chunk_data(data)
        
        fig.canvas.draw_idle()
        fig.canvas.flush_events()