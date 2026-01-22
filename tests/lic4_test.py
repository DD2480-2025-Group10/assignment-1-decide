from typing import List
from src.main import Point, calculate_lic_4

# LIC 4 tests is a number of consecutive points lie in more than a specified number of quadrants

def test_calculate_lic_4_positive():
    # Q1, Q2, Q3, Q1 (Start of list)
    points: List[Point] = [(1, 1), (-1, 1), (-1, -1), (1, 2)]
    q_pts = 3
    quads = 2
    # There the first three points lie in more than 2 quadrants
    assert calculate_lic_4(points, q_pts, quads) == True

    # Q1, Q1, Q2, Q3 (End of list)
    points: List[Point] = [(1, 2), (1, 1), (-1, 1), (-1, -1)]
    # The last three points lie in more than 2 quadrants
    assert calculate_lic_4(points, q_pts, quads) == True

def test_calculate_lic_4_negative():
    # Q1, Q1, Q2
    points: List[Point] = [(1, 1), (0, 0), (-1, -1)]
    q_pts = 3
    quads = 2
    # No set of 3 consecutive points lie in more than 2 quadrants
    assert calculate_lic_4(points, q_pts, quads) == False
