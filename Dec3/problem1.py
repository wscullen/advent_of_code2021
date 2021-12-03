with open("./input.txt") as reader:

    binary_value_list = reader.readlines()
    count_list = [0] * len(binary_value_list[0].strip())
    print(count_list)

    for binary_value in binary_value_list:

        for index, digit in enumerate(binary_value.strip()):
            count_list[index] += int(digit)
            # if (int(digit))

    print(count_list)
    list_length = len(binary_value_list)
    gamma = int("".join(["1" if x > list_length / 2 else "0" for x in count_list]), 2)
    epsilon = int("".join(["0" if x > list_length / 2 else "1" for x in count_list]), 2)

    print(gamma)
    print(epsilon)

    power_consumption = gamma * epsilon
    print(power_consumption)
