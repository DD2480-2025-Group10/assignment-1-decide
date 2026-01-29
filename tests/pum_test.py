from src.pum import *
from src.types import CONNECTORS


def test_pum_notused():
    """
    Test that CONNECTORS.NOTUSED always results in True in the PUM,
    regardless of whether the CMV values are True or False.
    """
    # CMV with False values
    cmv = [False] * 15
    # LCM filled entirely with NOTUSED
    lcm = [[CONNECTORS.NOTUSED for _ in range(15)] for _ in range(15)]

    pum = DefaultPumBuilder.build(cmv, lcm)

    assert all(all(row) for row in pum)


def test_pum_andd():
    """
    Test that CONNECTORS.ANDD correctly performs logical AND.
    """
    cmv = [False] * 15
    cmv[0] = True
    cmv[1] = True
    cmv[2] = False

    lcm = [[CONNECTORS.NOTUSED for _ in range(15)] for _ in range(15)]
    lcm[0][1] = CONNECTORS.ANDD  # True ANDD True -> True
    lcm[0][2] = CONNECTORS.ANDD  # True ANDD False -> False

    pum = DefaultPumBuilder.build(cmv, lcm)

    assert pum[0][1] is True
    assert pum[0][2] is False


def test_pum_orr():
    """
    Test that CONNECTORS.ORR correctly performs logical OR.
    """
    cmv = [False] * 15
    cmv[0] = True
    cmv[1] = False
    cmv[2] = False

    lcm = [[CONNECTORS.NOTUSED for _ in range(15)] for _ in range(15)]
    lcm[0][1] = CONNECTORS.ORR  # True ORR False -> True
    lcm[1][2] = CONNECTORS.ORR  # False ORR False -> False

    pum = DefaultPumBuilder.build(cmv, lcm)

    assert pum[0][1] is True
    assert pum[1][2] is False
