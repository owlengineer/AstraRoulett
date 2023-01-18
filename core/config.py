from dataclasses import dataclass


@dataclass(frozen=True)
class RevolverConfig:
    DEFAULT_DESCR: str = "Стандартный револьвер системы Colt. Классика дикого запада."
    DEFAULT_DRUM_COUNT: int = 6
    DEFAULT_DRUM_TURN_PERIOD: float = 0.5  # seconds
    MAX_DRUM_COUNT: int = 8