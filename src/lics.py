from dataclasses import dataclass
from typing import Protocol

from src.plane_utils import (
    Quadrant,
    Ray,
    calculate_distance,
    calculate_triangle_area,
    vector_magnitude,
)
from src.types import COMPTYPE, Parameters_T, Point, PointList
from src.utils import double_compare


# Protocol for LIC Rule classes
# This defines the interface that all LIC rule implementations must follow.
class LicRule(Protocol):
    # Unique identifier for the launch interception condition,
    # this is to make sure each rule is ordered correctly.
    # :Use the indetifier from the respective LICS rule set (ex. LIC2 -> 2)
    @property
    def ident(self) -> int: ...

    # Evaluete function for the LIC rule.
    # :Param points: List of points to evaluate the rule on
    # :Param params: Parameters_T object containing all parameters
    def evaluate(self, points: PointList, params: Parameters_T) -> bool: ...


# **********************************
# Conctete LIC Rule Implementations
# **********************************


@dataclass(frozen=True)
class LIC1:
    ident: int = 1

    def evaluate(self, points: PointList, params: Parameters_T) -> bool:
        R = params.radius1

        if len(points) < 3:
            return False

        for i in range(len(points) - 2):
            p1, p2, p3 = points[i], points[i + 1], points[i + 2]
            if not self.three_points_fit_in_circle(p1, p2, p3, R):
                return True

        return False

    @staticmethod
    def three_points_fit_in_circle(p1: Point, p2: Point, p3: Point, R: float) -> bool:
        a = calculate_distance(p2, p3)
        b = calculate_distance(p1, p3)
        c = calculate_distance(p1, p2)

        if (
            double_compare(a, 0.0) == COMPTYPE.EQ
            and double_compare(b, 0.0) == COMPTYPE.EQ
            and double_compare(c, 0.0) == COMPTYPE.EQ
        ):
            return True

        area = calculate_triangle_area(p1, p2, p3)

        # collinear
        if double_compare(area, 0.0) == COMPTYPE.EQ:
            required = max(a, b, c) / 2.0
            return double_compare(required, R) != COMPTYPE.GT

        a2, b2, c2 = a * a, b * b, c * c

        # obtuse or right
        if (
            double_compare(a2 + b2, c2) != COMPTYPE.GT
            or double_compare(a2 + c2, b2) != COMPTYPE.GT
            or double_compare(b2 + c2, a2) != COMPTYPE.GT
        ):
            required = max(a, b, c) / 2.0
            return double_compare(required, R) != COMPTYPE.GT

        # acute
        circumradius = (a * b * c) / (4.0 * area)
        return double_compare(circumradius, R) != COMPTYPE.GT


@dataclass(frozen=True)
class LIC3:
    ident: int = 3

    """
    Evaluates LIC3: There exists at least one set of three consecutive data
    points that are the vertices of a triangle with area greater than AREA1.
    (0 ≤ AREA1)
    """

    def evaluate(self, points: PointList, params: Parameters_T) -> bool:
        for i in range(0, len(points) - 2):
            area = calculate_triangle_area(points[i], points[i + 1], points[i + 2])
            if double_compare(area, params.area) == COMPTYPE.GT:
                return True
        return False


@dataclass(frozen=True)
class LIC4:
    ident: int = 4

    """
    Evaluates LIC4: There exists at least one set of Q_PTS consecutive points
    that lie in more than QUADS quadrants. That is, Q_PTS points in a row that
    lie in separate quartants, such that the number of quartants is greater
    than QUADS.
    """

    def evaluate(self, points: PointList, params: Parameters_T) -> bool:
        quadrants = [Quadrant.from_point(point) for point in points]

        for i in range(len(quadrants) - params.q_pts + 1):
            unique_quadrants = set(quadrants[i : i + params.q_pts])

            if len(unique_quadrants) > params.quads:
                return True

        return False


@dataclass(frozen=True)
class LIC6:
    ident: int = 6

    """
    Evaluates LIC6: There exists at least one set of N_PTS consecutive points
    such that at least one intermediate point is a distance greater than dist
    from the line segment joining the first and last points of the set.
    """

    def evaluate(self, points: PointList, params: Parameters_T) -> bool:
        if len(points) < 3:
            return False

        for i in range(len(points) - params.n_pts + 1):
            point_slice = points[i : i + params.n_pts]
            A = point_slice[0]
            B = point_slice[-1]

            # Create Ray from A to B
            ray = Ray(A, B)

            # Evalueate if any intermediate point is at a distance greate than dist from the ray
            for point in point_slice[1:-1]:
                proj_point = ray.project_point(point)
                vec_diff = (point[0] - proj_point[0], point[1] - proj_point[1])
                if vector_magnitude(vec_diff) > params.dist:
                    return True

        return False


@dataclass(frozen=True)
class LIC7:
    ident: int = 7

    """
    Evaluates LIC7: There exists at least one set of K_PTS consecutive points
    such that the distance between the first and last point is greater than LENGTH1.
    """

    def evaluate(self, points: PointList, params: Parameters_T) -> bool:
        if len(points) < 3:
            return False

        for i in range(len(points) - params.k_pts - 1):
            A = points[i]
            B = points[i + params.k_pts + 1]

            if calculate_distance(A, B) > params.length1:
                return True

        return False
