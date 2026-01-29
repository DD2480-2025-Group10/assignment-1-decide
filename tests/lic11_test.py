from src.lics import LIC11
from src.types import Parameters_T, PointList

# LIC11 Tests
# LIC11 checks whetther there exists at least one set of two data points, (X[i],Y[i]) and (X[j],Y[j]), separated by
# exactly G PTS consecutive intervening points, such that X[j] - X[i] < 0. (where i < j ) Thecondition is not met when NUMPOINTS < 3.


def test_calculate_lic_11_positive():
    # i = 0, j = 0 + G_PTS + 1 = 2 -> xj - xi = 1.0 - 3.0 < 0 -> True
    points: PointList = [
        (3.0, 0.0),
        (2.0, 0.0),  # intervening
        (1.0, 0.0),
    ]

    params = Parameters_T(g_pts=1)

    assert LIC11().evaluate(points, params) is True

    # Different g-pts
    params = Parameters_T(g_pts=2)
    points: PointList = [
        (3.0, 0.0),
        (4.0, 0.0),  # intervening
        (4.0, 0.0),
        (1.0, 0.0),
    ]
    assert LIC11().evaluate(points, params) is True

    # Not at the start of the list
    params = Parameters_T(g_pts=1)
    points: PointList = [
        (1.0, 0.0),
        (3.0, 0.0),
        (4.0, 0.0),  # intervening
        (1.0, 0.0),
    ]

    assert LIC11().evaluate(points, params) is True



def test_calculate_lic_11_negative():
    # i = 0, j = 0 + G_PTS + 1 = 2 -> xj - xi = 3.0 - 1.0 is NOT < 0 -> False
    points: PointList = [
        (1.0, 0.0),
        (2.0, 0.0),  # intervening
        (3.0, 0.0),
    ]

    params = Parameters_T(g_pts=1)

    assert LIC11().evaluate(points, params) is False

    # Less than 3 points -> False
    points = [(1.0, 0.0), (2.0, 0.0)]
    params = Parameters_T(g_pts=1)

    assert LIC11().evaluate(points, params) is False
