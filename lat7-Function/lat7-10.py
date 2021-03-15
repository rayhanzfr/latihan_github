def soal(x):
	x=str.upper(x)
	x=x.split(" ")
	s="*"
	for i in x:
		s+=i
	s+="*"
	return s
def inputan():
	kal=input("Masukkan Kalimat: " )
	while len(kal)>50:
		print('Maksimal 50 Karakter')
		kal=input("Masukkan Kalimat: ")
	while len(kal)==0:
		print("Masukkan sebuah inputan ")
		kal=(input("Masukkan kalimat"))
	kal=''+soal(kal)+'*'
	return kal
print(inputan())