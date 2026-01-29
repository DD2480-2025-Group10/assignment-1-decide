import math
import json
from src.main import *
from src.types import COMPTYPE, CONNECTORS, Parameters_T, PointList, Data

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



def load_data(path: str) -> Data:
    """
    helper function for turning json files into input for decide()
    param: path to json file
    return: Data datatype with test case.
    """
    with open(path) as f:
        data = json.load(f)

    return Data(
        numpoints=data["NUMPOINTS"],
        x=data["X"],
        y=data["Y"],
        parameters=data["PARAMETERS"],
        lcm=data["LCM"],
        puv=data["PUV"],
        expected_launch=bool(data["EXPECTED"]["LAUNCH"]),
    )


def expand_lcm(lcm_json: dict) -> list[list[CONNECTORS]]:
    """
    Helper function to change format of cases to usable info for our code

    param: dict: LCM of json file
    Returns:
        list[list[CONNECTORS]]: LCM in different format
    """
    default = CONNECTORS[lcm_json["default"]]
    matrix = [[default for _ in range(15)] for _ in range(15)]

    for override in lcm_json["overrides"]:
        i = override["i"]
        j = override["j"]
        val = CONNECTORS[override["value"]]
        matrix[i][j] = val
        matrix[j][i] = val

    return matrix
