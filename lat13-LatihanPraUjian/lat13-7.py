def persistence(s):
    s=str(s)
    ulang=0
    while len(s)!=1:
        jawab = 1
        for num in s:
            jawab *= int(num)
        s=str(jawab)
        ulang+=1
    print("hasil: ",ulang)
x=int(input("Masukkan Angka: "))
print(persistence(x))