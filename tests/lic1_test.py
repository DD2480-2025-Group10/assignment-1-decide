from src.lics import LIC1
from src.types import Parameters_T, PointList

# LIC1 Tests
# LIC1 checks whether there exists at least one set of three consecutive points
# that cannot all be contained within or on a circle of radius radius1.


def test_calculate_lic_1_positive():
    # Collinear: required radius = (max distance)/2 = 2/2 = 1.0
    points: PointList = [(0.0, 0.0), (1.0, 0.0), (2.0, 0.0)]
    params = Parameters_T(radius1=0.9)
    assert LIC1().evaluate(points, params) is True

    # Right triangle 3-4-5: required radius = 5/2 = 2.5
    points = [(0.0, 0.0), (3.0, 0.0), (0.0, 4.0)]
    params.radius1 = 2.4
    assert LIC1().evaluate(points, params) is True

    # Obtuse triangle: (0,0),(4,0),(1,1) has longest side 4 -> required radius = 2.0
    points = [(0.0, 0.0), (4.0, 0.0), (1.0, 1.0)]
    params.radius1 = 1.9
    assert LIC1().evaluate(points, params) is True

    # Acute triangle: (0,0),(2,0),(1,2) has circumradius = 1.25
    points = [(0.0, 0.0), (2.0, 0.0), (1.0, 2.0)]
    params.radius1 = 1.2
    assert LIC1().evaluate(points, params) is True


def test_calculate_lic_1_negative():
    # Collinear: required radius = 1.0 (fits exactly)
    points: PointList = [(0.0, 0.0), (1.0, 0.0), (2.0, 0.0)]
    params = Parameters_T(radius1=1.0)
    assert LIC1().evaluate(points, params) is False

    # Right triangle 3-4-5: required radius = 2.5 (fits exactly)
    points = [(0.0, 0.0), (3.0, 0.0), (0.0, 4.0)]
    params.radius1 = 2.5
    assert LIC1().evaluate(points, params) is False

    # Obtuse triangle: required radius = 2.0 (fits exactly)
    points = [(0.0, 0.0), (4.0, 0.0), (1.0, 1.0)]
    params.radius1 = 2.0
    assert LIC1().evaluate(points, params) is False

    # Acute triangle: circumradius = 1.25 (fits exactly)
    points = [(0.0, 0.0), (2.0, 0.0), (1.0, 2.0)]
    params.radius1 = 1.25
    assert LIC1().evaluate(points, params) is False

    # Fewer than 3 points should be False
    points = [(0.0, 0.0), (1.0, 1.0)]
    assert LIC1().evaluate(points, params) is False
