from src.lics import LIC13
from src.types import Parameters_T, PointList


def test_calculate_lic_13_positive():
    # A=1, B=1 -> triples (0,2,4) and (1,3,5)
    # (0,2,4) is 3-4-5 -> cannot fit r1=2.4
    # (1,3,5) -> can fit r2=1.0
    points: PointList = [
        (0.0, 0.0),  # 0
        (0.0, 0.0),  # 1
        (3.0, 0.0),  # 2
        (0.0, 0.0),  # 3
        (0.0, 4.0),  # 4
        (0.5, 0.0),  # 5
    ]
    params = Parameters_T(a_pts=1, b_pts=1, radius1=2.4, radius2=1.0)
    assert LIC13().evaluate(points, params) is True

    # Same triple works for both parts (fails r1 but fits r2)
    points = [(0.0, 0.0), (0.0, 0.0), (3.0, 0.0), (0.0, 0.0), (0.0, 4.0)]
    params = Parameters_T(a_pts=1, b_pts=1, radius1=2.4, radius2=2.5)
    assert LIC13().evaluate(points, params) is True


def test_calculate_lic_13_negative():
    # NUMPOINTS < 5 -> always False
    points: PointList = [(0.0, 0.0), (3.0, 0.0), (0.0, 4.0), (1.0, 1.0)]
    params = Parameters_T(a_pts=1, b_pts=1, radius1=0.1, radius2=10.0)
    assert LIC13().evaluate(points, params) is False

    # Part A false: all triples fit radius1=3.0 (3-4-5 needs 2.5)
    points = [(0.0, 0.0), (0.0, 0.0), (3.0, 0.0), (0.0, 0.0), (0.0, 4.0)]
    params = Parameters_T(a_pts=1, b_pts=1, radius1=3.0, radius2=10.0)
    assert LIC13().evaluate(points, params) is False

    # Part B false: no triple fits radius2=0.1, but some fail radius1=2.4
    points = [(0.0, 0.0), (0.0, 0.0), (3.0, 0.0), (0.0, 0.0), (0.0, 4.0), (0.5, 0.0)]
    params = Parameters_T(a_pts=1, b_pts=1, radius1=2.4, radius2=0.1)
    assert LIC13().evaluate(points, params) is False
