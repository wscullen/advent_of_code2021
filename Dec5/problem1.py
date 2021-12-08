from typing import List, Union, MutableSet

from enum import Enum


class LineType(Enum):
    HORIZONTAL = 1
    VERTICAL = 2
    DIAGONAL = 3


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __ne__(self, other):
        if self.x != other.x or self.y != other.y:
            return True
        return False

    def __hash__(self):
        return int(str(self.x) + str(self.y))

    def __str__(self):
        return f"({self.x},{self.y})"

    def __repr__(self):
        return f"({self.x},{self.y})"


class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def vertical_or_horiztonal(self) -> LineType:
        if self.start.x == self.end.x:
            return LineType.VERTICAL
        elif self.start.y == self.end.y:
            return LineType.HORIZONTAL
        else:
            return LineType.DIAGONAL

    def draw_line(self) -> List[Point]:
        min_x = min(self.start.x, self.end.x)
        max_x = max(self.start.x, self.end.x)

        min_y = min(self.start.y, self.end.y)
        max_y = max(self.start.y, self.end.y)
        points = []

        if self.vertical_or_horiztonal() == LineType.HORIZONTAL:
            for value in range(min_x, max_x + 1):
                new_point = Point(value, min_y)
                points.append(new_point)
        elif self.vertical_or_horiztonal() == LineType.VERTICAL:
            for value in range(min_y, max_y + 1):
                new_point = Point(min_x, value)
                points.append(new_point)

        return points

    def __str__(self):
        return f"({self.start.x},{self.start.y}) -> ({self.end.x},{self.end.y})"

    def __repr__(self):
        return f"({self.start.x},{self.start.y}) -> ({self.end.x},{self.end.y})"


def find_intersect_perpendicular_lines(line1: Line, line2: Line) -> Union[Point, None]:
    if (
        line1.vertical_or_horiztonal() == LineType.HORIZONTAL
        and line2.vertical_or_horiztonal() == LineType.HORIZONTAL
    ):
        raise Exception(
            "Lines are both horizontal, this function is for perpendicular lines"
        )
    elif (
        line1.vertical_or_horiztonal() == LineType.VERTICAL
        and line2.vertical_or_horiztonal() == LineType.VERTICAL
    ):
        raise Exception(
            "Lines are both vertical, this function is for perpendicular lines"
        )
    elif (
        line1.vertical_or_horiztonal() == LineType.DIAGONAL
        or line2.vertical_or_horiztonal() == LineType.DIAGONAL
    ):
        raise Exception(
            "Lines are diagonal, this function is for perpendicular horizontal and vertical lines"
        )

    vertical_line = None
    horizontal_line = None

    if line1.vertical_or_horiztonal() == LineType.VERTICAL:
        vertical_line = line1
        horizontal_line = line2
    else:
        vertical_line = line2
        horizontal_line = line1

    vert_x = vertical_line.start.x
    hor_x_min = min(horizontal_line.start.x, horizontal_line.end.x)
    hor_x_max = max(horizontal_line.start.x, horizontal_line.end.x)

    hor_y = horizontal_line.start.y
    vert_y_min = min(vertical_line.start.y, vertical_line.end.y)
    vert_y_max = max(vertical_line.start.y, vertical_line.end.y)

    if (vert_x >= hor_x_min and vert_x <= hor_x_max) and (
        hor_y >= vert_y_min and hor_y <= vert_y_max
    ):
        intersect_point = Point(vert_x, hor_y)
        return intersect_point

    return None


def find_intersect_parallel_lines(line1: Line, line2: Line) -> Union[List[Point], None]:
    if (
        line1.vertical_or_horiztonal() == LineType.HORIZONTAL
        and line2.vertical_or_horiztonal() == LineType.VERTICAL
    ):
        raise Exception("Lines are perpendicular, this function is for parallel lines")
    elif (
        line1.vertical_or_horiztonal() == LineType.VERTICAL
        and line2.vertical_or_horiztonal() == LineType.HORIZONTAL
    ):
        raise Exception("Lines are perpendicular, this function is for parallel lines")
    elif (
        line1.vertical_or_horiztonal() == LineType.DIAGONAL
        or line2.vertical_or_horiztonal() == LineType.DIAGONAL
    ):
        raise Exception(
            "Lines are diagonal, this function is for parallel horizontal and vertical lines"
        )

    if line1.start.y == line2.start.y or line1.start.x == line2.start.x:

        print(line1)
        print(line2)

        line1_min = min(line1.start.x, line1.end.x)
        line2_min = min(line2.start.x, line2.end.x)

        line1_max = max(line1.start.x, line1.end.x)
        line2_max = max(line2.start.x, line2.end.x)

        print(line1_min, line1_max)
        print(line2_min, line2_max)

        if (line1_min >= line2_min and line1_min <= line2_max) and (
            line1_max >= line2_min and line1_max <= line2_max
        ):
            print("line 1 start and end are contained within line 2")
            overlap = abs(line1.start.x - line1.end.x)
            print(overlap)
            coord_list = []
            for coord in range(0, overlap + 1):
                coord_list.append(Point(coord + line1_min, line1.start.y))
            return coord_list
        elif line1_min >= line2_min and line1_min <= line2_max:
            print("line 1 start is contained within line 2")
            overlap = abs(line1_min - min(line1_max, line2_max))
            print(overlap)
            coord_list = []
            for coord in range(0, overlap + 1):
                coord_list.append(Point(coord + line1_min, line1.start.y))
            return coord_list
        elif line1_max >= line2_max and line1_max <= line2_max:
            print("line 1 end is contained within line 2")
            overlap = abs(line1_max - max(line1_min, line2_min))
            print(overlap)
            coord_list = []
            for coord in range(0, overlap + 1):
                coord_list.append(Point(coord + line1_min, line1.start.y))
            return coord_list


with open("./input.txt") as reader:
    horizontal_lines = []
    vertical_lines = []
    line = reader.readline()
    horizontal_lines: List[Line] = []
    vertical_lines: List[Line] = []

    total_line_count = 0

    while line:
        print(line)
        line_parts = line.split("->")
        print(line_parts)
        start = line_parts[0].split(",")
        end = line_parts[1].split(",")
        start_point = Point(int(start[0].strip()), int(start[1].strip()))
        end_point = Point(int(end[0].strip()), int(end[1].strip()))

        line_segment = Line(start_point, end_point)

        if line_segment.vertical_or_horiztonal() == LineType.VERTICAL:
            vertical_lines.append(line_segment)
        elif line_segment.vertical_or_horiztonal() == LineType.HORIZONTAL:
            horizontal_lines.append(line_segment)

        line = reader.readline()

        total_line_count += 1

    print("horizontal lines count", len(horizontal_lines))
    print("vertical lines count", len(vertical_lines))
    print("total lines", total_line_count)

    intersection_points: MutableSet[Point] = set()
    # intersection_result = find_intersect_parallel_lines(
    #     vertical_lines[0], vertical_lines[1]
    # )
    # print(intersection_result)

    # point1 = Point(9, 4)

    # point2 = Point(3, 4)
    # point1 = Point(0, 9)

    # point2 = Point(5, 9)

    # line1 = Line(point1, point2)

    # # point1 = Point(3, 4)
    # # point2 = Point(1, 4)

    # point1 = Point(0, 9)

    # point2 = Point(2, 9)

    # line2 = Line(point1, point2)

    # intersect_results = find_intersect_parallel_lines(line1, line2)
    # print(intersect_results)
    # intersection_points.add(point1)
    # intersection_points.add(point2)

    # print(intersection_points)

    for hor_line in horizontal_lines:
        for vert_line in vertical_lines:
            vert_line_list = vert_line.draw_line()
            hor_line_list = hor_line.draw_line()
            vert_line_set = set(vert_line_list)
            hor_line_set = set(hor_line_list)
            intersect = vert_line_set.intersection(hor_line_set)
            intersection_points.update(intersect)

    for index, hor_line in enumerate(horizontal_lines):
        for index2, hor_line2 in enumerate(horizontal_lines):
            if index == index2:
                continue

            hor_line_list = hor_line.draw_line()
            hor_line2_list = hor_line2.draw_line()

            hor_line2_set = set(hor_line2_list)
            hor_line_set = set(hor_line_list)
            intersect = hor_line2_set.intersection(hor_line_set)
            intersection_points.update(intersect)

    for index, vert_line in enumerate(vertical_lines):
        for index2, vert_line2 in enumerate(vertical_lines):
            if index == index2:
                continue

            vert_line_list = vert_line.draw_line()
            vert_line2_list = vert_line2.draw_line()

            vert_line2_set = set(vert_line2_list)
            vert_line_set = set(vert_line_list)
            intersect = vert_line2_set.intersection(vert_line_set)
            intersection_points.update(intersect)

    print(len(intersection_points))
