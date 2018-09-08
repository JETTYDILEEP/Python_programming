a=[]
k=0
n,m=input("").split()
n=int(n)
m=int(m)
for i in range(0,n):
    b=int(input(""))
    a.append(b)

for i in range(0,n):
    if(a[i]==m):
      k=k+1

print(k)
