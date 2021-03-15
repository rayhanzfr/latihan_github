import random
def inputan():
	x= int (input("Masukkan Angka : "))
	return x
def inputMenu():
	print('''
	MENU:
	1. Urut
	2. Random
 	''')
	x= int (input("Masukkan Angka : "))
	while x>2 or x<1:
		x= int (input("Masukkan Angka : "))
	return x
def mat(x,z):
	mat = [[0 for i in range(x)] for j in range(x)]
	if z == 1:
		counter = 1
		for i in range(x): 
			for j in range(x):  
				mat[i][j] = counter
				counter +=1
	else:
		for i in range(x):
			for j in range(x):
				counter = random.randint(0,100)
				mat[i][j] = counter
	return mat


def main():
    x = inputan()
    z = inputMenu()
    y = mat(x,z)
    for i in range(x):
        for j in range(x):
            print(" ",end=str(y[i][j]))
        print()
main()