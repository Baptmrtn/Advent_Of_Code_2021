class HeatMap():
	def __init__(self,path):	
		with open(path,"r") as file:
			self.map = []
			for f in file:
				self.map.append([[int(y) for y in x][0] for x in f.strip()])

		self.ScorePart1 = 0
		self.bassins = []
		self.ScorePart2 = []

	def FindMinimum(self):
		for indexRow,row in enumerate(self.map):
			for indexCol,col in enumerate(row):
				currentValue = self.map[indexRow][indexCol]
				checkMin = False
				for com in ((0,1),(0,-1),(1,0),(-1,0)):
					if indexRow + com[0] < 0 or indexCol+ com[1] < 0 :
						pass
					else:
						try:
							if currentValue < self.map[indexRow + com[0]][indexCol+ com[1]]:
								checkMin = True
							else: 
								checkMin = False
								break	
						except:
							pass
				if checkMin:
					print(f"###########\n New One on {indexRow,indexCol} \n###########")
					self.ScorePart1 += currentValue + 1
					bassinsCount = 0
					result = self.RecursiveCheck(bassinsCount,indexRow,indexCol)
					print(f"|||||||||||\n RESULT IS : {len(self.bassins)}\n|||||||||||")
					self.ScorePart2.append(len(self.bassins))
					self.bassins = []

	def RecursiveCheck(self,Count,RowPoint,ColPoint):
		print("New recursive")
		if RowPoint < 0 or ColPoint < 0 or RowPoint> len(self.map)-1 or ColPoint > len(self.map[0])-1:
			pass
		else:
			print(RowPoint,ColPoint)
			if self.map[RowPoint][ColPoint] == 9:
				pass
			elif [RowPoint,ColPoint] in self.bassins:
				pass
			else:
				self.bassins.append([RowPoint,ColPoint])
				self.RecursiveCheck(Count,RowPoint+1,ColPoint)
				self.RecursiveCheck(Count,RowPoint-1,ColPoint)
				self.RecursiveCheck(Count,RowPoint,ColPoint+1)
				self.RecursiveCheck(Count,RowPoint,ColPoint-1)
				print(self.bassins)


PATH = "test.txt"

htmap = HeatMap(PATH)
htmap.FindMinimum()
print(htmap.ScorePart1)
print(htmap.bassins)
print(htmap.ScorePart2)

liste = htmap.ScorePart2.copy()

Part2ScoreFinal = 0
for x in range(3):
	
	print(liste.pop(max(liste)))