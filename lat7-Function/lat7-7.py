from collections import Counter

def Fmed(n,angka):
	angka.sort()
	if n % 2 == 0: 
		median1 = angka[n//2] 
		median2 = angka[n//2 - 1] 
		median = (median1 + median2)/2
	else: 
		median = angka[n//2]
	return median
def Fmodus(n,angka):
	data = Counter(angka) 
	modus = dict(data) 
	mode = [k for k, v in modus.items() if v == max(list(data.values()))]   
	if len(mode) == n: 
		modus = "Modus tidak ada"
	else: 
		modus = "Modusnya adalah: " + ','.join(map(str, mode))
	return modus

angka = list(i for i in input("Masukkan Angka : ").split(','))
y=[int(j) for j in angka]
n = len(y)
print("Mediannya adalah: ",Fmed(n,y))
print(Fmodus(n,y))