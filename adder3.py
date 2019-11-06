'''
This program depicts how to give default value to arguments
'''
def adder(good = 1,bad =2,ugly = 3):
	
	return good + bad + ugly

print(adder(ugly = 1,good = 5))