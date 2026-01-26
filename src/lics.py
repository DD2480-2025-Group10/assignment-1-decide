from dataclasses import dataclass
from typing import Protocol
import math

from src.plane_utils import (
    Quadrant,
    Ray,
    calculate_distance,
    calculate_triangle_area,
    three_points_fit_in_circle,
    vector_magnitude,
    calculate_angle,
)
from src.types import COMPTYPE, Parameters_T, PointList
from src.utils import Pi, double_compare


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
class LIC0:
    ident: int = 0
    """
    Evaluates LIC0: There exists at least one set of two consecutive data points 
    such that the distance between them is greater than LENGTH1. (0 ≤ LENGTH1)
    """

    def evaluate(self, points: PointList, params: Parameters_T) -> bool:
        if len(points) < 2:
            return False

        for i in range(len(points) - 1):
            p1 = points[i]
            p2 = points[i + 1]
            if calculate_distance(p1, p2) > params.length1:
                return True

        return False


@dataclass(frozen=True)
class LIC1:
    ident: int = 1

    def evaluate(self, points: PointList, params: Parameters_T) -> bool:
        radius = params.radius1

        if len(points) < 3:
            return False

        for i in range(len(points) - 2):
            p1, p2, p3 = points[i], points[i + 1], points[i + 2]
            if not three_points_fit_in_circle(p1, p2, p3, radius):
                return True

        return False


@dataclass(frozen=True)
class LIC2:
    ident: int = 2
    """
    There exists at least one set of three consecutive data points which form an angle 
    such that: angle < (PI - EPSILON) or angle > (PI + EPSILON) 
    The second of the three consecutive points is always the vertex of the angle. 
    If either the first point or the last point (or both) coincides with the vertex, 
    the angle is undefined and the LIC is not satisfied by those three points.
    """

    def evaluate(self, points: PointList, params: Parameters_T) -> bool:
        if len(points) < 3:
            return False

        epsilon = params.epsilon

        for i in range(len(points) - 2):
            p1 = points[i]
            vertex = points[i + 1]
            p3 = points[i + 2]

            angle = calculate_angle(p1, vertex, p3)

            if angle is None or angle < 0:
                continue  # Undefined angle

            if (
                double_compare(angle, math.pi - epsilon) == COMPTYPE.LT
                or double_compare(angle, math.pi + epsilon) == COMPTYPE.GT
            ):
                return True

        return False


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


@dataclass(frozen=True)
class LIC8:
    ident: int = 8

    """
    Evaluates LIC8: There exists at least one set of three data points separated by
    exactly A PTS and B PTS consecutive intervening points, respectively, that cannot
    be contained within or on a circle ofradius RADIUS1. The condition is not met when
    NUMPOINTS < 5.
    """

    def evaluate(self, points: PointList, params: Parameters_T) -> bool:
        if len(points) < 5:
            return False

        a_pts = params.a_pts
        b_pts = params.b_pts
        radius = params.radius1

        max_i = len(points) - (a_pts + b_pts + 3)
        if max_i < 0:
            return False

        for i in range(max_i + 1):
            p1 = points[i]
            p2 = points[i + a_pts + 1]
            p3 = points[i + a_pts + b_pts + 2]

            if not three_points_fit_in_circle(p1, p2, p3, radius):
                return True

        return False

@dataclass(frozen=True)
class LIC9:
    ident: int = 9

    """
    There exists at least one set of three data points separated by exactly C_PTS and D_PTS
    consecutive intervening points, respectively, that form an angle such that:
    angle < (PI−EPSILON) or angle > (PI+EPSILON)
    The second point of the set of three points is always the vertex of the angle. If either the first
    point or the last point (or both) coincide with the vertex, the angle is undefined and the LIC
    is not satisfied by those three points. When NUMPOINTS < 5, the condition is not met.
    """

    def evaluate(self, points: PointList, params: Parameters_T) -> bool:
        if len(points) < 5:
            return False

        condition1 = lambda x : x < Pi - params.epsilon
        condition2 = lambda x : x > Pi + params.epsilon
        angleInTolerance = lambda x : condition1(x) or condition2(x)

        for i in range(len(points) - params.c_pts - params.d_pts - 2):
            A = points[i]
            Vertex = points[i + params.c_pts + 1]
            B = points[i + params.c_pts + params.d_pts + 2]

            angle = calculate_angle(A, Vertex, B)
            validAngle = angle is not None and angle >= 0

            if validAngle and angleInTolerance(angle):
                return True

        return False



@dataclass(frozen=True)
class LIC10:
    ident: int = 10
    """
    There exists at least one set of three data points separated by exactly E PTS and F PTS con-
    secutive intervening points, respectively, that are the vertices of a triangle with area greater
    than AREA1. The condition is not met when NUMPOINTS < 5.
    1 ≤ E PTS, 1 ≤ F PTS
    E PTS + F PTS ≤ NUMPOINTS − 3
    """

    def evaluate(self, points: PointList, params: Parameters_T) -> bool:
        if len(points) < 5:
            return False

        e_pts = params.e_pts
        f_pts = params.f_pts

        for i in range(len(points) - f_pts - e_pts - 2):
            area = calculate_triangle_area(
                points[i], points[i + e_pts + 1], points[i + e_pts + f_pts + 2]
            )
            if double_compare(area, params.area) == COMPTYPE.GT:
                return True
        return False


@dataclass(frozen=True)
class LIC12:
    ident: int = 12

    """
    Evaluates LIC12: There exists at least one set of two points speaated by exactly K_pts consecuteve intervening points,
    that are a distance greater than LENGTH1 apart. Also there exists at least one set of two data points 
    separated by exactly K_pts consecutive intervening points, that are a distance less than LENGTH2 apart.
    """

    def evaluate(self, points: PointList, params: Parameters_T) -> bool:
        if len(points) < 3:
            return False

        longer_found = False
        shorter_found = False

        for i in range(len(points) - params.k_pts - 1):
            A = points[i]
            B = points[i + params.k_pts + 1]
            dist = calculate_distance(A, B)

            longer_found = longer_found or dist > params.length1
            shorter_found = shorter_found or dist < params.length2

        return longer_found and shorter_found


@dataclass(frozen=True)
class LIC13:
    ident: int = 13
    """
    There exists at least one set of three data points,
    separated by exactly A PTS and B PTS consecutive intervening points, respectively,
    that cannot be contained within or on a circle of radius RADIUS1. In addition,
    there exists at least one set of three data points (which can be the same or
    different from the three data points just mentioned) separated by exactly A PTS
    and B PTS consecutive intervening points, respectively, that can be contained in or
    on a circle of radius RADIUS2. Both parts must be true for the LIC to be true.
    The condition is not met when NUMPOINTS < 5.
    """

    def evaluate(self, points: PointList, params: Parameters_T) -> bool:
        if len(points) < 5:
            return False

        a_pts = params.a_pts
        b_pts = params.b_pts

        max_i = len(points) - (a_pts + b_pts + 3)
        if max_i < 0:
            return False

        found_cannot_radius1 = False
        found_can_radius2 = False

        for i in range(max_i + 1):
            p1 = points[i]
            p2 = points[i + a_pts + 1]
            p3 = points[i + a_pts + b_pts + 2]

            fits_r1 = three_points_fit_in_circle(p1, p2, p3, params.radius1)
            fits_r2 = three_points_fit_in_circle(p1, p2, p3, params.radius2)

            if not fits_r1:
                found_cannot_radius1 = True
            if fits_r2:
                found_can_radius2 = True

            if found_cannot_radius1 and found_can_radius2:
                return True

        return False


@dataclass(frozen=True)
class LIC14:
    ident: int = 14
    """
    There exists at least one set of three data points, separated by exactly E PTS and F PTS con-
    secutive intervening points, respectively, that are the vertices of a triangle with area greater
    than AREA1. In addition, there exist three data points (which can be the same or different
    from the three data points just mentioned) separated by exactly E PTS and F PTS consec-
    utive intervening points, respectively, that are the vertices of a triangle with area less than
    AREA2. Both parts must be true for the LIC to be true. The condition is not met when
    NUMPOINTS < 5.
    0 ≤ AREA2
    """

    def evaluate(self, points: PointList, params: Parameters_T) -> bool:
        if len(points) < 5:
            return False

        e_pts = params.e_pts
        f_pts = params.f_pts
        check_area1 = False
        check_area2 = False

        for i in range(len(points) - f_pts - e_pts - 2):
            area = calculate_triangle_area(
                points[i], points[i + e_pts + 1], points[i + e_pts + f_pts + 2]
            )
            if double_compare(area, params.area) == COMPTYPE.GT:
                check_area1 = True
            if double_compare(area, params.area2) == COMPTYPE.LT:
                check_area2 = True
            if check_area1 and check_area2:
                return True
        return check_area1 and check_area2
