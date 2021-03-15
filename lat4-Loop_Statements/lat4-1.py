a=int
while a!=0:
    print("Menu:")
    print("1. Luas dan Keliling Persegi")
    print("2. Volume dan Luas Alas Kubus")
    print("3. Pemilu")
    print("4. Perkuliahan")
    print("0. Akhiri Program")
    a=int(input("Pilih Menu: "))
    if a==1:
        x=float(input("Masukkan Sisi Persegi: "))
        l=x**2
        k=x*4
        print("Luas dan Keliling Persegi berturut turut adalah: ",l,"dan",k,)
        y=int(input("Apakah Sudah puas?(1/0) "))
        while y==0 and y==1:
            if y==1:
                print("\n\n")
            elif y==0:
                break
            else:
                print("Pilihan salah")
                y=int(input("Apakah Sudah puas?(1/0) "))
    elif a==2:
        x=float(input("Masukkan Sisi Kubus: "))
        v=x**3
        l=x*x*6
        print("Volume dan Luas Permukaan Kubus berturut turut adalah: ",v,"dan",l)
    elif a==3:
        x=(str(input("Sudah punya KTP? (iya/tidak): ")))
        pilA=x.lower()
        if  "ya" in pilA:
            pil1=str(input("Apakah akan ikut pemilu? (iya/tidak): "))
            pilB=pil1.lower()
            if "ya" in pilB and ("tidak" or "ga") not in pilB:
                print("Kalian KEREN")
            else:
                print("Kalian tidak keren")
        elif ("tidak" and "ga") in pilA:
            print("coba bikin atau urus dulu KTPnya")
    elif a==4:
        x=(int(input("Sudah kuliah? (1. sudah/ 2. belum): ")))
        if  x==1:
            print("ayok ikut ospek")
        elif x==2:
            print("semangat kawan")
    elif a==0:
        print("bye")
    else:
        print("pilihan tidak ada")
