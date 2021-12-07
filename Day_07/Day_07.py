from collections import Counter

data = open("C:/Personal/AdventOfCode2021/Day_07/input.txt").read().split(",")
data = list(map(int, data))

# Puzzle 1
distances = []
for i in range(min(data), max(data)+1):
  distances.append(sum(abs(i-x) for x in data))

print("Solution 1:", min(distances))

 
# Puzzle 2
distances = []
for i in range(min(data), max(data)+1):
    distances.append(sum(sum(range(abs(j-i)+1)) for j in data))

print("Solution 2:", min(distances))