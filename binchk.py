l=['0','1']
f=0
st=input()
m=len(st)
for i in range(m):
	if st[i] in l:
		continue
	else :
		f=1
		break
if f!=1:
	print('yes')
else :
	print('no')
