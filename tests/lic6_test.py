from typing import List
from src.utils import Point
from src.cmv import calculate_lic_6

# Test cases for LIC 6 calculation
# LIC 6 checks if there exists at least one set of points of a specified size such
# that one point is a distance greater than a specified value from the line formed
# by the two start and end points of the set.

def test_calculate_lic_6_positive():
    # Straight line with sufficient distance
    points: List[Point] = [(0,0), (2,2), (4,0)]
    n_pts = 3
    dist = 1.0

    assert calculate_lic_6(points, n_pts, dist) == True

    # Test with same point repeated
    points: List[Point] = [(0,0), (2,2), (0,0)]
    assert calculate_lic_6(points, n_pts, dist) == True

    # Multiple points with one exceeding distance
    points: List[Point] = [(0,0), (0,0), (1,5), (4,0)]
    assert calculate_lic_6(points, n_pts, dist) == True


def test_calculate_lic_6_negative():
    # Straight line with insufficient distance
    points: List[Point] = [(0,0), (2,2), (4,0)]
    n_pts = 3
    dist = 3.0

    assert calculate_lic_6(points, n_pts, dist) == False
