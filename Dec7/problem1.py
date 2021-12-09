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

    print(sums)
    minimum = min(sums)
    print(minimum)
    print(sums.index(minimum))
    # while count <= 18:
    #     lantern_fish_copy = [x for x in crab_positions]

    #     for index in range(0, len(lantern_fish_copy)):
    #         current_fish = lantern_fish[index]

    #         if current_fish == 0:
    #             lantern_fish.append(8)
    #             lantern_fish[index] = 6
    #         else:
    #             lantern_fish[index] -= 1

    #     print(f"After {count + 1} day: {','.join([str(x) for x in lantern_fish])}")
    #     print(len(lantern_fish))
    #     count += 1
