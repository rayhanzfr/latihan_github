# def visual():
# 	bantu=0
# 	kosong=0
# 	x=input1()
# 	for i in reversed(range(x)):
# 		for j in range(i+1):
# 			print(' ', end='')
# 		for k in range(bantu+1):
# 			if k==0 and i==x-1:
# 				print('***', end='')
# 			elif k==0:
# 				print('**', end='')
# 			else:
# 				print(' ', end='')
# 		for l in range(bantu):
# 			if l==kosong:
# 				print('**', end='')
# 				kosong+=1
# 			else:
# 				print(' ', end='')
# 		bantu+=1
# 		print()
# 	for i in range(x+2):
# 		print('**', end='')
# 	return ''
# def input1():
# 	x=int(input("Masukkan Bilangan: "))
# 	return x

# print(visual())


def dalam(bantu,i,n,kosong):
	x=kosong
	for i in range(bantu):
		if i==x:
			print('**', end='')
			x+=1
		else:
			print('', end='')
	return x
		
def luarkiri(bantu,i,n):
	for k in range(bantu+1):
		if k==0 and i==n-1:
			print('***', end='')
		elif k==0:
			print('**', end='')
		else:
			print(' ', end='')
	return bantu
def luarkanan(bantu,i,n):
	for k in range(bantu+1):
		if k==0 and i==n-1:
			print('', end='')
		elif k==0:
			print('', end='')
		elif k==bantu:
			print('**',end='')
		else:
			print(' ', end='')
	return bantu
def kosongkiri(bantu,i,n):
	for i in range(i+1):
		print(' ', end='')
def kosongkanan(bantu,i,n):
	for i in (range(0,i+1-1)):
		print('=', end='')
def segitiga1():
	n=int(input("Masukkan Bilangan: "))
	bantu=0
	# kosong=0
	for i in reversed(range(n)):
		kosongkiri(bantu,i,n)
		luarkiri(bantu,i,n)
		luarkanan(bantu,i,n)
		# dalam(bantu,i,n,kosong)
		bantu+=1
		print()
	for i in range(n+2):
		print('**', end='')
	return ''
print(segitiga1())