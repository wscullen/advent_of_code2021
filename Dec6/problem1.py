from typing import List, Union, MutableSet

from enum import Enum

with open("./testinput.txt") as reader:
    line = reader.readline()

    lantern_fish: List[int] = [int(x) for x in line.split(",")]

    print(lantern_fish)
    count = 0
    while count <= 18:
        lantern_fish_copy = [x for x in lantern_fish]

        for index in range(0, len(lantern_fish_copy)):
            current_fish = lantern_fish[index]

            if current_fish == 0:
                lantern_fish.append(8)
                lantern_fish[index] = 6
            else:
                lantern_fish[index] -= 1

        print(f"After {count + 1} day: {','.join([str(x) for x in lantern_fish])}")
        print(len(lantern_fish))
        count += 1
