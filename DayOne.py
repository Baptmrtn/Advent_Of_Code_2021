import numpy as np 


class Ocean():
	def __init__(self,path):
		with open(path) as f:
			file = [int(line.strip()) for line in f]
		self.depth = file

class Sonar(Ocean):
	def __init__(self,path):
		"""
		Initiate path of data and Total Increase.
		"""
		self.Total_Increase = 0
		Ocean.__init__(self,path)

	def DepthChange(lastValue,newValue):
		# Determine if it is an increase or a decrease.
		if lastValue < newValue:
			return True
	############
	#### * #####
	############
	def CalculusDiff(self):
		"""
		Get data from datasource and calculate directly the change in depth. 
		"""
		with open(self.path) as f:
			for measurement in f:
				try:
					if Sonar.DepthChange(lastMeasurement,int(measurement.strip())):
						self.Total_Increase += 1
				except:
					pass 
				lastMeasurement = int(measurement.strip())

		print(f"Total Number of depth increase : {self.Total_Increase}")
	#############
	#### ** #####
	#############

	def SlidingWindowsCalculus(self):
		"""
		Créer une fonction qui calcule les sliding windows automatiquement et n'en garde en mémoire que 2:
		- lastMeasurement = précédente mesure obtenue sur la fenêtre des 3 valeurs
		- newMeasurement = nouvelle valeur obtenue sur la fenêtre des 3 valeurs
		"""
		lastMeasurement = 0
		for index in range(len(self.depth)):
			if len(self.depth[index:index+3]) == 3 and lastMeasurement != 0:
				newMeasurement = sum(self.depth[index:index+3])
				if Sonar.DepthChange(lastMeasurement,newMeasurement):
					self.Total_Increase += 1
					#print(f" {newMeasurement} > {lastMeasurement} ")
				lastMeasurement = newMeasurement
			else:
				lastMeasurement = sum(self.depth[index:index+3])

		print(f"Total Number of depth increase : {self.Total_Increase}")

def main():
	MySonar = Sonar("DayOne.txt") 
	MySonar.SlidingWindowsCalculus()

if __name__ == "__main__":
	main()