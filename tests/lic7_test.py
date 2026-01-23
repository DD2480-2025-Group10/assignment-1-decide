from src.cmv import LIC7
from src.types import Parameters_T, PointList

# LIC 7 Tests 
# LIC 7 checks whether there exists at least two points separated by k_pts consecutive intervening points
# such that the distance between the two points is greater than length1.

def test_calculate_lic_7_positive():
    points: PointList = [(0, 0), (1, 0), (5, 0), (10, 0)]
    params = Parameters_T(k_pts = 2 ,length1 = 8.0)

    # (0,0) and (10,0) are separated by 2 intervening points and distance is 10 > 8
    assert LIC7().evaluate(points, params) == True

    # (1,0) and (10,0) are separated by 1 intervening point and distance is 9 > 8
    params.k_pts = 1
    assert LIC7().evaluate(points, params) == True

def test_calculate_lic_7_negative():
    points: PointList = [(0, 0), (1, 0), (2, 0), (3, 0)]
    params = Parameters_T(k_pts = 1 ,length1 = 5.0)

    # No two points are separated by at least 1 intervening point with distance > 5
    assert LIC7().evaluate(points, params) == False

