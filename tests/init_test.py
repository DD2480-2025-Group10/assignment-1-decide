import json
from dataclasses import dataclass
from typing import Any


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


def test_example():
    d = load_data("./tests/whole_program_cases/case0_false.json")
    if d != None:
        assert True
