'''
This program finds the first 100 fibonacci numbers and times the progam to get time taken
'''
import timeit as t
def fibo(n):
	b = 1
	a = 0
	c = 0
	print("first ",n," Fibonacci numbers are: \n\n",a,"\n\n",b)
	for i in range(n-2):
		c = a+b
		print("\n",c)
		a = b
		b = c
		c = 0
fibo(100)
print("\n The time taken by the program to run =  ",t.timeit())
