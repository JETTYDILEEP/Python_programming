s=input()
if '/' in s:
  m,n=map(int,s.split('/'));
  v=m//n
elif '%' in s:
  m,n=map(int,s.split('%'));
  v=m%n

print(v)  
