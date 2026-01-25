from src.lics import LIC2
from src.types import Parameters_T, PointList

# LIC2 Tests
# LIC2 checks whether there exists at least one set of three consecutive data points which form an angle 
# such that: angle < (PI − EPSILON) or angle > (PI + EPSILON) 
# The second of the three consecutive points is always the vertex of the angle. 
# If either the first point or the last point (or both) coincides with the vertex, 
# the angle is undefined and the LIC is not satisfied by those three points

def test_calculate_lic_2_positive():
    # Angle = 45 degrees ~ 0.785 rad < PI - 0.5 -> True
    points: PointList = [
        (1.0, 0.0),
        (0.0, 0.0), # vertex
        (1.0, 1.0)
    ]

    params = Parameters_T(epsilon=0.5)

    assert LIC2().evaluate(points, params) is True


def test_calculate_lic_2_negative():
    # Angle = 180 degrees ~ PI rad NOT < PI - 0.1 -> False
    # PI rad NOT > PI + 0.1 -> False
    points: PointList = [
        (-1.0, 0.0),
        (0.0, 0.0), # vertex
        (1.0, 0.0)
    ]

    params = Parameters_T(epsilon=0.1)

    assert LIC2().evaluate(points, params) is False