def reverse_join_reversed_iter(mytxt):
	txt=''
	for i in mytxt:
		txt +=(''.join(reversed(i))+' ')
	return txt
mytxt=(input("Masukkan Kalimat: ").split())
print(reverse_join_reversed_iter(mytxt))