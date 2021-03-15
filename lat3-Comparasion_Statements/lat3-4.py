import math
nApel=float(input("Masukkan jumlah Apel: "))
nJeruk=float(input("Masukkan jumlah Jeruk: "))
nAnggur=float(input("Masukkan jumlah Anggur: "))

hApel=float (input('Masukkan Jumlah Harga Apel:'))
hJeruk=float (input('Masukkan Jumlah Harga Jeruk:'))
hAnggur=float (input('Masukkan Jumlah Harga Anggur:'))

tApel= nApel*hApel
tJeruk=nJeruk*hJeruk
tAnggur=nAnggur*hAnggur
Total=tApel+tJeruk+tAnggur

print("\nDetail Belanja")
print("Apel: "+str(nApel)+" x "+str(hApel)+" = "+str(tApel))
print("Jeruk: "+str(nJeruk)+" x "+str(hJeruk)+" = "+str(tJeruk))
print("Anggur: "+str(nAnggur)+" x "+str(hAnggur)+" = "+str(tAnggur))
print("Total: Rp."+str(Total))
uang=float(input("\nMasukkan jumlah uang: "))
kembali=float (uang-Total)
if kembali>0:
    print("Terima Kasih")
    print("Uang kembali anda"+str(kembali))
elif kembali==0:
    print("Terima Kasih")
elif kembali<0:
    print("Transaksi anda dibatalkan")
    print("Uangnya kurang sebesar",int(abs(kembali)))
