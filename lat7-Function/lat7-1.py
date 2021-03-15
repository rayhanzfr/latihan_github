# create Function untuk bangun datar sebanyak 3 fungsi

def persegipjg(nilai1=1,nilai2=2):
	return nilai1*nilai2
def segitiga(nilai1,nilai2):
	luas=nilai1*nilai2/2
	print("Luas segitiganya adalah %d"%luas)
def lingkaran(nilai1,nilai2):
	return (nilai1**2)*22/7

nilai1=int(input("Masukkan nilai 1: "))
nilai2=int(input("Masukkan nilai 2: "))

print("Luas Persegi Panjang adalah: ",persegipjg(nilai1))
segitiga(nilai1,nilai2)
print("Nilai pertama yang dipakai. Maka Luas Lingkaran adalah: ",lingkaran(nilai1,nilai2))
