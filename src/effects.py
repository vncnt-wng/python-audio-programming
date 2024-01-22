from __future__ import annotations
import numpy as np
from abc import ABC
from typing import List


class Effect(ABC):
    wet: float = 1.0

    def process(self, sample: np.float32):
        pass


class SignalChain(Effect):
    def __init__(self, effects: List[Effect]):
        self.effects = effects

    def process(self, sample: np.float32) -> bytes:
        for effect in self.effects:
            sample = effect.process(sample)
        return sample


class Gain(Effect):
    def __init__(self, mult: float):
        self.mult = mult

    def process(self, sample):
        return sample * self.mult


class FeedForwardComb(Effect):
    def __init__(self, delay_samples: int, b0: float = 1.0, bM: float = 1.0):
        self.delay_samples = delay_samples
        self.buffer = np.zeros((delay_samples,))
        self.buffer_index = 0
        self.b0 = b0
        self.bM = bM

    def process(self, sample):
        result = (
            self.b0 * sample
            + self.bM * self.buffer[(self.buffer_index + 1) % self.delay_samples]
        )

        self.buffer[self.buffer_index] = sample
        self.buffer_index += 1
        if self.buffer_index == self.delay_samples:
            self.buffer_index = 0

        return result


class FeedBackComb(Effect):
    def __init__(self, delay_samples: int, b0: float = 1.0, feedback: float = 0.5):
        self.delay_samples = delay_samples
        self.buffer = np.zeros((delay_samples,))
        self.buffer_index = 0
        self.b0 = b0
        self.feedback = feedback

    def process(self, sample):
        result = (
            self.b0 * sample
            + self.feedback * self.buffer[(self.buffer_index + 1) % self.delay_samples]
        )

        self.buffer[self.buffer_index] = result
        self.buffer_index += 1
        if self.buffer_index == self.delay_samples:
            self.buffer_index = 0

        return result
