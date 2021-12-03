with open("./input.txt") as reader:
    value_list = reader.readlines()

    increase_count = 0

    window_size = 3

    for index in range(0, len(value_list) - 3):
        if index < 20 or index > len(value_list) - 20:
            print(index)
            print(int(value_list[index]))
            print(int(value_list[index + 1]))
            print(int(value_list[index + 2]))
            print(int(value_list[index + 3]))

        current_window_sum = (
            int(value_list[index])
            + int(value_list[index + 1])
            + int(value_list[index + 2])
        )
        next_window_sum = (
            int(value_list[index + 1])
            + int(value_list[index + 2])
            + int(value_list[index + 3])
        )
        if current_window_sum < next_window_sum:
            increase_count += 1

    print(increase_count)
