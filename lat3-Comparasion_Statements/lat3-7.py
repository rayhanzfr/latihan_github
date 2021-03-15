import math

jmlHari= int (input('Masukan Jumlah hari:'))
if jmlHari>=0:
    tahun=math.floor(jmlHari/360)
    sisahari1=(jmlHari%360)
    bulan=math.floor(sisahari1/30)
    sisahari2=(sisahari1%30)
    minggu=math.floor(sisahari2/7)
    sisahari3=(sisahari2%7)
    print(str(jmlHari)+'hari='+str(tahun)+'tahun,'+str(bulan)+'bulan,'+str(minggu)+'minggu,'+str(sisahari3)+'hari')
else:
    print("Jumlah hari tidak boleh Negatif")