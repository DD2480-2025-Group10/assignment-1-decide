from src.lics import LIC14
from src.types import Parameters_T, PointList

# LIC14 tests: check whether there exists:
# 1. At least one set of three data points separated by E_PTS and F_PTS
#    whose triangle area is GREATER than `area` (AREA1).
# AND
# 2. At least one set of three data points separated by E_PTS and F_PTS
#    whose triangle area is LESS than `area2` (AREA2).


def test_calculate_lic_14_positive():
    # Case 1: Separate groups satisfy conditions
    # Group 1 (Indices 0, 2, 4): (0,0), (2,0), (0,2) -> Area = 2.0 (> area=1.5)
    # Group 2 (Indices 1, 3, 5): (0,0), (0,0), (0,0) -> Area = 0.0 (< area2=0.5)
    points: PointList = [
        (0.0, 0.0),
        (0.0, 0.0),
        (2.0, 0.0),
        (0.0, 0.0),
        (0.0, 2.0),
        (0.0, 0.0),
    ]
    # E_PTS=1, F_PTS=1
    params = Parameters_T(area=1.5, area2=0.5, e_pts=1, f_pts=1)

    assert LIC14().evaluate(points, params) is True

    # Case 2: One single group satisfies BOTH conditions
    # Indices 0, 2, 4: (0,0), (4,0), (0,3) -> Area = 6.0
    # 6.0 is GREATER than area=5.0
    # 6.0 is LESS than area2=10.0
    points = [(0.0, 0.0), (1.1, 1.1), (4.0, 0.0), (1.1, 1.1), (0.0, 3.0)]
    params = Parameters_T(area=5.0, area2=10.0, e_pts=1, f_pts=1)

    assert LIC14().evaluate(points, params) is True

    # Case 3: Larger E and F values
    # We need indices i, i+3, i+5 (E=2, F=1)
    # Target points: (0,0), (3,0), (0,4) -> Area = 6.0
    # Condition: > 5.0 AND < 7.0
    points = [
        (0.0, 0.0),
        (9.9, 9.9),
        (9.9, 9.9),  # i=0, +2 skip
        (3.0, 0.0),
        (9.9, 9.9),  # +1 skip
        (0.0, 4.0),
    ]
    params = Parameters_T(area=5.0, area2=7.0, e_pts=2, f_pts=1)
    assert LIC14().evaluate(points, params) is True


def test_calculate_lic_14_negative():
    # Case 1: Only satisfying the "Greater Than" condition (Missing "Less Than")
    # All triangles here are huge (Area = 50.0).
    # area=10 (Satisfied: 50 > 10)
    # area2=20 (Failed: 50 is NOT < 20)
    points: PointList = [(0.0, 0.0), (0.1, 0.1), (10.0, 0.0), (0.1, 0.1), (0.0, 10.0)]
    params = Parameters_T(area=10, area2=20, e_pts=1, f_pts=1)

    assert LIC14().evaluate(points, params) is False

    # Case 2: Only satisfying the "Less Than" condition (Missing "Greater Than")
    # All points are collinear (Area = 0.0).
    # area=0.5 (Failed: 0 is NOT > 0.5)
    # area2=1.0 (Satisfied: 0 < 1.0)
    points = [(0.0, 0.0), (1.1, 1.1), (2.0, 2.0), (3.3, 3.3), (4.0, 4.0)]
    params = Parameters_T(area=0.5, area2=1.0, e_pts=1, f_pts=1)

    assert LIC14().evaluate(points, params) is False

    # Case 3: Not enough points (< 5)
    points = [(0.0, 0.0), (1.0, 0.0), (0.0, 1.0), (2.2, 2.2)]
    params = Parameters_T(area=0.1, area2=10.0, e_pts=1, f_pts=1)

    assert LIC14().evaluate(points, params) is False

    # Case 4: E/F points out of bounds test
    # Length 6. Need index i + 1 + 1 + 3 + 1 = i + 6.
    # Max index is 5. Loop should not run or find anything.
    points = [(0.0, 0.0), (0.1, 0.1), (4.0, 0.0), (0.1, 0.1), (0.1, 0.1), (0.0, 3.0)]
    params = Parameters_T(area=0.1, area2=10.0, e_pts=1, f_pts=3)
    assert LIC14().evaluate(points, params) is False
