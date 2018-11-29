m,n=map(int,input().split())
while(n!=0):
  t=n
  n=m%n
  m=t

print(m)  
