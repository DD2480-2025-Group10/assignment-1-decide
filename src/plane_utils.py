from enum import Enum, auto
import math
from typing import Optional 

from src.utils import double_compare
from src.types import Point, COMPTYPE

# A Quadrant splits the plane into for quadrants separated by each of the 
# coordiante axes.
#
# The quadrants are numbered as follows:
# Q1: Positive X, Positive Y
# Q2: Negative X, Positive Y
# Q3: Negative X, Negative Y
# Q4: Positive X, Negative Y
class Quadrant(Enum): 
    Q1 = auto()
    Q2 = auto()
    Q3 = auto()
    Q4 = auto()

    @classmethod
    def from_point(cls, point: Point) -> 'Quadrant':
        x, y = point
        if x >= 0 and y >= 0:
            return cls.Q1
        elif x < 0 and y >= 0:
            return cls.Q2
        elif x < 0 and y < 0:
            return cls.Q3
        else:
            return cls.Q4

# A Ray is defined by an origin point and an end point.
# It defines a line between the origin and end point.
class Ray: 
    def __init__(self, origin: Point, end: Point):
        self.origin = origin
        self.end = end

    # Projects a point onto the ray anr returns the projected point.
    def project_point(self, point: Point) -> Point:
        # shorthanded as A(origin), B(end), C(point), D(projection)
 
        # Create vectors from origin to end and origin to point, 
        AB = (self.end[0] - self.origin[0], self.end[1] - self.origin[1])
        AC = (point[0] - self.origin[0], point[1] - self.origin[1])

        denom = dot_product(AB, AB)
        # Origin and end are the same point avoid division by zero
        if denom == 0:
            return self.origin

        # Projection formula: proj_AB(AC) = (AB . AC / AB . AB) * AB
        scalar = dot_product(AC, AB) / denom
        AD = (AB[0] * scalar, AB[1] * scalar)

        return (self.origin[0] + AD[0], self.origin[1] + AD[1])

def calculate_distance(p1: Point, p2: Point) -> float:
    """
    Calculates the Euclidean distance between two points.

    :param p1: The first point (x, y).
    :param p2: The second point (x, y).
    :return: The distance between p1 and p2 (float).
    """
    return math.dist(p1, p2)

# Takes the dot product of two 2D vectors
def dot_product(v1: Point, v2: Point) -> float:
    return v1[0] * v2[0] + v1[1] * v2[1]

# Takes the magnitude of a 2D vector
def vector_magnitude(v: Point) -> float:
    return math.sqrt(v[0]**2 + v[1]**2)

def calculate_angle(p1: Point, vertex: Point, p3: Point) -> Optional[float]:
    """
    Calculates the angle <p1, vertex, p3> in radians.

    :param p1: The first point (x, y).
    :param vertex: The vertex point (x, y).
    :param p3: The third point (x, y).
    :return: The angle in radians in the range [0, PI]. Returns None if the vertex
             coincides with p1 or p3 (undefined angle).
    """
    if (double_compare(p1[0], vertex[0]) == COMPTYPE.EQ and double_compare(p1[1], vertex[1]) == COMPTYPE.EQ) or \
       (double_compare(p3[0], vertex[0]) == COMPTYPE.EQ and double_compare(p3[1], vertex[1]) == COMPTYPE.EQ):
        return -1.0

    x1, y1 = p1
    xv, yv = vertex
    x3, y3 = p3

    ax, ay = x1 - xv, y1 - yv
    bx, by = x3 - xv, y3 - yv

    dot_product = ax * bx + ay * by
    mag_a = math.sqrt(ax**2 + ay**2)
    mag_b = math.sqrt(bx**2 + by**2)

    if math.isclose(mag_a * mag_b, 0):
        return None

    cos_val = dot_product / (mag_a * mag_b)
    cos_val = max(-1.0, min(1.0, cos_val))

    return math.acos(cos_val)
