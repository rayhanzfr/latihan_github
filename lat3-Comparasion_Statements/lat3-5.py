x= int(input("Masukan Angka: "))
if x%2==0:
    if x>0:
        print("Angka'",x,"'tergolong bilangan Genap")
    elif x==0:
        print("0 bukan bilangan ganjil maupun genap")
    elif x<0:
        print("Masukkan bilangan Bulat Positif")
else :
        print("Angka "+str(x)+" tergolong bilangan Ganjil")