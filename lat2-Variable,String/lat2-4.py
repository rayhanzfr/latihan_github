import math

Apel=int (input('Masukkan Jumlah Apel:'))
Jeruk=int (input('Masukkan Jumlah Jeruk:'))
Anggur=int (input('Masukkan Jumlah Anggur:'))

HApel=int (input('Masukkan Jumlah Harga Apel:'))
HJeruk=int (input('Masukkan Jumlah Harga Jeruk:'))
HAnggur=int (input('Masukkan Jumlah Harga Anggur:'))

TApel= Apel*HApel
TJeruk=Jeruk*HJeruk
TANggur=Anggur*HAnggur
Total=TApel+TJeruk+TANggur

print('Jumlah Harga Apel:'+str(TApel)+'\nJumlah Harga Jeruk'+str(TJeruk)+'\nJumlah Harga Anggur:'+str(TANggur)+'\nTotal Harga:'+str(Total))


