with open("test.txt","r") as file:
	data = []
	for f in file:
		data.append(f.strip())

CaractScore = {")":3,"]": 57,"}": 1197,">": 25137}

for lines in data:
	print(lines)
	for index,caracter in enumerate(lines):
		if caracter == ")":
			counter = lines[:index+1].count(")")
			counterClose = lines[:index+1].count("(")
		elif caracter == "]":
			counter = lines[:index+1].count("]")
			counterClose = lines[:index+1].count("[")
		elif caracter == "}":
			counter = lines[:index+1].count("}")
			counterClose = lines[:index+1].count("{")
		elif caracter == ">":
			counter = lines[:index+1].count(">")
			counterClose = lines[:index+1].count("<")	
		else:
			counter = 0 
			counterClose = 1

		if counter > counterClose:
			print(f" line {lines} prob on caracter : {caracter}")

print("oui")