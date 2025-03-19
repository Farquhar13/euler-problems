import numpy as np

triangle = []
with open('data_problem_18.txt', 'r') as file:
	line = file.readline()
	while line:
		list_of_ints = [int(x) for x in line.split()]
		triangle.append(list_of_ints)
		line = file.readline()

starting_path = [0] * len(triangle)
paths = [starting_path]
current_path = starting_path.copy()

c = 0
while True:
	for i in reversed(range(0, len(current_path))):
		if i == 0:
			break
		if current_path[i - 1] == current_path[i]:
			current_path[i] += 1
			for j in range(i+1, len(current_path)):
				current_path[j] = current_path[i]
			paths.append(current_path.copy())
			break
	if i == 0:
		break
sums=[]
for path in paths:
	sum=0
	for i,row in enumerate(triangle):
		sum+=row[path[i]]
	sums.append(sum)

print("Sum of max path:", max(sums))
	

