from src.utils import *
"""
This file will contain all 15 LIC functions

"""
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

def calculate_lic_4(points: List[Point], q_pts: int, quads: int) -> bool:
    quadrants = [Quadrant.from_point(point) for point in points]

    for i in range(len(quadrants) - q_pts + 1):
        unique_quadrants = set(quadrants[i:i + q_pts])

        if len(unique_quadrants) > quads:
            return True

    return False

class Ray: 
    def __init__(self, origin: Point, end: Point):
        self.origin = origin
        self.end = end

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


def calculate_lic_6(points: List[Point], n_pts: int, dist: float) -> bool:
    if len(points) < 3:
        return False

    for i in range(len(points) - n_pts + 1):
        point_slice = points[i:i + n_pts]
        A = point_slice[0]
        B = point_slice[-1]

        # Create Ray from A to B
        ray = Ray(A, B)

        # Evalueate if any intermediate point is at a distance greate than dist from the ray
        for point in point_slice[1:-1]:
            proj_point = ray.project_point(point)
            vec_diff = (point[0] - proj_point[0], point[1] - proj_point[1])
            if vector_magnitude(vec_diff) > dist:
                return True

    return False



