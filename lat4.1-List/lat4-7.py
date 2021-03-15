n=int(input("Masukkan Bilangan: "))
bantu=0
kosong=0
for i in reversed(range(n)):
	for j in range(i+1):
		print(' ', end='')
	for k in range(bantu+1):
		if k==0 and i==n-1:
			print('***', end='')
		elif k==0:
			print('**', end='')
		else:
			print(' ', end='')
	for l in range(bantu):
		if l==kosong:
			print('**', end='')
			kosong+=1
		else:
			print(' ', end='')
	bantu+=1
	print()
for i in range(n+2):
	print('**', end='')