from enum import Enum, auto
import math
from typing import List, Tuple
from dataclasses import dataclass

Point = Tuple[float, float]

#CONSTANTS
Pi: float = 3.1415926535


class CONNECTORS(Enum):
    NOTUSED = 777
    ORR = auto()
    ANDD = auto()


class COMPTYPE(Enum):
    LT = 1111
    EQ = auto()
    GT = auto()

@dataclass
class Parameters_T:
    length1: float      # Length in LICs 0, 7,  12
    radius1: float      # Radius in LICs 1, 8,  13
    epsilon: float      # Deviation from P1 in LICs 2,  9
    area: float         # Area in LICs 3,  10,  14
    q_pts: float        # No. of consecutive points in LIC  4
    quads: float        # No. of quadrants in LIC 4
    dist: float         # Distance in LIC 6
    n_pts: int          # No. of consecutive pts. in LIC 6
    k_pts: int          # No. of int. pts. in LICs  7, 12
    a_pts: int          # No. of int. pts. in LICs  8, 13
    b_pts: int          # No. of int. pts. in LICs  8, 13
    c_pts: int          # No. of int. pts. in LICs  9
    d_pts: int          # No. of int. pts. in LICs  9
    e_pts: int          # No. of int. pts. in LICs  10, 14
    f_pts: int          # No. of int. pts. in LICs  10, 14
    g_pts: int          # No. of int. pts. in LICs  11
    length2: float      # Maximum length in LIC 12
    radius2: float      # Maximum radius in LIC 13
    area2: float        # Maximum area in LIC 14


# GLOBAL VARIABLES

PARAMETERS2: Parameters_T

POINTS: List[Point]


NUMPOINTS: int

# 2D array of [15, 15] CONNECTORS
LCM: List[List[CONNECTORS]]

# 2D array of [15, 15] booleans
PUM: List[List[bool]]

# array of 15 booleans
CMV: List[bool]

# array of 15 booleans
FUV: List[bool]

LAUNCH: bool

# floating point
def double_compare(a: float, b: float, eps: float = 1e-6) -> COMPTYPE:
    if math.fabs(a - b) < eps:
        return COMPTYPE.EQ
    if a < b:
        return COMPTYPE.LT
    return COMPTYPE.GT

def calculate_distance(p1: Point, p2: Point) -> float:
    """
    Calculates the Euclidean distance between two points.

    :param p1: The first point (x, y).
    :param p2: The second point (x, y).
    :return: The distance between p1 and p2 (float).
    """
    return math.dist(p1, p2)


def calculate_angle(p1: Point, vertex: Point, p3: Point) -> float:
    """
    Calculates the angle <p1, vertex, p3> in radians.

    :param p1: The first point (x, y).
    :param vertex: The vertex point (x, y).
    :param p3: The third point (x, y).
    :return: The angle in radians in the range [0, PI]. Returns None if the vertex
             coincides with p1 or p3 (undefined angle).
    """
    if (double_compare(p1[0], vertex[0]) == COMPTYPE.EQ and double_compare(p1[1], vertex[1]) == COMPTYPE.EQ) or \
       (double_compare(p3[0], vertex[0]) == COMPTYPE.EQ and double_compare(p3[1], vertex[1]) == COMPTYPE.EQ):
        return -1.0

    x1, y1 = p1
    xv, yv = vertex
    x3, y3 = p3

    ax, ay = x1 - xv, y1 - yv
    bx, by = x3 - xv, y3 - yv

    dot_product = ax * bx + ay * by
    mag_a = math.sqrt(ax**2 + ay**2)
    mag_b = math.sqrt(bx**2 + by**2)

    if math.isclose(mag_a * mag_b, 0):
        return None

    cos_val = dot_product / (mag_a * mag_b)
    cos_val = max(-1.0, min(1.0, cos_val))

    return math.acos(cos_val)