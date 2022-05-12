
with open("test.txt","r") as file:
	data = []
	for f in file:
		data.append([x.split(" ") for x in f.strip().split(" | ")])
"""
count = 0
for index in data:
	for number in index[1]:
		if len(number) == 3 or len(number) == 2 or len(number) == 7 or len(number) == 4:
			count += 1
print(f"Solution of the part 1 is {count}")

"""



DicoNumberLetter = {"0":["a","b","c","e","f","g"],
"1":["c","f"],
"2":["a","c","d","e","g"],
"3":["a","c","d","f","g"],
"4":["b","c","d","f"],
"5":["a","b","d","f","g"],
"6":["a","b","d","e","f","g"],
"7":["a","c","f"],
"8":["a","b","c","d","e","f","g"],
"9":["a","b","c","d","f","g"]}

def FlowLookUp(data):
	DicoGuessNumber = {"0":"","1":"","2":"","3":"","4":"","5":"","6":"","7":"","8":"","9":""}
	DicoGuessLetter = {"a" :"","b" :"","c" :"","d" :"","e" :"","f" :"","g" :""}
	#Find 7 | 1 | 8 | 4:
	for number in data:
		if len(number) == 3:
			DicoGuessNumber["7"] = number
		elif len(number) == 2:
			DicoGuessNumber["1"] = number
		elif len(number) == 7:
			DicoGuessNumber["8"] = number
		elif len(number) == 4:
			DicoGuessNumber["4"] = number
	# Guess "a"	
	DicoGuessLetter["a"] = [x for x in DicoGuessNumber["7"] if x not in [y for y in DicoGuessNumber['1']]][0] 
	#print(f" a : {DicoGuessLetter['a']}")
	# Guess "f"
	for index,number in enumerate(data):
		if len(number) == 6:
			if len([x for x in number if x in DicoGuessNumber["1"]]) ==1:
				DicoGuessLetter["f"] = [x for x in number if x in DicoGuessNumber["1"]][0]
			else:
				Findc = [x for x in number if x in DicoGuessNumber["1"]]
	#print(f" f : {DicoGuessLetter['f']}")
	# Guess "c"
	DicoGuessLetter["c"] = [x for x in Findc if x != DicoGuessLetter["f"]][0]
	#print(f" c : {DicoGuessLetter['c']}")
	# Guess "d"
	for letter in [x for x in ["a","b","c","d","e","f","g"] if x not in [DicoGuessLetter['a'],DicoGuessLetter['f'],DicoGuessLetter['c']]]: 
		count = 0
		for number in [x for x in data if (len(x) != 3 and len(x) != 2 and len(x) != 4 )]:
			if letter in number:
				count += 1
		if count == 6:
			DicoGuessLetter["d"] = letter
			break
	#print(f" d : {DicoGuessLetter['d']}")
	# Guess "b"
	DicoGuessLetter["b"] = [x for x in DicoGuessNumber["4"] if x not in [DicoGuessLetter['d'],DicoGuessLetter['c'],DicoGuessLetter['f']]][0] 
	#print(f" b : {DicoGuessLetter['b']}")
	# Guess "g"
	for numberMixt in [x for x in data if (len(x) == 6)]:
		numberSimplified = numberMixt
		for x in DicoGuessLetter:
			numberSimplified = numberSimplified.replace(DicoGuessLetter[x],"")
		if len(numberSimplified) == 1:
			DicoGuessLetter["g"] = numberSimplified
	#print(f" g : {DicoGuessLetter['g']}")
	# Guess "e"
	DicoGuessLetter["e"] = [x for x in ["a","b","c","d","e","f","g"] if x not in DicoGuessLetter.values()][0]
	#print(f" e : {DicoGuessLetter['e']}")
	return DicoGuessLetter

def OutPutUpdate(data,updateLetter):
	#Return the Output number with real letter for each segment
	newList = []
	for number in data:
		newNumber = ""
		for letter in number:
			for realLetter in updateLetter:
				if updateLetter[realLetter] == letter:
					newNumber += realLetter
					break
		newList.append(newNumber)
	return newList	

FinalResult = 0

for index in data:

	CombinaisonLetter = FlowLookUp(index[0])
	newValue = OutPutUpdate(index[1],CombinaisonLetter)
	#print(newValue)
	RESULTList = []

	for output in newValue:
		print("---")
		#print(output)
		for Digit in DicoNumberLetter :
			if len(output) == len(DicoNumberLetter[Digit]):
				print(f"{Digit} : {DicoNumberLetter[Digit]} with {output}")
				checkIn = False
				for letters in output:
					if letters in DicoNumberLetter[Digit]:
						checkIn = True
					else:
						checkIn = False
						break
				if checkIn:
					RESULTList.append(Digit)
					break

	print(RESULTList)
	print(int(RESULTList[0])*1000 + int(RESULTList[1])*100+int(RESULTList[2])*10+int(RESULTList[3]))
	FinalResult += int(RESULTList[0])*1000 + int(RESULTList[1])*100+int(RESULTList[2])*10+int(RESULTList[3])

print(f"Result Day8 ** is {FinalResult}")

"""
"0" : 6 #
"2" : 5 ##
"3" : 5 ##
"5" : 5 ##
"6" : 6 #
"9" : 6 #

"1" : 2 OK
"4" : 4 OK
"7" : 3 OK
"8" : 7 OK

a = 7 - 1  OK
f = 1 - 6 OK
c = 7 - (a et f) OK
d = "celui qu'ils ont tous en commun" (sauf 1 et 7)
b = 4 - (d,c,f)
e = 8 - (6 lettres)
g = autro  

"""

#     
# b    
# b    
#  dddd
# e    
# e    
#  gggg

#  Base  # Modified
#  aaaa  #  dddd
# b    c # e    a
# b    c # e    a
#  dddd  #  ffff
# e    f # g    b
# e    f # g    b
#  gggg  #  cccc