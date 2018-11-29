m,n=map(int,input().split())
a=max(m,n)
while(True):
  if a%m==0 and a%n==0:
    break
  a+=a  


print(a)
