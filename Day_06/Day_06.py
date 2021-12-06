from collections import Counter

data = open("C:/Personal/AdventOfCode2021/Day_06/input.txt").read().split(",")
data = list(map(int, data))

def calculate_num_fish(days):
    fishdata = Counter(data)

    for day in range(0, days):
        next_fishdata = Counter()
        
        for key in fishdata.keys():
            num_fish = fishdata[key]
            if key <= 0:
                next_fishdata[8] = num_fish
                next_fishdata[6] += num_fish  
            else:
                next_fishdata[key-1] += num_fish

        fishdata = next_fishdata

    return sum(fishdata[x] for x in fishdata.keys()) 


# Puzzle 1
print("Solution 1:", calculate_num_fish(80))

# Puzzle 2
print("Solution 2:", calculate_num_fish(256))