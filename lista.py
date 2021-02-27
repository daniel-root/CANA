v = [8,6,4,2,5,3,1,9,8]
x = 28
v.append(x)
print(v)
i=0
while(v[i] != x):
	if(v[i]==x):
		print("Encontrei na possição",i+1)
		return 0
	i=i+1
print("Elemento não está presente")
	