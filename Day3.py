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


OxygenSelection = [x for x in numbers].copy()
CO2ScrubberSelection = [x for x in numbers].copy()
indexOxy = 0
indexCO2 = 0

while len(OxygenSelection) > 1 or len(CO2ScrubberSelection) > 1:
	ratioOxy = sum([1 for x in OxygenSelection if x[indexOxy] == "1"])/len(OxygenSelection)
	ratioCO2 = sum([1 for x in CO2ScrubberSelection if x[indexCO2] == "1"])/len(CO2ScrubberSelection)
	if len(OxygenSelection) > 1:
		if ratioOxy >= 0.5:
			OxygenSelection = [x for x in OxygenSelection if x[indexOxy] == "1"]
			indexOxy += 1
		else: 
			OxygenSelection = [x for x in OxygenSelection if x[indexOxy] == "0"]
			indexOxy += 1
	if len(CO2ScrubberSelection) > 1:
		if ratioCO2 >= 0.5:
			CO2ScrubberSelection = [x for x in CO2ScrubberSelection if x[indexCO2] == "0"]
			indexCO2 += 1 
		else: 
			CO2ScrubberSelection = [x for x in CO2ScrubberSelection if x[indexCO2] == "1"]
			indexCO2 += 1

OxygenSelection = OxygenSelection[0]
CO2ScrubberSelection = CO2ScrubberSelection[0]

oxygenGeneratorRating = 0
CO2ScrubberRating = 0
for index in range(len(OxygenSelection)):
	oxygenGeneratorRating += BinaryConvert(int(OxygenSelection[index]),index,len(OxygenSelection))
	CO2ScrubberRating += BinaryConvert(int(CO2ScrubberSelection[index]),index,len(OxygenSelection))

print(oxygenGeneratorRating*CO2ScrubberRating)

#
"""
while len(OxygenSelection) > 1:
	ratio = sum([1 for x in OxygenSelection if x[index] == "1"])/len(OxygenSelection)
	if ratio >= 0.5:
		OxygenSelection = [x for x in OxygenSelection if x[index] == "1"]
	else: 
		OxygenSelection = [x for x in OxygenSelection if x[index] == "0"]
	print(OxygenSelection)
	index += 1


print(CO2ScrubberSelection)

index = 0
while len(CO2ScrubberSelection) > 1:
	ratio = sum([1 for x in CO2ScrubberSelection if x[index] == "1"])/len(CO2ScrubberSelection)
	if ratio >= 0.5:
		CO2ScrubberSelection = [x for x in CO2ScrubberSelection if x[index] == "0"]
	else: 
		CO2ScrubberSelection = [x for x in CO2ScrubberSelection if x[index] == "1"]
	print(CO2ScrubberSelection)
	index += 1
"""