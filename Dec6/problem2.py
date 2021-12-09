from typing import List, Union, MutableSet, Any

from enum import Enum


class Vector:
    def __init__(self, current_num: int, size: int):
        self.current_num = current_num
        self.size = size

    def __repr__(self):
        return f"({self.current_num}, {self.size})"


with open("./input.txt") as reader:
    line = reader.readline()

    lantern_fish: List[Vector] = [Vector(int(x), 1) for x in line.split(",")]
    count = 1
    total_days = 256
    previous_size = len(lantern_fish)
    previous_growth_rate = 1
    while count <= total_days:
        # print(count)
        new_vector_size = 0

        for vector in lantern_fish:

            if vector.current_num == 0:
                new_vector_size += vector.size
                vector.current_num = 6
            else:
                vector.current_num -= 1

        if new_vector_size > 0:
            new_vector = Vector(8, new_vector_size)
            lantern_fish.append(new_vector)

        count += 1
        # print([vector for vector in lantern_fish])

    print(sum([vector.size for vector in lantern_fish]))
