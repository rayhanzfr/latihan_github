# bangun ruang, hitung volume, luas alas

class Balok:
	def __init__(self,nama,panjang,lebar,tinggi):
		self.nama=nama
		self.p=panjang
		self.l=lebar
		self.t=tinggi
	def volume(self,a):
		v=a.l_alas*self.t
		return v
	def l_permukaan(self):
		lp=2*(self.p * self.l + self.p * self.t + self.l * self.t)
		return lp
	def l_alas(self):
		la=self.p*self.l
		return la
pjg=int(input("Panjang: "))
lbr=int(input("Lebar: "))
tgg=int(input("Tinggi: "))

br=Balok("balok",pjg,lbr,tgg)
print("Volume dan Luas Permukaan {} adalah: {} dan {}".format(br.nama,br.volume(br.l_alas),br.l_permukaan()))
# print(br.nama)
# print(br.volume())
# print(br.l_permukaan())