
with open("Day5.txt") as file:
	data = []
	for f in file:
		data.append([[int(y) for y in x.split(",")] for x in f.strip().split(" -> ")])


class LineVents():

	def __init__(self):
		self.LineCoordonate = {}
	
	def ADDPoint(self,x,y):
		if f"{x},{y}" in self.LineCoordonate : 
			self.LineCoordonate[f"{x},{y}"] += 1
		else:
			self.LineCoordonate[f"{x},{y}"] = 1		

	def FlatLine(self,Coord,vertical):
		if vertical:
			for y in range(min(Coord[0][1],Coord[1][1]),max(Coord[0][1],Coord[1][1])+1): 
				self.ADDPoint(Coord[0][0],y)
		else:
			for x in range(min(Coord[0][0],Coord[1][0]),max(Coord[0][0],Coord[1][0])+1): 
				self.ADDPoint(x,Coord[0][1])

	def NoFlatLine(self,Coord):
		if Coord[0][0] > Coord[1][0]:
			range1 = range(Coord[0][0],Coord[1][0]-1,-1)
		else:
			range1 = range(Coord[0][0],Coord[1][0]+1)
		if Coord[0][1] > Coord[1][1]:
			range2 = range(Coord[0][1],Coord[1][1]-1,-1)
		else:
			range2 = range(Coord[0][1],Coord[1][1]+1)

		for x,y in zip(range1,range2):
			self.ADDPoint(x,y)

	def Calculus(self,data):
		for line in data:
			if line[0][0] == line[1][0]:
				# Select only vertical line for part1
				self.FlatLine(line,True)
			elif line[0][1] == line[1][1]:
				# Select only horizontal line for part1
				self.FlatLine(line,False)
			else:
				self.NoFlatLine(line)

vent = LineVents()
vent.Calculus(data)
print("------------")
count = 0
for point in vent.LineCoordonate.keys():
	if vent.LineCoordonate[point] >= 2 :
		count += 1 

print(f"2st * answer : {count}")