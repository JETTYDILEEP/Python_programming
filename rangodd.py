n,m = map(int,input().split())
for i in range(n+1,m):
  if i%2==1:
    if(i<m-2):
      print(i,end=' ')
    else:
      print(i,end="")  
