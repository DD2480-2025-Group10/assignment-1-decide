from src.lics import LIC5
from src.types import Parameters_T, PointList

# LIC5 Tests
# LIC5 checks whether there exists at least one set of two consecutive data points,
# (X[i],Y[i]) and (X[j],Y[j]), such that X[j] - X[i] < 0 (where j = i + 1).


def test_calculate_lic_5_positive():
    # X[1] (0.0) - X[0] (1.0) = -1.0 which is < 0 -> True
    points: PointList = [
        (1.0, 5.0),
        (0.0, 2.0),
    ]

    params = Parameters_T()

    assert LIC5().evaluate(points, params) is True


def test_calculate_lic_5_negative():
    # X[1] (2.0) - X[0] (1.0) = 1.0 (>= 0)
    # X[2] (3.0) - X[1] (2.0) = 1.0 (>= 0)
    # No consecutive points satisfy X[j] < X[i] -> False
    points: PointList = [
        (1.0, 0.0),
        (2.0, 0.0),
        (3.0, 10.0),
    ]

    params = Parameters_T()

    assert LIC5().evaluate(points, params) is False


def test_calculate_lic_5_boundary_equal_x():
    # X[1] (1.0) - X[0] (1.0) = 0.0
    # 0.0 is NOT < 0, so this should be False.
    points: PointList = [
        (1.0, 5.0),
        (1.0, 2.0),
    ]

    params = Parameters_T()

    assert LIC5().evaluate(points, params) is False
