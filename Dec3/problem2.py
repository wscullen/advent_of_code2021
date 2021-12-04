from typing import List
import math


def recursive_search(binary_value_list: List[str], digit: int, most: bool) -> List[str]:
    list_length = len(binary_value_list)
    print(list_length)
    if list_length == 1:
        print("list_length is 1")
        return binary_value_list

    one_count = 0
    zero_count = 0
    one_list: List[str] = []
    zero_list: List[str] = []

    for bin_val in binary_value_list:
        if int(bin_val[digit]) == 1:
            one_count += 1
            one_list.append(bin_val.strip())
        else:
            zero_count += 1
            zero_list.append(bin_val.strip())

    if most:
        if one_count >= (list_length / 2):
            return recursive_search(one_list, digit + 1, most)
        else:
            return recursive_search(zero_list, digit + 1, most)
    else:
        if zero_count <= (list_length / 2):
            return recursive_search(zero_list, digit + 1, most)
        else:
            return recursive_search(one_list, digit + 1, most)


with open("./input.txt") as reader:

    binary_value_list = reader.readlines()

    oxygen_gen_value = recursive_search(binary_value_list, 0, True)
    oxygen_gen_decimal = 0
    print(oxygen_gen_value)
    if len(oxygen_gen_value) == 1:
        oxygen_gen_decimal = int(oxygen_gen_value[0], 2)
        print(oxygen_gen_decimal)

    co2_scrubber_value = recursive_search(binary_value_list, 0, False)

    print(co2_scrubber_value)
    co2_scrubber_decimal = 0
    if len(co2_scrubber_value) == 1:
        co2_scrubber_decimal = int(co2_scrubber_value[0], 2)
        print(co2_scrubber_decimal)

    life_support_rating = oxygen_gen_decimal * co2_scrubber_decimal

    print(life_support_rating)
