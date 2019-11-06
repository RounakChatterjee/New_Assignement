L = [1,2,4,8,32,64]
X =5 
i = 0
for i in range(0,len(L)):
	if 2**X == L[i]:
		print(2**X," found at index ",i)
		break
else:
	print(2**X," not found")
	
