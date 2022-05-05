
with open("test.txt") as file:
	data = []
	for f in file:
		data.append([[int(y) for y in x.split(",")] for x in f.strip().split(" -> ")])


class LineVents():

	def __init__(self):

			self.LineCoordonate = {}


	def Calculus(self,data):

		for line in data:
			if line[0][0] != line[1][0] and line[0][1] != line[1][1]:
				# Select only Horinzontal line for part1
				pass
			else:
				pass
	
	def DrawLine(self,point1,point2):
		pass		





vent = LineVents()
vent.Calculus(data)


