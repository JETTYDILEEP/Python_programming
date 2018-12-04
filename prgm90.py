n=input()
i=list(n)
a=''
for v in i:
	if v.isnumeric():
		a+=v
print(a)
