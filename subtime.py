h, m = int(input(" ")) , int(input(" "))
h1, m1 = int(input(" ")) , int(input(" "))
if(h<=12 and h1<=12 and m<=60 and m1<=60):
  h2=h-h1
  h2=abs(h2)
  m2=m-m1
  m2=abs(m2)


print(h2 , m2)

