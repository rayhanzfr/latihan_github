#n(10) = ….. (2)

a= int(input('Masukan Bilangan Desimal='))
Nb=' '
while a>=1:
    if a % 2 == 0:
        Nb='0'+Nb
    else:
        Nb='1'+Nb
    a=int (a/2)
print('Nilai Konversi desimal menjadi biner adalah',Nb)