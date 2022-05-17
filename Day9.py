

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
					try:
						if currentValue < self.map[indexRow + com[0]][indexCol+ com[1]]:
							checkMin = True
						else: 
							checkMin = False
							break	
					except:
						pass
				if checkMin:
					self.ScorePart1 += currentValue
					self.ScorePart1 += 1
					print(f"{currentValue} at the position {indexRow} | {indexCol}")

PATH = "Day9.txt"

htmap = HeatMap(PATH)
htmap.FindMinimum()
print(htmap.ScorePart1)
"""
import numpy as np

list2d = []

with open(PATH, 'r') as f:
    for line in f.readlines():
        list2d.append(list(line.rstrip('\n')))

array2d = np.array(list2d).astype(np.int32)
# arr_mask = np.full(np.shape(array2d), -1)
max_y, max_x = np.shape(array2d)

total = 0
for y in range(max_y):
    for x in range(max_x):
        debug_value = array2d[y][x]
        count = 0
        if x != 0:
            if array2d[y][x] < array2d[y][x-1]:
                count += 1
        else:
            count += 1
        if x != max_x-1:
            if array2d[y][x] < array2d[y][x+1]:
                count += 1
        else:
            count += 1
        if y != 0:
            if array2d[y][x] < array2d[y-1][x]:
                count += 1
        else:
            count += 1
        if y != max_y-1:
            if array2d[y][x] < array2d[y+1][x]:
                count += 1
        else:
            count += 1
        if count == 4:
            # arr_mask[y][x] = array2d[y][x]
            total += array2d[y][x] + 1

print(total)
"""