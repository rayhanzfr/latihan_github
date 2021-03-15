awal= list(item.lower() for item in input("Masukkan Kalimat : ").split()) 
kamus={}
values=1
for i in awal:
	if i in kamus:
		kamus[i] += values
	else:
		kamus[i] = values
	print(kamus)
print("Jumlah kata terbanyak adalah sebanyak"%max(kamus.values()))
for i in kamus:
	print("Jumlah Kata %s ada sebanyak %s"%(i.capitalize(),kamus[i]))