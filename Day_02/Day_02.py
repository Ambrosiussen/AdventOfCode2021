data = open("C:/AdventOfCode2021/Day_02/input.txt").read().splitlines()

# Puzzle 1
position = [0,0]

for entry in data:
    direction, amount = entry.split(" ")
    amount = int(amount)

    if direction == "up":
            position[1] -= amount
    elif direction == "down":
            position[1] += amount
    elif direction == "forward":
            position[0] += amount 

print("Puzzle 1", position[0] * position[1])


# Puzzle 2
position = [0,0]
aim = 0

for entry in data:
    direction, amount = entry.split(" ")
    amount = int(amount)

    if direction == "up":
    		aim -= amount
    elif direction == "down":
    		aim += amount
    elif direction == "forward":
            position[0] += amount
            position[1] += amount * aim

print("Puzzle 2", position[0] * position[1])