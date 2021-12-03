with open("./input.txt") as reader:
    value_list = reader.readlines()

    increase_count = 0

    for index in range(0, len(value_list) - 1):
        if int(value_list[index]) < int(value_list[index + 1]):
            increase_count += 1

    print(increase_count)
