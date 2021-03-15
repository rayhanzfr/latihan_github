def pangkat(n):
	awal= list(item for item in input("Masukkan Angka : ").split())
	awal=[int(i) for i in awal]
	# proses = [i*5 for i in awal]
	# for x in awal:
	# 	proses.append(x*5)
	return [i*5 for i in awal],awal
n=1
print(pangkat(n))