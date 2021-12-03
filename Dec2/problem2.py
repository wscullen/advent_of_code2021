with open("./input.txt") as reader:
    direction_list = reader.readlines()

    aim = 0
    horizontal = 0
    depth = 0

    for direction in direction_list:
        direction_split = direction.split(" ")
        instruction = direction_split[0]
        value = int(direction_split[1])

        if instruction == "up":
            aim -= value
        elif instruction == "down":
            aim += value
        elif instruction == "forward":
            horizontal += value
            depth += aim * value

    print(depth * horizontal)
