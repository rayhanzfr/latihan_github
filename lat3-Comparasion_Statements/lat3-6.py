#menghitung luas segitiga, luas persegi, 
# ketika memasukan angka 3 atau karakter lain, akan mengeluarkan output 'Masukan input yang benar

print("Masukan Angka 1 untuk menghitung luas segitiga")
print("Masukan Angka 2 untuk menghitung luas persegi")
menu=int(input("Pilih Menu yang diinginkan: "))
if menu==1:
    x=float(input("Masukkan Tinggi Segitiga: "))
    y=float(input("Masukkan Alas Segitiga: "))
    l=(x*y)/2
    print("Luas Segitiga tersebut adalah: ",l)
elif menu==2:
    x=float(input("Masukkan Sisi Persegi: "))
    l=x**2
    print("Luas Persegi tersebut adalah: ",float(l))
else:
    print("Masukkan inputan yang benar")    