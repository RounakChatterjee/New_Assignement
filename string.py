S = "mumbai"
s = 0
for i in range(0,len(S)):
	print(S[i]+" Unicode: ",ord(S[i]))
	s = s+ord(S[i])
print("Sum of unicode points: ",s)
