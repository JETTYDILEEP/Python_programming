num = input("")
try:
    n = float(num)
    val = int(n)
    if (val%1==0):
        print("Yes")
   
except ValueError:
    print("No")
