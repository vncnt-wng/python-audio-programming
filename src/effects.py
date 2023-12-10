from __future__ import annotations
import numpy as np
from abc import ABC
from typing import List

class Effect(ABC):
    wet: float
    
    def process(self, data: bytes):
        pass
    
class SignalChain():
    def __init__(self, effects: List[Effect]):
        self.effects = effects
        
    def process(self, data: bytes) -> bytes:
        data_np = np.frombuffer(data)
        for effect in self.effects:
            data_np = effect
        return np.tobytes(data_np)
    
class Delay(Effect):
    def __init__(self, time, feedback, wet, sample_rate=44100):
        self.time = time
        self.feedback = feedback 
        self.wet = wet
        self.delay_line = time * sample_rate
    
    def process(self, data):
        