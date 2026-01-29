import json
from dataclasses import dataclass
from typing import Any
from src.main import *
from src.types import CONNECTORS


@dataclass
class Data:
    numpoints: int
    x: list[float]
    y: list[float]
    parameters: dict[str, Any]
    lcm: dict[str, Any]
    puv: list[int]
    expected_launch: bool


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


def test_decide_case0_false():
    # Fails because the only required condition (LIC0) is not met.
    # Distance between points (0,0) and (1,0) is 1.0, which is NOT > LENGTH1 (5.0).
    # Since PUV[0] is True, FUV[0] becomes False, blocking the launch.
    d = load_data("./whole_program_cases/case0_false.json")

    points = list(zip(d.x, d.y))
    params = Parameters_T(**d.parameters)
    puv = [bool(v) for v in d.puv]
    lcm = expand_lcm(d.lcm)

    launch = decide(
        points=points,
        parameters=params,
        lcm=lcm,
        puv=puv,
    )

    assert launch == d.expected_launch


def test_decide_case0_true():
    # Launch is TRUE because PUV is all zeros.
    # Even though there are no points (NUMPOINTS=0) and all LICs fail (CMV=False),
    # the PUV indicates that no conditions are required to authorize a launch.
    d = load_data("./whole_program_cases/case0_true.json")

    points = list(zip(d.x, d.y))
    params = Parameters_T(**d.parameters)
    puv = [bool(v) for v in d.puv]
    lcm = expand_lcm(d.lcm)

    launch = decide(
        points=points,
        parameters=params,
        lcm=lcm,
        puv=puv,
    )

    assert launch == d.expected_launch


def test_decide_case1_true():
    # Launch is TRUE because all PUV entries are False (0).
    # Even though coordinates are provided and some LCM overrides exist,
    # a zeroed-out PUV means no LICs are required for launch.
    # Therefore, all FUV elements become True by default.
    d = load_data("./whole_program_cases/case1_true.json")

    points = list(zip(d.x, d.y))
    params = Parameters_T(**d.parameters)
    puv = [bool(v) for v in d.puv]
    lcm = expand_lcm(d.lcm)

    launch = decide(
        points=points,
        parameters=params,
        lcm=lcm,
        puv=puv,
    )

    assert launch == d.expected_launch
