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

    def line_orientation(self) -> LineType:
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

        if self.line_orientation() == LineType.HORIZONTAL:
            for value in range(min_x, max_x + 1):
                new_point = Point(value, min_y)
                points.append(new_point)
        elif self.line_orientation() == LineType.VERTICAL:
            for value in range(min_y, max_y + 1):
                new_point = Point(min_x, value)
                points.append(new_point)
        elif self.line_orientation() == LineType.DIAGONAL:
            start = None
            end = None
            if self.start.x < self.end.x:
                start = self.start
                end = self.end
            else:
                start = self.end
                end = self.start

            if start.y < end.y:
                for value in range(1, end.x + 1):
                    new_point = Point(start.x + value, start.y + value)
                    points.append(new_point)
            else:
                for value in range(1, end.x + 1):
                    new_point = Point(start.x - value, start.y - value)
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


with open("./input.txt") as reader:
    horizontal_lines = []
    vertical_lines = []
    line = reader.readline()
    all_lines: List[Line] = []

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

        all_lines.append(line_segment)

        line = reader.readline()

        total_line_count += 1

    print("total lines", total_line_count)

    intersection_points: MutableSet[Point] = set()

    for index, line in enumerate(all_lines):
        for index2, line2 in enumerate(all_lines):
            if index == index2:
                continue

            line_list = line.draw_line()
            line2_list = line2.draw_line()

            line2_set = set(line_list)
            line_set = set(line2_list)
            intersect = line2_set.intersection(line_set)
            intersection_points.update(intersect)

    print(len(intersection_points))
