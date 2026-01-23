from src.lics import LIC3
from src.types import Parameters_T, PointList


# LIC3 tests: check whether there exists any set of three consecutive points
# whose triangle area is greater than the parameter `area`.


def test_calculate_lic_3_positive():
    # A simple triangle with area 0.5 -> should be greater than 0.4
    points: PointList = [(0.0, 0.0), (1.0, 0.0), (0.0, 1.0)]
    params = Parameters_T(area=0.4)

    assert LIC3().evaluate(points, params) is True

    # Larger list where a later triple satisfies the area condition
    points = [(0.0, 0.0), (0.1, 0.0), (0.15, 0.0), (0.0, 1.0), (1.0, 0.0)]
    # triple (0.0,1.0),(1.0,0.0),(0.2,0.0) contains a large triangle
    assert LIC3().evaluate(points, params) is True


def test_calculate_lic_3_negative():
    # Three collinear points area = 0, so with threshold > 0 it's False
    points: PointList = [(0.0, 0.0), (0.5, 0.0), (1.0, 0.0)]
    params = Parameters_T(area=0.1)

    assert LIC3().evaluate(points, params) is False

    # List shorter than 3 points should also be False
    points = [(0.0, 0.0), (1.0, 1.0)]
    assert LIC3().evaluate(points, params) is False