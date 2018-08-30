a=[]
n=int(input(" "))
for i in range(1,n+1):
    b=int(input(" ").split())
    a.append(b)
a.sort()
print(a[n-1])
