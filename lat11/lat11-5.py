import math
def combination(i,j):
	x1=math.factorial(i)
	y1=math.factorial(j)
	z1=math.factorial(i - j)
	z2=int((math.factorial(i)) / ((math.factorial(j)) * math.factorial(i - j)))
	print("i:{} ; j:{} ;!i:{} ;!j:{} ;!(i-j):{} \n!i/!j*!(i-j):{}".format(i,j,x1,y1,z1,z2))
	return int((math.factorial(i)) / ((math.factorial(j)) * math.factorial(i - j)))

def segitiga(n_baris):
	hasil = []
	for i in range(n_baris):
		baris = []
		for j in range(i + 1):
			baris.append(combination(i, j))
		hasil.append(baris)
	return hasil
n = int(input("Masukkan Baris: "))
print("\n\n",segitiga(n),"\n\n")
# for i in segitiga(n):
# 	print(i)

