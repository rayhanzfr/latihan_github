hp=str(input("Masukkan No HP: "))
a=hp.count("0")
if hp[0]!="0" and hp[1]!="8":
    print("No HP harus dimulai dengan 08")
elif len(hp)>=13:
    print("No HP hanya maksimal 13 Angka")
else:
    print("Nomor HP saya adalah: ",hp)