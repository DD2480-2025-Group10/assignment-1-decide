from src.lics import LIC0
from src.types import Parameters_T, PointList

# LIC0 Tests
# LIC0 checks whether there exists at least one pair of two consecutive points
# such that the distance between them is greater than LENGTH1.


def test_calculate_lic_0_positive():
    # Horizontal distance, distance = 5.0 > LENGTH1
    points: PointList = [(0.0, 0.0), (5.0, 0.0)]  # Distance = 5.0
    params = Parameters_T(length1=4.9)
    assert LIC0().evaluate(points, params) is True

    # Diagonal distance, distance = sqrt(13) ~ 3.605 > LENGTH1
    points = [(0.0, 0.0), (3.0, 2.0)]  # distance = sqrt(13) ~ 3.605
    params.length1 = 3.6
    assert LIC0().evaluate(points, params) is True


def test_calculate_lic_0_negative():
    # Distance equal to LENGTH1 should be False
    points: PointList = [(0.0, 0.0), (4.0, 3.0)]  # distance = 5.0
    params = Parameters_T(length1=5.0)
    assert LIC0().evaluate(points, params) is False

    # Single point: Fewer than 2 points should be False
    points = [(0.0, 0.0)]
    assert LIC0().evaluate(points, params) is False

    # Distance less than LENGTH1 should be False
    points = [(0.0, 0.0), (1.0, 1.0)]  # distance = sqrt(2) ~ 1.414
    params.length1 = 2.0
    assert LIC0().evaluate(points, params) is False

    # No points: Fewer than 2 points should be False
    points = []
    assert LIC0().evaluate(points, params) is False
