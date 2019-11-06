L = [1,2,4,8,32,64]
X =5 
i = 0
while i<len(L):
	if 2**X == L[i]:
		print(2**X," found at index ",i)
		break
	else:
		i = i+1
else:
	print(2**X," not found")
	
