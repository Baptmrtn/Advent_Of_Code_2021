

class HeatMap():
	def __init__(self,path):	
		with open(path,"r") as file:
			self.map = []
			for f in file:
				self.map.append([[int(y) for y in x][0] for x in f.strip()])

		self.ScorePart1 = 0

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
					self.ScorePart1 += currentValue + 1

PATH = "Day9.txt"

htmap = HeatMap(PATH)
htmap.FindMinimum()
print(htmap.ScorePart1)