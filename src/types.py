from dataclasses import dataclass
from enum import Enum, auto
from typing import Any

Point = tuple[float, float]
PointList = list[Point]

@dataclass
class Data:
    numpoints: int
    x: list[float]
    y: list[float]
    parameters: dict[str, Any]
    lcm: dict[str, Any]
    puv: list[int]
    expected_launch: bool

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
    length1: float = 0.0  # Length in LICs 0, 7,  12
    radius1: float = 0.0  # Radius in LICs 1, 8,  13
    epsilon: float = 0.0  # Deviation from P1 in LICs 2,  9
    area: float = 0.0  # Area in LICs 3,  10,  14
    q_pts: int = 0  # No. of consecutive points in LIC  4
    quads: int = 0  # No. of quadrants in LIC 4
    dist: float = 0.0  # Distance in LIC 6
    n_pts: int = 0  # No. of consecutive pts. in LIC 6
    k_pts: int = 0  # No. of int. pts. in LICs  7, 12
    a_pts: int = 0  # No. of int. pts. in LICs  8, 13
    b_pts: int = 0  # No. of int. pts. in LICs  8, 13
    c_pts: int = 0  # No. of int. pts. in LICs  9
    d_pts: int = 0  # No. of int. pts. in LICs  9
    e_pts: int = 0  # No. of int. pts. in LICs  10, 14
    f_pts: int = 0  # No. of int. pts. in LICs  10, 14
    g_pts: int = 0  # No. of int. pts. in LICs  11
    length2: float = 0.0  # Maximum length in LIC 12
    radius2: float = 0.0  # Maximum radius in LIC 13
    area2: float = 0.0  # Maximum area in LIC 14
