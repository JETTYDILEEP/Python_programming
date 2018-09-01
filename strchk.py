num = input("")
try:
    val = int(num)
    if (val%1==0):
        print("Yes")
   
except ValueError:
    print("No")
