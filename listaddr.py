a=[]
n=int(input(" "))
for i in range(1,n+1):
  b=int(input(" "))
  a.append(b)

for i in range (1,n+1):
  print(a[i-1],(i-1))  
