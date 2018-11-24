n=int(input())
r=[]
m=n%10
while(n!=0):
	r.append(m)
	n//=10
for i in range(len(r)-1,-1,-1):
	if r[i]%2!=0:
		print(r[i])
