
with open("test.txt","r") as file:
	data = []
	for f in file:
		data.append(f.strip().split(" |"))


data[0] = data[0][0].split(" ")

print(data[0])

DicoNumber = {"0":"","1":"","2":"","3":"","4":"","5":"","6":"","7":"","8":"","9":""}
DicoLetter = {"a" :"","b" :"","c" :"","d" :"","e" :"","f" :"","g" :""}




#DicoLetter["a"] = 



"""
"0" : 6 #
"1" : 2
"2" : 5 ##
"3" : 5 ##
"4" : 4
"5" : 5 ##
"6" : 6 #
"7" : 3 
"8" : 7
"9" : 6 #

"1" : 2
"4" : 4
"7" : 3 
"8" : 7

a = 7 - 1 
f = 1 - 6
c = 7 - (a et f)
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