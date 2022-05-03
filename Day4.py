with open("test.txt") as file:
	data = []
	for f in file:
		data.append(f.strip().replace("  "," ").split(" "))

class Grid(): 
	def __init__(self,lines):
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
		print(f"No Win for {self}")

class Bingo():
	def __init__(self,data):
		self.Grids = []
		self.numbers = [int(num) for num in data.pop(0)[0].split(",")]
		for x in range(int(len([x for x in data if len(x) != 1 ])/5)):
			self.Grids.append(Grid([x for x in data if len(x) != 1 ][5*x:5*(x+1)]))
		
	def PlayGame(self):
		for draw in self.numbers:
			print(draw)




game = Bingo(data)
print(game.numbers)
game.PlayGame()