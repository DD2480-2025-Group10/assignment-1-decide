from src.lics import LIC8
from src.types import Parameters_T, PointList

# LIC8: uses points[i], points[i + a_pts + 1], points[i + a_pts + b_pts + 2]
# True if any such triple cannot fit in/on a circle of radius1.
# False if NUMPOINTS < 5.


def test_calculate_lic_8_positive():
    # A=1, B=1 -> triple (0,2,4) is 3-4-5, needs 2.5 > 2.4
    points: PointList = [(0.0, 0.0), (0.0, 0.0), (3.0, 0.0), (0.0, 0.0), (0.0, 4.0)]
    params = Parameters_T(a_pts=1, b_pts=1, radius1=2.4)
    assert LIC8().evaluate(points, params) is True

    # A=2, B=1 -> triple (0,3,5) has longest side 4, needs 2.0 > 1.9
    points = [(0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (4.0, 0.0), (0.0, 0.0), (1.0, 1.0)]
    params = Parameters_T(a_pts=2, b_pts=1, radius1=1.9)
    assert LIC8().evaluate(points, params) is True


def test_calculate_lic_8_negative():
    # NUMPOINTS < 5 -> always False
    points: PointList = [(0.0, 0.0), (3.0, 0.0), (0.0, 4.0), (1.0, 1.0)]
    params = Parameters_T(a_pts=1, b_pts=1, radius1=0.1)
    assert LIC8().evaluate(points, params) is False

    # A=1, B=1 -> triple (0,2,4) fits at 2.5
    points = [(0.0, 0.0), (0.0, 0.0), (3.0, 0.0), (0.0, 0.0), (0.0, 4.0)]
    params = Parameters_T(a_pts=1, b_pts=1, radius1=2.5)
    assert LIC8().evaluate(points, params) is False

    # Indices out of range -> False
    points = [(0.0, 0.0)] * 5
    params = Parameters_T(a_pts=2, b_pts=2, radius1=1.0)
    assert LIC8().evaluate(points, params) is False
