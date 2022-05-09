with open("Day7.txt") as file:
	for f in file:
		data =  [int(x) for x in f.split(",")]
		#data.append([[int(y) for y in x.split(",")] for x in f.strip().split(" -> ")])

def SumFunc(n):
	return n*0.5 + (n/2-1)*n + n

minfuel = 100000000000000000000
for index in range(min(data),max(data)+1):
	if sum([SumFunc(abs(index-x)) for x in data]) < minfuel:
		#print(f"for index {index} : {[SumFunc(abs(index-x)) for x in data]}")
		minfuel = sum([SumFunc(abs(index-x)) for x in data])

print(minfuel)

print(SumFunc(11))

print(1+2+3+4+5+6+7+8+9+10+11)