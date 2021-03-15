import math

stk_apel=float(input("Jumlah Stock Apel: "))
stk_jeruk=float(input("Jumlah Stock Jeruk: "))
stk_anggur=float(input("Jumlah Stock Anggur: "))
jml_apel=float(input("Jumlah Apel:"))
while jml_apel>stk_apel or jml_apel<0:
    print("Stok tinggal",stk_apel)
    jml_apel=float(input("Jumlah Apel:"))
jml_jeruk=float(input("Jumlah Jeruk:"))
while jml_jeruk>stk_jeruk or jml_jeruk<0:
    print("Stok tinggal",stk_jeruk)
    jml_jeruk=float(input("Jumlah Jeruk:"))
jml_anggur=float(input("Jumlah Anggur:"))
while jml_anggur>stk_anggur or jml_anggur<0:
    print("Stok tinggal",stk_anggur)
    jml_anggur=float(input("Jumlah Apel:"))

hApel=float (input('Masukkan Jumlah Harga Apel:'))
hJeruk=float (input('Masukkan Jumlah Harga Jeruk:'))
hAnggur=float (input('Masukkan Jumlah Harga Anggur:'))

tApel= jml_apel*hApel
tJeruk=jml_jeruk*hJeruk
tAnggur=jml_anggur*hAnggur
Total=tApel+tJeruk+tAnggur

print("\nDetail Belanja")
print("Apel: "+str(jml_apel)+" x "+str(hApel)+" = "+str(tApel))
print("Jeruk: "+str(jml_jeruk)+" x "+str(hJeruk)+" = "+str(tJeruk))
print("Anggur: "+str(jml_anggur)+" x "+str(hAnggur)+" = "+str(tAnggur))
print("Total: Rp."+str(Total))
uang=float(input("\nMasukkan jumlah uang: "))
kembali=float (uang-Total)
while kembali<0:
    if kembali>0:
        print("Terima Kasih")
        print("Uang kembali anda"+str(kembali))
    elif kembali==0:
        print("Terima Kasih")
    elif kembali<0:
        print("Transaksi anda dibatalkan")
        print("Uangnya kurang sebesar",int(abs(kembali)))
        uang=float(input("\nMasukkan jumlah uang: "))
        kembali=float (uang-Total)

