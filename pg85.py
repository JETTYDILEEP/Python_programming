s=input()
l=list(s)
(m,n)=('','')
for i in range(len(s)):
  if(i%2==0):
    m+=l[i]
  elif(i%2!=0):
    n+=l[i]
  
print(m,n)
