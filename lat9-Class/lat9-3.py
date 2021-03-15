# rata rata dan variansi
import math
class statistik:
	def __init__(self,data,ndata):
		self.data=data
		self.ndata=ndata
	def rata2(self):
		if n % 2 == 0: 
			median1 = self.data[self.ndata//2] 
			median2 = self.data[self.ndata//2 - 1] 
			median = (median1 + median2)/2
		else: 
			median = self.data[self.ndata//2]
		return median
	def variansi(self,median):
		atas=0
		for i in self.data:
			atas+=(i-median)**2
			variansi=atas/(self.ndata-1)
			deviasi=math.sqrt(variansi)
		return variansi,deviasi
angka = list(int(i) for i in input("Masukkan Angka : ").split(','))
n = len(angka)
angka.sort()
x=statistik(angka,n)
print(angka)
print(x.rata2())
print("variansi: ",x.variansi(x.rata2))