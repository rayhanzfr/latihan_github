from datetime import date ,timedelta
def penanggalan():
    thn=(int(input("Masukkan Tahun: ")))
    bln=(int(input("Masukkan Bulan (Dari 1-12): ")))
    tgl=(int(input("Masukkan Hari/Tanggal (Dari 1-31): ")))
    if thn%4==0 and bln==2 and tgl>29:
        print("Tanggal tidak ada\n\n")
        return penanggalan()
    elif thn%4!=0 and bln==2 and tgl>=29:
        print("Tanggal tidak ada!\n\n")
        return penanggalan()
    elif 0<bln<=12 and 0<tgl<=31:
        tanggal = date(thn, bln, tgl) # tahun, bulan, tanggal
        return tanggal
    else:
        print("Inputan Salah!\n\n")
        return penanggalan()
besok=penanggalan()+timedelta(days=1)
print('{0.day}-{0.month}-{0.year}'.format(besok))