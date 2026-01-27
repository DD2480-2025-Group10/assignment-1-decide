from src.types import CONNECTORS
from src.types import PUM


class PumBuilder:
    """
    Creates the PUM based on the CMV and the LCM.
    """

    def build(self, cmv: list[bool], lcm: list[list[CONNECTORS]]) -> list[list[bool]]:
        """
        Constructs a 15x15 matrix where each element is a boolean
        representing the combination of two LICs according to the LCM.

        :param cmv: The 15-element boolean vector from CmvBuilder.
        :param lcm: The 15x15 matrix of logical connectors.
        :return: A 15x15 matrix representing the PUM.
        """
        if len(cmv) != 15:
            raise ValueError("CMV must have 15 elements.")

        pum = [[False for _ in range(15)] for _ in range(15)]

        for i in range(15):
            for j in range(15):
                connector = lcm[i][j]

                if connector == CONNECTORS.ANDD:
                    pum[i][j] = cmv[i] and cmv[j]
                elif connector == CONNECTORS.ORR:
                    pum[i][j] = cmv[i] or cmv[j]
                elif connector == CONNECTORS.NOTUSED:
                    # If NOTUSED, the PUM element is True.
                    pum[i][j] = True
                else:
                    raise ValueError(f"Unknown connector type: {connector}")

        return pum


# Export a singleton
DefaultPumBuilder = PumBuilder()
