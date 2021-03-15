listlama=[]
n=(int(input("masukkan banyak input: ")))
for i in range (n):
	x=int (input("data ke-%d:"%(i+1)))
	listlama.append(x)
jum = sum(listlama)
rata= jum / n
if 5 in listlama:
	print(f"Ada angka 5 dalam list. Terdapat pada index ke-{listlama.index(5)}")
else:
	print("Tidak ada angka 5 dalam list")
print("Jumlah: \t",jum)
print("Banyak data: \t",n)
print("Rata Rata: \t",float(rata))
listbaru=listlama.copy()
print(listbaru)
listbaru2 = map(str, listbaru)
print(list(listbaru2))