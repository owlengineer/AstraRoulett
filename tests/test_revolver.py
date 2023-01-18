import numpy as np

from core.revolver import Revolver


def test_revolver_descr():
    """Testing standart configuration"""
    r = Revolver()

    assert str(r) == "Стандартный револьвер системы Colt. Классика дикого запада. Размер барабана: 6," \
                            " время переключения между капсюлями по ттх: 0.5 секунд."


def test_revolver_drum_load_success():
    """Testing success loading bullets into existing standart revolver"""
    r = Revolver()

    load = np.asarray([True, False, False, False, False, False])
    r.drum_load = load
    assert load.all() == r.drum_load.all()


def test_revolver_drum_load_size_fail():
    """Testing failed loading bullets into existing standart revolver"""
    res = False
    r = Revolver()

    load = np.asarray([True, True, True, False, False, False, False, False])
    try:
        r.drum_load = load
    except ValueError:
            res = True
    assert res
