
numbers = [x.strip().split(" ") for x in open('Day2.txt', 'r').readlines()]
############
#### * #####
############
position = sum([int(x[1]) if x[0] == "forward" else 0 for x in numbers])
depth_decrease = sum([int(x[1]) if x[0] == "up" else 0 for x in numbers])
depth_increase = sum([int(x[1]) if x[0] == "down" else 0 for x in numbers])
print(f'The solution for the first * is : {position*(depth_increase-depth_decrease)}')

##############
##### ** #####
##############

aim = 0 
depth = 0 
position = 0 

for x in numbers:
	if x[0] == "forward":
		position += int(x[1])
		depth += aim*int(x[1])
	elif x[0] == "up":
		aim -= int(x[1])
	else:
		aim += int(x[1])
print(f'The solution for the second * is : {position*depth}')