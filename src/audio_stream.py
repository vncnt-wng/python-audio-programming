import pyaudio as pa 

from typing import Any

class AudioStream: 
    
    def __init__(self, chunk=1024 * 2, format=pa.paInt16, channels=1, rate=44100) -> None:
        self.p = pa.PyAudio()
        self.chunk = chunk
        self.format = format
        self.channels = channels
        self.rate = rate
        
        self.stream = self.p.open(
            format = format,
            channels = channels,
            rate = rate,
            input=True,
            output=True,
            frames_per_buffer=chunk
        )

    def read_chunk_data(self) -> Any:
        return self.stream.read(self.chunk)
        
    def write_chunk_data(self, data) -> Any:
        self.stream.write(data)