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
                for value in range(0, abs(end.x - start.x) + 1):
                    new_point = Point(start.x + value, start.y + value)
                    points.append(new_point)
            else:
                for value in range(0, abs(end.x - start.x) + 1):
                    new_point = Point(start.x + value, start.y - value)
                    points.append(new_point)

        return points

    def __str__(self):
        return f"({self.start.x},{self.start.y}) -> ({self.end.x},{self.end.y})"

    def __repr__(self):
        return f"({self.start.x},{self.start.y}) -> ({self.end.x},{self.end.y})"


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
        print(start)
        print(end)
        start_point = Point(int(start[0].strip()), int(start[1].strip()))
        end_point = Point(int(end[0].strip()), int(end[1].strip()))

        line_segment = Line(start_point, end_point)
        if line_segment.line_orientation() in [
            LineType.VERTICAL,
            LineType.HORIZONTAL,
            LineType.DIAGONAL,
        ]:
            all_lines.append(line_segment)

        line = reader.readline()

        total_line_count += 1

    print("total lines", total_line_count)

    intersection_points: MutableSet[Point] = set()

    total_line_comparison = 0
    coords = {}
    intersect_coords = []
    for index, line in enumerate(all_lines):
        points = line.draw_line()
        for point in points:
            if point in coords.keys():
                coords[point] += 1
                if point not in intersect_coords:
                    intersect_coords.append(point)
            else:
                coords[point] = 1

    print(len(coords.keys()))
    print(len(intersect_coords))

    for index in range(0, 50):
        for index2 in range(0, 50):
            point = Point(index2, index)
            if point in coords.keys():
                print(f" {coords[point]} ", end="")
            else:
                print(" . ", end="")

        print("\n")
