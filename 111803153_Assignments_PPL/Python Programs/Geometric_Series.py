
print("Enter the first no and the common ratio: ")
a = int(input("First number: "))
r = int(input("Common ratio: "))
c = 0
l = []
print("The first 10 numbers of Geometric Series are:")
while c < 10:
	l.append(a*(r**c))
	c += 1
print(l)	
