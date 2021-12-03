with open("./input.txt") as reader:
    direction_list = reader.readlines()

    depth = 0
    horizontal = 0

    for direction in direction_list:
        direction_split = direction.split(" ")
        instruction = direction_split[0]
        value = int(direction_split[1])

        if instruction == "up":
            depth -= value
        elif instruction == "down":
            depth += value
        elif instruction == "forward":
            horizontal += value

    print(depth * horizontal)
