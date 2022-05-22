
class GetData():
	def __init__(self,path):
		# Initialise les infos de la maps
		self.path = path
		self.Shape = []
		self.dataInfo = []
		# Liste des aventuriers
		self.Aventuriers = []
		with open(self.path,"r") as file:
			for f in file:
				self.dataInfo.append([x.strip() for x in f.strip().split("-")])


class Aventurier():
	def __init__(self,infos,index):
		#Info de l'aventurier 
		self.Num = index
		self.name = infos[0]
		self.col = int(infos[1])
		self.line = int(infos[2])
		self.orientation = infos[3] 
		self.treasures = 0 
		# créer la liste des mouvement d'un Aventurier
		self.mouvement = [x for x in infos[-1].upper().replace("A","A_").split("_") if x != ""]

	def ShowInfo(self):
		# Print les Infos de l'aventurier 
		print(f" Name : {self.name} - {self.col} - {self.line} - {self.orientation} - {self.treasures} ")

	def Find_New_Orientation(self,tour):
		# Renvoi la nouvelle Orientation de l'aventurier
		sequence = self.mouvement[tour][:-1]
		RoseDesVents = {0 : "N" ,1 : "E", 2 : "S", 3 : "O"}
		sumIndex = 0 
		for action in sequence:
			if action == "D":
				sumIndex += 1
			elif action == "G":
				sumIndex -= 1
			else:
				pass
		# Calcul le score actuelle sur notre rose des vents 
		scoreOnRDV = [x for x in range(4) if RoseDesVents[x] == self.orientation][0]
		# Défini la rose des vents comme la somme de l'ancien score + du nouveau modulo 4
		# Modulo permet de faire une boucle infini sur : 0,1,2,3
		self.orientation = RoseDesVents[(scoreOnRDV + sumIndex)%4]


	def ProgressCheck(self,tour):
		# Renvoi le changement de ligne à faire en fonction de l'orientation actuel de l'aventurier
		if self.orientation == "N":
			return (self.col,self.line-1)
		elif self.orientation == "S":
			return (self.col,self.line+1)
		elif self.orientation == "E":
			return (self.col+1,self.line)
		else:
			return (self.col-1,self.line)

class Game(GetData):
	def CreateMap(self):
		# Define Map Dimension First with "C" argument
		for line in self.dataInfo:
			#line = 
			if line[0] == "C":
				self.Shape = [["." for y in range(int(line[1]))] for x in range(int(line[2]))]
				break
					
	def Define_Map_Object(self):
		# Define other Objects of the map
		for line in self.dataInfo:
			# Define Montagne localisation
			if line[0] == "M":
				self.Shape[int(line[2])][int(line[1])] = "M"
			# Define treasure localisation
			elif line[0] == "T":
				self.Shape[int(line[2])][int(line[1])] = f"T{line[3]}"
			else:
				pass

	def MapUpdate(self,aventurier,tour):
		# Permet de modifier les valeurs de la map avec les valeurs actuelles
		mouvementCheck = aventurier.ProgressCheck(tour)
		print(f" - Aventurier {aventurier.name} is in {aventurier.col,aventurier.line} want to go {mouvementCheck} -")
		# Si aventurier veut aller plus loin que la map : pass
		if mouvementCheck[0] < 0 or mouvementCheck[1] < 0 or mouvementCheck[1] > len(self.Shape)-1 or mouvementCheck[0] > len(self.Shape[0])-1:
			print("Le joueur ne peut pas avancer car il est aux limites de la map")
		# Si mountain : pass
		elif self.Shape[mouvementCheck[1]][mouvementCheck[0]] == "M":
			print("Moutain Here")
		# Si aventurier : pass
		elif self.Shape[mouvementCheck[1]][mouvementCheck[0]][0] == "A":
			print("Aventurier Here")
		# Sinon update la map 
		else:
			# change la localisation actuelle de l'aventurier
			self.Shape[aventurier.line][aventurier.col] = '.'
			# Collect le Trésor s'il y a 
			if "T" in self.Shape[mouvementCheck[1]][mouvementCheck[0]] :
				aventurier.treasures += int(self.Shape[mouvementCheck[1]][mouvementCheck[0]][1:])
			# Ajoute la nouvelle position 
			self.Shape[mouvementCheck[1]][mouvementCheck[0]] = f"A{aventurier.Num}"
			aventurier.col = mouvementCheck[0]
			aventurier.line = mouvementCheck[1]


	def Start_Game(self):
		index = 0
		# Ajoute les aventuriers à la liste + sur la map
		for info in self.dataInfo:
			if info[0] == "A":
				index += 1
				self.Aventuriers.append(Aventurier(info[1:],index))
		for aventurier in self.Aventuriers:
			self.Shape[aventurier.line][aventurier.col] = f"A{aventurier.Num}"


		print(f"MapSize : {len(self.Shape[0])} | {len(self.Shape)}")
		#Nombre max de tour
		maxIter = max([len(aventurier.mouvement) for aventurier in self.Aventuriers])
		for tour in range(maxIter):
			print(f"||||| Tour {tour} |||||\n")
			for aventurier in self.Aventuriers:
				validate = False
				try:# Voir s'il lui reste des mouvements
					aventurier.mouvement[tour]
					validate = True
				except:
					validate = False

				if validate:
					print(f"--- Aventurier {aventurier.name} play ------")
					print("######################")
					print(f"Sequence : {aventurier.mouvement[tour]}")
					print(f"Current orientation {aventurier.orientation}")
					if aventurier.mouvement[tour] != "A":
						aventurier.Find_New_Orientation(tour)
						print(f"Nouvelle orientation {aventurier.orientation}")
					print("######################")
					self.MapUpdate(aventurier,tour)

					for x in self.Shape:
						print(x)
		print("#########\nFINAL : \n#########")
		for aventurier in self.Aventuriers:
			aventurier.ShowInfo()
		print()
		for x in self.Shape:
			print(x)

path = "test.txt"
test = Game(path)
test.CreateMap()
test.Define_Map_Object()
test.Start_Game()




