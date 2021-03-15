class Person:
	def __init__(self,name,age):
		self.nama=name
		self.umur=age
	def kenalan(self,SalamKenal):
		print('Halo Nama Saya {} Umur {}, Salam Kenal {}'.format(self.nama,self.umur,SalamKenal))
#class 2
class segitiga:
	def __init__(self,alas,tinggi):
		self.alas=alas
		self.tinggi=tinggi
		alastinggi=self.alas*tinggi
	def keliling(self):
		keliling=(self.alas+self.tinggi)/2
		return keliling
	def luas(self):
		luas=(self.alas*self.tinggi)/2
		return luas
class purwadhika(Person):
	def __init__(self,name,age,kelas,nilai):
		super().__init__(name,age)
		self.kelas=kelas
		self.nilai=nilai
	def kenalan1(self,kata):
		super().kenalan(kata)
fana=purwadhika('Fana',22,"Purwadhika JC",9)
print("""
saya {} umur {} berada di kelas {} 
dan mendapatkan nilai akhir {}"""
.format(fana.nama,fana.umur,fana.kelas,fana.nilai))

fana.kenalan1("salam kenal")