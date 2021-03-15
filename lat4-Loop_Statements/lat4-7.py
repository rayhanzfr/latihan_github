jml=int(input("Masukan angka terakhir yang hendak ditampilkan: "))
awal=int(input("Bilangan pertama: "))
akhir=int(input("Bilangan kedua: "))
for i in range (0,jml+1):
    if i % awal == 0 and i% akhir == 0:
        print("fizzbuzz")    
    elif i % awal == 0:
        print("fizz")    
    elif i % akhir == 0:
        print("buzz")
    else:    
        print(i)