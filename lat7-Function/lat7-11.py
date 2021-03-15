def inputan():
	a=str(input("Masukkan No HP: "))
	return a
def cek(hp):
	hp=inputan()
	hp
	if hp[0]!="0" and hp[1]!="8":
		print("No HP harus dimulai dengan 08")
		return cek(hp)
	elif len(hp)>=13:
		print ("No HP hanya maksimal 13 Angka")
		return cek(hp)
	else:
		return("Nomor HP saya adalah: "+hp)
a=''
print(cek(a))