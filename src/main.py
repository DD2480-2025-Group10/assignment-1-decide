from enum import Enum, auto
import math
from typing import List
from dataclasses import dataclass


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

X: List[float]
Y: List[float]


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

# function you must write
def decide():
    pass