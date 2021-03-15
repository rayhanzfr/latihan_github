baris=int (input("masukkan jumlah baris maksimal: "))
for i in range (1,baris+1,1):
    for j in range (1,i+1,1):
        print(j,end=' ')
    print('')


# bil=int(input("Masukkan angka: "))
# if bil>=0:
#     fak=1
#     for i in range(1,bil+1):
#         fak=fak*i
#     print("Nilai dari "+str(bil)+"! adalah",fak)
# else:
#     print("Faktorial hanya diperbolehkan untuk Bilangan Positif")

