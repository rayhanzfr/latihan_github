x=str(input("masukan sebuah kalimat: "))
panjang=len(x)
while 0<=len(x)<=50 or len(x)>50:
    if 0<len(x)<=50:
        y=x.replace(" ","")
        print("*"+str.upper(y)+"*")
        break
    elif len(x)==0:
        print("Masukkan sebuah inputan")
        x=str(input("masukan sebuah kalimat: "))
    else:
        print("Melebihi batas(50 karakter) ")
        x=str(input("masukan sebuah kalimat: "))