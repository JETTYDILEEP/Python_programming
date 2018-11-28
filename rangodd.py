n,m = map(int,input().split())
for x in range(n+1,m):
  if(x%2!=0):
    print(x,end=' ')
  else:
    print(x,end="")  
