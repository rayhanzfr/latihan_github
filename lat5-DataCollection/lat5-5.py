# import math
# bil_awal = int(input('Masukan bilangan awal: '))
# bil_akhir = int(input('Masukan bilangan akhir: '))
 
# list_bil = [i for i in range(bil_awal, bil_akhir +1 )]
# print('Daftar bilangan: {}'.format(list_bil))

# bil_ganjil = []
# bahan=""
# for bil in list_bil:
#     if bil % 2 != 0:
#         bil_ganjil.append(bil)
 
# print('ganjil: {}'.format(', '.join([str(bil) for bil in bil_ganjil])))



# # bilangan=[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59,61,63,65,67,69,71]
# # bahan=[]
# # spasi=''
# string=""
# x = math.sqrt(len(bil_ganjil))+1
# bar = x
# no = 0
# # Looping Baris
# while bar >= 0:
# 	# Looping Kolom Spasi Kosong
# 	kol = bar
# 	while kol > 0:
# 		string = string + "   "
# 		kol = kol - 1
# 	# Looping Kolom Angka Sisi Kiri
# 	kiri = 0
# 	while kiri < (x - (bar-1)):
# 		if kiri == (x-(bar-1)-1):
# 			string = string + " " + str(bil_ganjil[no]) + " "
# 			no=no+1
# 		kiri = kiri + 1
# 	# Looping Kolom Angka Sisi Kanan
# 	kanan = 0
# 	while kanan < kiri -1:
# 		if kanan == kiri -2:
# 			string = string + " " + str(bil_ganjil[no]) + " "
# 			no=no+1
# 		kanan = kanan + 1

# 	string = string + "\n\n"
# 	bar = bar - 1

# print (string)



# Jumlah Baris
row = int(input("Jumlah baris: "))

# Jumlah Data
n = 1
for i in range(row, 0, -1):
	n += i
	print(n)

# List Data
numbers = [(2*number)-1 for number in range(1, n+1)]
print(numbers)
numbers_even = [(2*number) for number in range(1, n+1)]

# Visualisasi Data
index = 0
space = row * 4
for i in range(1, row+1):
	output_1 = numbers[index:index+i]
	print(output_1)
	output_2 = [str(item) for item in output_1]
	print(output_2)
	output_3 = "  ".join(output_2)
	#print(output_1)
	blank_1 = space - len(output_3)
	blank_2 = blank_1 // 2
	print(" " * blank_2 + output_3 + " " * blank_2)
	index += i

formula = ' + '.join(output_2)
total = 0
for item in output_1:
    total += item
print(f"\n{formula} = {total}")  