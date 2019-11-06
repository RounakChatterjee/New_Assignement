a = 0
b = 1
c = 0
print("first 10 Fibonacci numbers are: \n\n",a,"\n\n",b)
for i in range(8):
	c = a+b
	print("\n",c)
	a = b
	b = c
	c = 0