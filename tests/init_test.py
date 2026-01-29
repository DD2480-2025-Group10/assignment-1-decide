from src.main import *
from src.utils import load_data, expand_lcm

def test_decide_case0_false():
    # Fails because the only required condition (LIC0) is not met.
    # Distance between points (0,0) and (1,0) is 1.0, which is NOT > LENGTH1 (5.0).
    # Since PUV[0] is True, FUV[0] becomes False, blocking the launch.
    d = load_data("./whole_program_cases/case0_false.json")

    if d.expected_launch is None:
        raise ValueError("Expected launch value is missing in the test data.")

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

    if d.expected_launch is None:
        raise ValueError("Expected launch value is missing in the test data.")

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

    if d.expected_launch is None:
        raise ValueError("Expected launch value is missing in the test data.")

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
