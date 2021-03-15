def inputan():
	x=int(input("Masukkan angka: "))
	if x>359999:
		print("invalid input")
		x=int(input("Masukkan angka: "))
	return x
def timeconvert (ss):
	hh=ss//3600
	sisa=ss%3600
	mm=sisa//60
	sisa1=sisa%60
	return "(%02d:%02d:%02d)"%(hh,mm,sisa1)
print(timeconvert(inputan()))