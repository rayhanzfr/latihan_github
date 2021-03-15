awal= list(item for item in input("Masukkan Kalimat : ").split()) 
# akhir=[]
print(awal)
# jumlah=len(awal)
# i=1
# nakhir=0
# akhir=''
# for x in awal:
# 	if i<len(awal):
# 		n=len(awal[i])
# 		print("Panjang kata %s adalah %d\nPanjang kata %s adalah %d"%(x,len(x),awal[i],n))
# 		if len(x)>n and len(x)>nakhir:
# 			nakhir=len(x)
# 			akhir==x
# 			print(len(x))
# 			print(akhir)
# 		elif len(x)==n:
# 			akhir+=x+' '
# 			print(akhir)
# 		else:
# 			if nakhir<n:
# 				nakhir=n
# 				akhir+=awal[i]
# 				print(len(x))
# 				print(akhir)
# 		i+=1
# print("Jumlah Karakter Terbanyak adalah sebesar %d karakter "%nakhir)
# print("Kata yang memiliki jumlah karakter terbanyak adalah ",akhir)

kamus={}
for i in awal:
	kamus[i]=len(i)
	print(kamus)
print("Jumlah karakter terbanyak adalah sebesar %d karakter"%max(kamus.values()))
for i in kamus:
	if kamus[i]==max(kamus.values()):
		print("Kata yang memiliki karakter terbanyak adalah kata: ",i)