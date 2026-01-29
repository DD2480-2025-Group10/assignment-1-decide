from src.lics import LIC4
from src.types import Parameters_T, PointList

# LIC 4 tests is a number of consecutive points lie in more than a specified number of quadrants


def test_calculate_lic_4_positive():
    # Q1, Q2, Q3, Q1 (Start of list)
    points: PointList = [(1, 1), (-1, 1), (-1, -1), (1, 2)]
    params = Parameters_T(quads=2, q_pts=3)

    # There the first three points lie in more than 2 quadrants
    assert LIC4().evaluate(points, params) == True

    # Q1, Q1, Q2, Q3 (End of list)
    points: PointList = [(1, 2), (1, 1), (-1, 1), (-1, -1)]
    # The last three points lie in more than 2 quadrants
    assert LIC4().evaluate(points, params) == True


def test_calculate_lic_4_negative():
    # Q1, Q1, Q2
    points: PointList = [(1, 1), (0, 0), (-1, -1)]
    params = Parameters_T(quads=2, q_pts=3)

    # No set of 3 consecutive points lie in more than 2 quadrants
    assert LIC4().evaluate(points, params) == False

    # Cannot be satisfied under normal program function be satisfied 
    # two points cannot lie in more than 2 quadrants
    points: PointList = [(1, 1), (0, 0), (-1, -1)]
    params = Parameters_T(quads=2, q_pts=2)

    assert LIC4().evaluate(points, params) == False
