from collections import Counter

data = open("C:/AdventOfCode2021/Day_03/input.txt").read().splitlines()

# Puzzle 1
data_split = [list(x) for x in data]
zipped_list = list(zip(*data_split))
counts_dominant = [int(max(x, key=Counter(x).get)) for x in zipped_list]

gamma = ""
epsilon = ""

for x in counts_dominant:
	if x == 0:
		gamma += "0"
		epsilon += "1"
	else:
		gamma += "1"
		epsilon += "0"

print("Solution 1:", int(gamma, 2) * int(epsilon, 2))



# Puzzle 2
data_left_dominant = data
data_left_inverse = data

def find_dominant(data, idx):
	data_split = [x[idx] for x in data]
	counts = Counter(data_split)

	if counts["1"] == counts["0"]:
		return "1"
	else:
		return max(data_split, key=Counter(data_split).get)

for idx in range(len(data[0])):
	if len(data_left_dominant) > 1:
		dominant = find_dominant(data_left_dominant, idx)		
		data_left_dominant = [x for x in data_left_dominant if x[idx] == dominant]

	if len(data_left_inverse) > 1:
		inverse = find_dominant(data_left_inverse, idx)	
		data_left_inverse = [x for x in data_left_inverse if x[idx] != inverse] 
		
print("Solution 2:", int(data_left_dominant[0], 2) * int(data_left_inverse[0], 2))