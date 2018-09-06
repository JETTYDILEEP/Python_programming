a=[]
n=int(input(" "))
max=0
for i in range(1,n+1):
  b=int(input(" "))
  a.append(b)
for i in a:
	if max<i:
		max=i

print(max)
