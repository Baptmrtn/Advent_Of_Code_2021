
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

print(data[0])


DicoGuessNumber = {"0":"","1":"","2":"","3":"","4":"","5":"","6":"","7":"","8":"","9":""}
DicoGuessLetter = {"a" :"","b" :"","c" :"","d" :"","e" :"","f" :"","g" :""}

def FlowLookUp(data):
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
	
	DicoGuessLetter["a"] = [x for x in DicoGuessNumber["7"] if x not in [y for y in DicoGuessNumber['1']]][0] 

	for index,number in enumerate(data):
		if len(number) == 6:
			if len([x for x in number if x in DicoGuessNumber["1"]]) ==1:
				DicoGuessLetter["f"] = [x for x in number if x in DicoGuessNumber["1"]][0]
			else:
				Findc = [x for x in number if x in DicoGuessNumber["1"]]
	DicoGuessLetter["c"] = [x for x in Findc if x != DicoGuessLetter["f"]][0]

	for letter in ["a","b","c","d","e","f","g"]:
		count = 0
		for number in [x for x in data if (len(x) != 3 and len(x) != 2)]:
			if letter in number:
				count += 1
			
		if count == 6:
			DicoGuessLetter["d"] = letter
			print(f"{letter} pass")
			break

	print(DicoGuessLetter)



FlowLookUp(data[0][0])


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

#  aaaa   
# b    c
# b    c
#  dddd
# e    f
# e    f
#  gggg


#  aaaa  #  dddd
# b    c # e    a
# b    c # e    a
#  dddd  #  ffff
# e    f # g    b
# e    f # g    b
#  gggg  #  cccc