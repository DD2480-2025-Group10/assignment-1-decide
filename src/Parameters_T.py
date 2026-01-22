from dataclasses import dataclass

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
