with open("Day10.txt","r") as file:
	data = []
	for f in file:
		data.append(f.strip())

CaractScore = {")":3,"]": 57,"}": 1197,">": 25137}

def RemovePatern(message):
	paternsList = ["[]","()","{}","<>"]
	for patern in paternsList:
		for index,car in enumerate(message):
			try:
				if message[index] == patern[0] and message[index+1] == patern[1]:
					message = message[0:index] + message[index+2:]
					message = RemovePatern(message)
			except:
				pass

	return message

def FindScore(messageClear):
	points = 0
	breakTrue = False
	for car in messageClear:
		for patern in CaractScore.keys():
			if car == patern:
				breakTrue = True 
				points = CaractScore[patern]
			else:
				pass
		if breakTrue:
			break

	return points

def IncompletesLines(messageIncomplete):
	paternsList = {"[":2,"(":1,"{":3,"<":4}
	score = 0
	for x in messageIncomplete[::-1]:
		score = score*5 + paternsList[x]
	return score 		


Score1 = 0
Score2 = []

for line in data:
	newMessage = RemovePatern(line)
	if FindScore(newMessage) > 0:
		Score1 += FindScore(newMessage)
	else:
		Score2.append(IncompletesLines(newMessage))

print(Score1)
index =(len(Score2)-1)/2
print(sorted(Score2)[int(index)])