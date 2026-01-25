from src.lics import LIC12
from src.types import Parameters_T, PointList


def test_calculate_lic_13_positive():
    # Simple case where length1 < dist < length2
    # for the same pair of points
    params = Parameters_T(length1=1.0, length2=3.0, k_pts=1)
    points: PointList = [(0.0, 0.0), (0.5, 0.0), (2.0, 0.0)]

    assert LIC12().evaluate(points, params) is True

    # Different pairs of ponts satisfy each of the lengths
    params = Parameters_T(length1=5.0, length2=2.0, k_pts=1)
    points = [(0.0, 0.0), (0.0, 0.0), (6.0, 0.0), (1.0, 0.0)]

    assert LIC12().evaluate(points, params) is True

    # Different K_PTS
    params = Parameters_T(length1=1.0, length2=3.0, k_pts=2)
    points: PointList = [(0.0, 0.0), (0.25, 0.0), (0.75, 0.0), (2.0, 0.0)]

    assert LIC12().evaluate(points, params) is True


def test_calculate_lic_13_negative():
    # Less than 3 points -> always false
    params = Parameters_T(length1=0.5, length2=2.0, k_pts=1)
    points: PointList = [(0.0, 0.0), (0.5, 0.5)]

    assert LIC12().evaluate(points, params) is False

    # No pair of points satisfy length1 < dist < length2
    # neither side of the condition is satisfied
    params = Parameters_T(length1=10.0, length2=0.0, k_pts=1)
    points = [(0.0, 0.0), (0.5, 0.0), (1.0, 0.0), (1.5, 0.0), (2.0, 0.0)]

    assert LIC12().evaluate(points, params) is False

    # Left side satisfied but not right side
    params = Parameters_T(length1=10.0, length2=0.0, k_pts=1)
    points = [(0.0, 0.0), (0.5, 0.0), (11.0, 0.0)]

    assert LIC12().evaluate(points, params) is False

    # Left side satisfied but not right side
    params = Parameters_T(length1=10.0, length2=0.0, k_pts=1)
    points = [(0.0, 0.0), (0.5, 0.0), (1.0, 0.0)]

    assert LIC12().evaluate(points, params) is False


