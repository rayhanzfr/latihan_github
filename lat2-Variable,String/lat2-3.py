import math

Thari= int (input('Masukan Jumlah hari:'))
tahun=math.floor(Thari/360)
sisahari1=(Thari%360)
bulan=math.floor(sisahari1/30)
sisahari2=(sisahari1%30)
minggu=math.floor(sisahari2/7)
sisahari3=(sisahari2%7)
print(str(Thari)+'hari='+str(tahun)+'tahun,'+str(bulan)+'bulan,'+str(minggu)+'minggu,'+str(sisahari3)+'hari')