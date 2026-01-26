from src.lics import (
    LIC0,
    LIC1,
    LIC10,
    LIC12,
    LIC13,
    LIC14,
    LIC2,
    LIC3,
    LIC4,
    LIC6,
    LIC7,
    LIC8,
    LIC5,
    LicRule,
)
from src.types import Parameters_T, PointList


class CmvBuilder:
    LicRules: dict[int, LicRule]

    def __init__(self):
        self.LicRules = {}

    def register_lic(self, lic_rule: LicRule) -> "CmvBuilder":
        ident = lic_rule.ident

        if not (0 <= ident < 15):
            raise ValueError(f"LIC Rule ident {ident} is out of valid range (0-14).")

        if ident in self.LicRules:
            raise ValueError(f"LIC Rule with ident {ident} is already registered.")

        self.LicRules[ident] = lic_rule
        return self

    def build(self, points: PointList, params: Parameters_T) -> list[bool]:
        missing = set(range(15)) - set(self.LicRules.keys())

        if missing:
            raise ValueError(
                f"Not all LIC Rules are registered. Missing idents: {missing}"
            )

        cmv = [False] * 15
        for ident, lic_rule in self.LicRules.items():
            cmv[ident] = lic_rule.evaluate(points, params)

        return cmv


# Add LICS to the default builder, other code can then inport this singleton and
# use it to build the CMV directly.
DefaultCmvBuilder = (
    CmvBuilder()
    .register_lic(LIC0())
    .register_lic(LIC1())
    .register_lic(LIC2())
    .register_lic(LIC3())
    .register_lic(LIC4())
    .register_lic(LIC5()) 
    .register_lic(LIC6())
    .register_lic(LIC7())
    .register_lic(LIC8())
    # Add LIC9 later
    .register_lic(LIC10())
    # Add LIC11 later
    .register_lic(LIC12())
    .register_lic(LIC13())
    .register_lic(LIC14())
)
