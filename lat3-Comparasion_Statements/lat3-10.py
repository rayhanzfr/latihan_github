#Masukan Kalimat: Saya adalah akhmad kurniansyah
#Masukan Kata/Karakter yang dihilangkan: a
#Kalimat awal:
#Kalimat yang sudah dimodifikasi:

awal=str(input("Masukan Kalimat: "))
char= str(input("Masukan Kata/Karakter yang dihilangkan: "))
if char or char.upper() in awal:
    modif=awal.replace(char,"" )
    modif1=modif.replace(char.lower(),"")
    print("Kalimat Awal: "+awal)
    print("Kalimat Modifikasi: "+modif1)
else:
    modif=awal
    print(awal)
    print(modif)