def check(z):
  if(z%2==0):
    print("even")
  else:
    print("odd")  

def main():
  try:
    m,n=int(raw_input("")).split( )
    check(m*n)
  except:
    print("invalid")  

main()    
