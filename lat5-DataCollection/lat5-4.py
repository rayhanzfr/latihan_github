awal= [item for item in input("Masukkan Kalimat : ").split()] 
n=int(input("Minimum huruf yang ditampilkan: "))
# akhir=[]
print(awal)
print("Berikut ini Daftar kata yang lebih dari atau sama dengan %d huruf: "%n)
for x in awal:
	if len(x) >= n:
		# akhir.append(x)
		akhir=x
		print(akhir)