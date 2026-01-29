from src.cmv import *
from src.utils import *
from src.fuv import *
from src.pum import *


# function you must write
def decide(
    points: list[tuple[float, float]],
    parameters: Parameters_T,
    lcm: list[list[CONNECTORS]],
    puv: list[bool],
) -> bool:
    """
    Determines if an interceptor should be launched based on radar tracking data.

    The function follows a three-stage pipeline:
    1. CMV: Evaluates 15 Launch Interceptor Conditions (LICs).
    2. PUM: Combines CMV results with the Logical Connector Matrix (LCM).
    3. FUV: Masks the PUM with the Preliminary Unlocking Vector (PUV) to
       generate the Final Unlocking Vector.

    :param points: A list of (x, y) coordinates representing radar echoes.
    :param parameters: Configuration values for the 15 LICs.
    :param lcm: 15x15 matrix defining the logical relationships between LICs.
    :param puv: 15-element vector indicating which LICs are required for launch.
    :return: True if all conditions in the FUV are met, else False.
    """
    cmv = DefaultCmvBuilder.build(points, parameters)

    pum = DefaultPumBuilder.build(cmv, lcm)

    fuv = DefaultFuvBuilder.build(puv, pum)

    # Iff all entries in FUV are true we launch
    if all(fuv):
        print("The rockets are launched")
    else:
        print("No rockets are launched")
    return all(fuv)


if __name__ == "__main__":
    decide()
