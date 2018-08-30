a=[]
n=int(input(""))
for i in range(1,n+1):
    b=int(input(" "))
    a.append(b)

a.sort()
for j in range(1,n+1):
    print(a[j-1])
