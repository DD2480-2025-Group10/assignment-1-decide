from src.cmv import *
from src.utils import *

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


# function you must write
def decide():
    pass


if __name__ == "__main__":
    decide()

