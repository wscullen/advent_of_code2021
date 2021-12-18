from typing import List, Union, MutableSet
import math

from enum import Enum

with open("./input.txt") as reader:
    line = reader.readline()

    crab_positions: List[int] = [int(x) for x in line.split(",")]
    max_position = max(crab_positions)
    print(crab_positions)
    print(max_position)

    print()
    sums = []
    for index in range(0, max_position):
        current_sum = 0
        for val in crab_positions:
            sub_sum = 0
            for sub_index in range(1, abs(val - index) + 1):
                sub_sum += sub_index
            current_sum += sub_sum

        sums.append(current_sum)

    minimum = min(sums)
    print(minimum)
    print(sums.index(minimum))
