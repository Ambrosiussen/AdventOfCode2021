data = open("C:/AdventOfCode2021/Day_01/input.txt").read()
data_int = [int(x) for x in data.splitlines()]


# Puzzle 1
out = sum([1 for i, x in enumerate(data_int) if x > data_int[max(i-1,0)]])
print(out)


# Puzzle 2
windows = [sum(data_int[i:i+3]) for i in range(len(data_int)-2)]
out = sum([1 for i, x in enumerate(windows) if x > windows[max(i-1,0)]])
print(out)