'''
String unicode by map class
'''
def uni(x):
	return ord(x)
S = "mumbai"
a = map(uni,S)# the map function maps every character from S to uni(x)
print("The unicodes for letters in ",S," is",list(a))
