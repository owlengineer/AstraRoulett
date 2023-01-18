import numpy as np

from core.config import RevolverConfig


class Revolver:
    def __init__(self,
                 descr: str = RevolverConfig.DEFAULT_DESCR,
                 drum_count: int = RevolverConfig.DEFAULT_DRUM_COUNT,
                 drum_turn_period: float = RevolverConfig.DEFAULT_DRUM_TURN_PERIOD):
        self._descr = descr
        self._drum_count = drum_count
        self._drum_turn_period = drum_turn_period
        self._drum_load = np.zeros((drum_count,), dtype=bool)

    @property
    def drum_turn_period(self):
        return self._drum_turn_period

    @property
    def drum_load(self):
        return self._drum_load

    @property
    def drum_count(self):
        return self._drum_count

    @property
    def description(self):
        return self._descr

    @drum_count.setter
    def drum_count(self, value: int):
        if len(value) > RevolverConfig.MAX_DRUM_COUNT:
            raise ValueError(f"drum_count must not be larger than {RevolverConfig.MAX_DRUM_COUNT}")
        else:
            self._drum_count = value

    @drum_load.setter
    def drum_load(self, value: np.ndarray):
        if len(value) != self._drum_count:
            raise ValueError(f"drum_load size must be equal {self._drum_count}")
        if value.dtype != bool:
            raise TypeError(f"drum_load type must be numpy.nd_array")
        else:
            self._drum_load = value

    def __str__(self):
        return f"{self._descr} Размер барабана: {len(self._drum_load)}, время переключения между капсюлями по ттх: {self._drum_turn_period} секунд."