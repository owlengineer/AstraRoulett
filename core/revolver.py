import math
import random

import numpy as np

from core.config import RevolverConfig


import logging
logger = logging.getLogger('root')


class Revolver:
    def __init__(self,
                 name: str = RevolverConfig.DEF_NAME,
                 descr: str = RevolverConfig.DEF_DESCR,
                 drum_capacity: int = RevolverConfig.DEF_DRUM_CAPACITY):
        self._name = name
        self._descr = descr
        self._barrel_bullet_index = 0
        self._drum_capacity = drum_capacity
        self._drum_load = np.zeros((drum_capacity,), dtype=bool)

    @property
    def barrel_bullet_index(self):
        return self._barrel_bullet_index

    @property
    def drum_load(self):
        return self._drum_load

    @property
    def drum_capacity(self):
        return self._drum_capacity

    @property
    def description(self):
        return self._descr

    @property
    def name(self):
        return self._name

    @drum_capacity.setter
    def drum_capacity(self, value: int):
        if value > RevolverConfig.MAX_DRUM_CAPACITY:
            raise ValueError(f"drum_capacity must not be larger than {RevolverConfig.MAX_DRUM_CAPACITY}")
        if value < RevolverConfig.MIN_DRUM_CAPACITY:
            raise ValueError(f"drum_capacity must be larger than {RevolverConfig.MIN_DRUM_CAPACITY}")
        else:
            self._drum_capacity = value

    @drum_load.setter
    def drum_load(self, value: np.ndarray):
        if len(value) != self._drum_capacity:
            raise ValueError(f"drum_load size must be equal {self._drum_capacity}")
        if value.dtype != bool:
            raise TypeError(f"drum_load type must be numpy.nd_array")
        else:
            self._drum_load = value

    def __str__(self):
        return f"{self._descr} " \
               f"Размер барабана: {len(self._drum_load)}"

    def shot(self) -> bool:
        """
        Imitating shot after spinning the drum.
        """
        self._barrel_bullet_index = random.randint(0,self.drum_capacity-1)
        return self._drum_load[self._barrel_bullet_index]

    def reload_drum(self, bullets_count: int = RevolverConfig.DEF_BULLETS_COUNT):
        """
        Randomize drum load with bullets count got.
        
        @param bullets_count: integer, less than drum capacity,
        """
        if bullets_count > self.drum_capacity:
            raise ValueError(f"bullets_count must not be larger than {self.drum_capacity}")

        load = [True for _ in range(bullets_count)] + \
               [False for _ in range(self.drum_capacity - bullets_count)]
        load = np.asarray(load)
        np.random.shuffle(load)
        self.drum_load = load
        logger.info(f"Drum load generated: {self.drum_load}")