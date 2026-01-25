from src.lics import LIC10
from src.types import Parameters_T, PointList

# LIC10 tests: check whether there exists any set of set of three data points
# separated by exactly E PTS and F PTS con-secutive intervening points
# whose triangle area is greater than the parameter `area`.


def test_calculate_lic_3_positive():
    # A simple triangle with area 0.5 -> should be greater than 0.4
    points: PointList = [(0.0, 0.0), (0.0, 0.0), (2.0, 0.0), (0.0, 0.0), (0.0, 2.0)]
    params = Parameters_T(area=0.5, e_pts=1, f_pts=1)

    assert LIC10().evaluate(points, params) is True

    # Larger list where a later triple satisfies the area condition
    points = [
        (0.0, 0.0),
        (0.0, 0.0),
        (0.0, 0.0),
        (0.0, 0.0),
        (0.0, 0.0),
        (0.0, 0.0),
        (3.0, 0.0),
        (0.0, 0.0),
        (0.0, 4.0),
    ]
    assert LIC10().evaluate(points, params) is True

    points = [(0.0, 0.0), (9.0, 9.0), (9.0, 9.0), (3.0, 0.0), (9.0, 9.0), (0.0, 3.0)]
    params = Parameters_T(area=1, e_pts=2, f_pts=1)
    assert LIC10().evaluate(points, params) is True

    points = [
        (0.0, 0.0),
        (0.1, 0.1),
        (4.0, 0.0),
        (0.1, 0.1),
        (0.1, 0.1),
        (0.1, 0.1),
        (0.0, 3.0),
    ]
    params = Parameters_T(area=5, e_pts=1, f_pts=3)
    assert LIC10().evaluate(points, params) is True


def test_calculate_lic_3_negative():
    # Three collinear points area = area1, False
    points: PointList = [(0.0, 0.0), (0.0, 0.0), (1.0, 0.0), (0.0, 0.0), (0.0, 1.0)]
    params = Parameters_T(area=0.5, e_pts=1, f_pts=1)

    assert LIC10().evaluate(points, params) is False

    # List shorter than 3 points should also be False
    points = [(0.0, 0.0), (1.0, 1.0)]
    assert LIC10().evaluate(points, params) is False

    # Points on the same line
    points = [(0.0, 0.0), (9.9, 9.9), (1.0, 1.0), (8.8, 8.8), (2.0, 2.0)]
    assert LIC10().evaluate(points, params) is False

    points = [(0.0, 0.0), (5.0, 0.0), (0.0, 5.0), (1.0, 1.0), (9.9, 9.9), (2.0, 2.0)]
    params = Parameters_T(area=1, e_pts=2, f_pts=1)
    assert LIC10().evaluate(points, params) is False

    points = [(0.0, 0.0), (0.1, 0.1), (4.0, 0.0), (0.1, 0.1), (0.1, 0.1), (0.0, 3.0)]
    params = Parameters_T(area=5, e_pts=1, f_pts=3)
    assert LIC10().evaluate(points, params) is False
