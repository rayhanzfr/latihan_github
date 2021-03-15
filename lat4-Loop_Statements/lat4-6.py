import random

number = random.randint(1, 9) #random nomor nomor yang akan ditebak
print("Tebak angka dari 1 sampai 9")
tebak = 0
while tebak != number :
    tebak =int(eval(input("Masukkan tebakan :"))) #pengguna menebak nomor
    if tebak == number:
        print("Tebakan Benar, Nilai yang ditebak",number)
    else:
        print("Tebakan salah")

    # elif tebak > number:
    #     print("Tebakan terlalu tinggi")
    # else:
    #     print("Tebakan terlalu rendah")