import numpy as np 

numbers = [x.strip() for x in open('Day3.txt', 'r').readlines()]

def BinaryConvert(bit,index,rangeX):
	return bit*2**(rangeX -1 - index)

GammaRate = 0
Epsilonrate = 0

for index in range(len(numbers[0])):
	if sum([1 for x in numbers if x[index] == "1"])/len(numbers) > 0.5:
		GammaRate += BinaryConvert(1,index,len(numbers[0]))
		Epsilonrate += BinaryConvert(0,index,len(numbers[0]))
	else:
		GammaRate += BinaryConvert(0,index,len(numbers[0]))
		Epsilonrate += BinaryConvert(1,index,len(numbers[0]))

print(GammaRate*Epsilonrate)