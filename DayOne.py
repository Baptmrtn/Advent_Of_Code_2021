import numpy as np 


class Sonar():
	def __init__(self,path):
		"""
		Initiate path of data and Total Increase
		"""
		self.Total_Increase = 0
		self.path = path

	def DepthChange(lastValue,newValue):
		# Determine if it is an increase or a decrease 
		if lastValue < newValue:
			return True

	def CalculusDiff(self):
		"""
		Get data from 
		"""
		with open(self.path) as f:
			for measurement in f:
				try:
					if Sonar.DepthChange(lastMeasurement,int(measurement.strip())):#lastMeasurement < int(measurement.strip()):
						self.Total_Increase += 1
				except:
					pass 
				lastMeasurement = int(measurement.strip())

		print(f"Total Number of depth increase : {self.Total_Increase}")


def main():
	MySonar = Sonar("DayOne.txt") 
	MySonar.CalculusDiff()

if __name__ == "__main__":
	main()