a=[]
n=int(input(""))
for i in range(1,n+1):
    b=int(input(" "))
    a.append(b)

a.sort()
k = len(a)/2
for j in range(1,n+1):
     print(a[k])
     break
