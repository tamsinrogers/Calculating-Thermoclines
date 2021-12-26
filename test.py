#Tamsin Rogers
#CS152
#Project3
#Lab


import sys

#see what it is
print( sys.argv )

#what is the first element?
print( sys.argv[0])

#what is the second element?
if len(sys.argv) > 1:
	print( sys.argv[1])
else:
	print("not enough things")

#how many things are there?
print( len(sys.argv) )

a = [1,2,3,4,5]
print("number of numbers ", len(a))

#add things to the list
a.apppend(7)
a.apppend(8)
print(a)