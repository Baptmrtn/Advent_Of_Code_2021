with open("Day4.txt") as file:
	data = []
	for f in file:
		data.append(f.strip().replace("  "," ").split(" "))

class Grid(): 
	# Grid Object
	def __init__(self,lines):
		# Define the values of the grid
		self.grid = [[int(num) for num in line] for line in lines]

	def show(self):
		for line in self.grid:
			print(line)

	def win(self):
		for index in range(5):
			if sum(self.grid[index]) == -5:
				return True
			elif sum([self.grid[index2][index] for index2 in range(5)]) == -5:
				return True
		return False

	def Mark(self,numberDraw):
		for indexLine,line in enumerate(self.grid):
			for indexCol,value in enumerate(line):
				if value == numberDraw:
					self.grid[indexLine][indexCol] = -1

	def Result_Part_1(self):
		for indexLine,line in enumerate(self.grid):
			for indexCol,value in enumerate(line):
				if value == -1:
					self.grid[indexLine][indexCol] = 0
		return 	sum([sum(line) for line in self.grid])

class Bingo():
	# Bingo Game Object
	def __init__(self,data):
		# Define the grids and the number found
		self.Grids = []
		self.numbers = [int(num) for num in data.pop(0)[0].split(",")]
		for x in range(int(len([x for x in data if len(x) != 1 ])/5)):
			self.Grids.append(Grid([x for x in data if len(x) != 1 ][5*x:5*(x+1)]))
		
	def PlayGame(self):
		# Start the Game
		winner = False
		score = []
		GridNumber = len(self.Grids)
		for indexDraw,draw in enumerate(self.numbers):
			for grid in self.Grids:
				grid.Mark(draw)
				#grid.show()
				"""
				if grid.win() :
					winner = True
					print(f"Part1 result is : {grid.Result_Part_1()*draw}")
				"""
				if grid.win() :
					if grid not in score:
						score.append(grid)
				if len(score) == GridNumber:
					winner = True
					print(f"Part2 result is : {grid.Result_Part_1()*draw}")
					break

			if winner == True:
				break


game = Bingo(data)
game.PlayGame()