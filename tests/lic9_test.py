from src.lics import LIC9
from src.types import Parameters_T, PointList
from src.utils import Pi

def test_calculate_lic_9_positive():
    # Test where with small epsilon, the angle condition is met
    # the angle inside condition should almost always be met
    params = Parameters_T(c_pts=1, d_pts=1, epsilon=0.01)
    points: PointList = [(0.0, 1.0), (1.0, 0.0), (0.0, 0.0), (0.0, 0.0), (1.0, 0.0)]

    # angle between pi/2
    assert LIC9().evaluate(points, params) is True

    # Test where angle is larger than pi + epsilon
    params = Parameters_T(c_pts=1, d_pts=1, epsilon=0.00)
    points = [(0.0, 1.0), (1.0, 0.0), (0.0, 0.0), (0.0, 1.0), (-1.0, -1.0)]

    # angle greater than pi
    assert LIC9().evaluate(points, params) is True

    # test with other d_pts and c_pts
    params = Parameters_T(c_pts=2, d_pts=2, epsilon=0.00)
    points = [(0.0, 1.0), (1.0, 0.0), (1.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 1.0), (-1.0, -1.0)]

    assert LIC9().evaluate(points, params) is True

def test_calculate_lic_9_negative():
    # Test where NUMPOINTS < 5
    params = Parameters_T(c_pts=1, d_pts=1, epsilon=0.01)
    points: PointList = []

    assert LIC9().evaluate(points, params) is False

    # Test where all points are conincient
    points: PointList = [(0.0, 0.0),(0.0, 0.0),(0.0, 0.0),(0.0, 0.0),(0.0, 0.0)]

    assert LIC9().evaluate(points, params) is False

    # Test where angle is > pi - epsilon and < pi + epsilon
    params = Parameters_T(c_pts=1, d_pts=1, epsilon=Pi)
    points = [(0.0, 1.0), (1.0, 0.0), (0.0, 0.0), (0.0, -1.0), (1.0, 0.0)]

    assert LIC9().evaluate(points, params) is False
