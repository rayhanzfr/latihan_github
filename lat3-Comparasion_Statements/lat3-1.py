#1
x=float(input("Masukan Nilai: "))
if x>=70:
    print("Siswa lulus\n")

#2
cuaca=str(input("\nCuaca hujan atau cerah?:"))
harikerja=str(input("hari apa sekarang:"))

if (("hujan" or "Hujan") not in cuaca) and "Minggu" not in harikerja:
    print("Berangkat kerja\n")

#3
SKS=int(input("\nJumlah SKS:"))
nilai=int(input("Nilai ujian:"))

if nilai>=80:
    skripsi= str ('A')
    if SKS==150 and 'A' in skripsi:
        print("Lulus ujian skripsi")