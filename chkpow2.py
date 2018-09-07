def main():
	try:
		k=0
		n=int(input())
		while(n!=0):
			n=n/2
			if n==1:
				k=1
				break
		if k!=1:
			print('no')
		else :
			print('yes')
	except:
		print('invalid')
main()
