with open("Day6.txt") as file:
	for f in file:
		fishs = [int(x) for x in f.split(",")]

Fish = {}
for internalTime in range(9):
	Fish[internalTime] = 0

for Onefish in fishs:
	Fish[Onefish] += 1 

for day in range(256):
	for internalDay in Fish.keys():
		if internalDay == 0:
			newBorn = Fish[internalDay]
		else:
			Fish[internalDay-1] = Fish[internalDay]
	Fish[8] = newBorn
	Fish[6] += newBorn

count = 0
for key in Fish.keys():
	count += Fish[key]

print(f" 2nd * answer : {count}")