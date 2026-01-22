from src.utils import *
"""
This file will contain all 15 LIC functions

"""

def LIC0() -> bool:

    if NUMPOINTS < 2:
        return False
    
    for i in range(NUMPOINTS - 1):
        distance = calculate_distance(POINTS[i], POINTS[i + 1])
        if double_compare(distance, PARAMETERS2.length1) == COMPTYPE.GT:
            return True
        
        return False