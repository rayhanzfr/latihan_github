def reverse(mytxt,n):
	txt=''
	for i in mytxt:
		if (len(i)>=n):
			txt +=(''.join(reversed(i))+' ')
		else:
			txt+=''.join(i)+' '
	return txt
mytxt=(input("Masukkan Kalimat: ").split(' '))
n=int(input("Masukkan angka batas: "))
print(reverse(mytxt,n))