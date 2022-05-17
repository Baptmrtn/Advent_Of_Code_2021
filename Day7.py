with open("Day7.txt") as file:
	for f in file:
		data =  [int(x) for x in f.split(",")]

def SumFunc(n):
	return n*0.5 + (n/2-1)*n + n

minfuel = 100000000000000000000
for index in range(min(data),max(data)+1):
	if sum([SumFunc(abs(index-x)) for x in data]) < minfuel:
		minfuel = sum([SumFunc(abs(index-x)) for x in data])

print(minfuel)



