class kendaraan:
	def __init__(self,jarak,kapasitas):
		self.jarak=jarak
		self.kapasitas=kapasitas
	def tarif(self):
		harga=self.jarak*self.kapasitas*100
		return harga
class bus(kendaraan):
	def __init__(self,nama,jarak,kapasitas):
		super().__init__(jarak,kapasitas)
		self.nama=nama
	def tambahan(self,a):
		total=(a*110)//100
		return total
jenis=bus("bus sekolah",10,14)
print("Jarak tempuh: {}km".format(jenis.jarak))
print("Kapasitas: {}".format(jenis.kapasitas))
print("Tarif {} yang harus dibayar adalah {}".format(jenis.nama,jenis.tambahan(jenis.tarif())))