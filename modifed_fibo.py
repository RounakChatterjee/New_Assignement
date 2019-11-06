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