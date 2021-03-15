#masukan tanda buka kurungnya:{{ <2
#masukan tutup kurungnya: ) <2
#masukan kalimat:
#{{....)

a=str(input("Masukan tanda buka kurungnya: "))
b=str(input("Masukan tanda tutup kurungnya: "))
kal=str(input("Masukan kalimat: "))
if len(a)<=2:
    modA=a+kal
    if len(b)<=2:
        modB=modA+b
        kal=modB
        print(kal)
    else:
        print("Maksimal hanya boleh 2 karakter")
else:
    print("Maksimal hanya boleh 2 karakter")
