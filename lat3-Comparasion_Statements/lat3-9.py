#konversi suhu Farenheit ke celcius

F= float(input('Masukan suhu(dalam Farenheit): '))
C=float((F-32) * 5/9)
print("Suhu badan Anda adalah: ",C," Derajat Celcius")
if C<36.5:
    print("Anda HIPOTERMIA")
elif 36.5<=C<=37.2:
    print("Suhu badan Normal")
elif C>37.2:
    print("Anda HIPERTERMIA")