m,n=map(int,input().split())
c=m*n
if(c==0):
  print("yes")
else:
  for i in range(1,c):
    if(i*i==c):
      print("yes")
      break
  else:
    print("no")    
