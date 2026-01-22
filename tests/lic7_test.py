from typing import List
from src.cmv import calculate_lic_7
from src.utils import Point

# LIC 7 Tests 
# LIC 7 checks whether there exists at least two points separated by k_pts consecutive intervening points
# such that the distance between the two points is greater than length1.

def test_calculate_lic_7_positive():
    points: List[Point] = [(0, 0), (1, 0), (5, 0), (10, 0)]
    k_pts = 2
    length1 = 8.0

    # (0,0) and (10,0) are separated by 2 intervening points and distance is 10 > 8
    assert calculate_lic_7(points, k_pts, length1) == True

    # (1,0) and (10,0) are separated by 1 intervening point and distance is 9 > 8
    k_pts = 1
    assert calculate_lic_7(points, k_pts, length1) == True

def test_calculate_lic_7_negative():
    points: List[Point] = [(0, 0), (1, 0), (2, 0), (3, 0)]
    k_pts = 1
    length1 = 5.0

    # No two points are separated by at least 1 intervening point with distance > 5
    assert calculate_lic_7(points, k_pts, length1) == False

