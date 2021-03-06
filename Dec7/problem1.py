from typing import List, Union, MutableSet

from enum import Enum

with open("./input.txt") as reader:
    line = reader.readline()

    crab_positions: List[int] = [int(x) for x in line.split(",")]
    max_position = max(crab_positions)
    print(crab_positions)
    print(max_position)
    sums = []
    for index in range(0, max_position):
        current_sum = 0
        for val in crab_positions:
            current_sum += abs(val - index)

        sums.append(current_sum)

    minimum = min(sums)
    print(minimum)
    print(sums.index(minimum))
