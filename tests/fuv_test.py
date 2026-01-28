from src.fuv import *


def test_all_true():
    # should be all True since pum is all True
    puv = [True] * 15
    pum = [[True for _ in range(15)] for _ in range(15)]
    fuv = DefaultFuvBuilder.build(puv, pum)
    assert all(fuv)


def test_all_false_puv():
    # PUV all False → all FUV should be True regardless of PUM
    puv = [False] * 15
    pum = [[False for _ in range(15)] for _ in range(15)]
    fuv = DefaultFuvBuilder.build(puv, pum)
    assert all(fuv)


def test_partial_true_rows():
    # PUV has some True and some False, PUM has mixed rows
    puv = [True, False, True, True, False] + [True] * 10
    pum = [
        [
            True,
            False,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
        ],  # row 0 → not all True
        [False] * 15,  # row 1 → all False
        [True] * 15,  # row 2 → all True → FUV[2] = True
        [True] * 15,  # row 3 → all True → FUV[3] = True
        [False] * 15,  # row 4 → PUV[4] = False → FUV[4] = True
    ] + [[True] * 15 for _ in range(10)]
    fuv = DefaultFuvBuilder.build(puv, pum)
    assert fuv[0] == False
    assert fuv[1] == True
    assert fuv[2] == True
    assert fuv[3] == True
    assert fuv[4] == True


def test_in_lab_sheet():
    puv = [True, False, True] + [True] * 12
    pum = [
        [
            True,
            False,
            True,
            False,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
        ],  # row 0
        [False] * 15,
        [True] * 15,
    ] + [[True] * 15 for _ in range(12)]
    fuv = DefaultFuvBuilder.build(puv, pum)
    assert fuv[0] == False
    assert fuv[1] == True
    assert fuv[2] == True
