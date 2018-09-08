n = input("")
j=0
k=0
for i in n:
  if(i.isalpha()):
    j=j+1
  elif(i.isnumeric()):
    k=k+1

if(j+k==len(n) and j>0 and k>0):
  print("yes")
else:
  print("no")      
