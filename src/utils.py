import math

from src.types import COMPTYPE, CONNECTORS, Parameters_T, PointList

# CONSTANTS
Pi: float = 3.1415926535

# GLOBAL VARIABLES

PARAMETERS2: Parameters_T

POINTS: PointList

NUMPOINTS: int

# 2D array of [15, 15] CONNECTORS
LCM: list[list[CONNECTORS]]

# 2D array of [15, 15] booleans
PUM: list[list[bool]]

# array of 15 booleans
CMV: list[bool]

# array of 15 booleans
FUV: list[bool]

LAUNCH: bool

# array of 15 booleans - ADD THIS LINE
PUV: list[bool]

# array of 15 booleans
FUV: list[bool]


# floating point
def double_compare(a: float, b: float, eps: float = 1e-6) -> COMPTYPE:
    if math.fabs(a - b) < eps:
        return COMPTYPE.EQ
    if a < b:
        return COMPTYPE.LT
    return COMPTYPE.GT
