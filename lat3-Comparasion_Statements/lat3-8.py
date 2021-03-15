#buatlah program yang menampilkan kalimat yang karakternya dibawah 50 karakter
#jika tidak memasukan input apa apa, program akan menampilkan pesan sebuah kalimat

x=str(input("Masukkan Sebuah Kalimat: "))
pjgstring=len(x)
if pjgstring>0:
    if pjgstring<50:
        print("Jumlah kalimat ideal, berikut ini adalah kalimatnya: "+str(x))
    else:
        print("Kalimat yang dimasukan terlalu panjang")
elif pjgstring<=0:
    print("Diharap memasukan sebuah kalimat")