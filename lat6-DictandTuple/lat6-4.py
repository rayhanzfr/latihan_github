iniTuple=(input("Tuple:\t").replace(' ','').split(','))
angkaTuple=tuple(map(int,iniTuple))
a=1
print("Proses Perkalian: ")
for x in angkaTuple:
	print("%d x"%a,x)
	a=(a*x)
	print(a)
print("\nOriginal Tuple:\n",angkaTuple)
print("Hasil Kali Semua Elemen adalah = %d"%a)