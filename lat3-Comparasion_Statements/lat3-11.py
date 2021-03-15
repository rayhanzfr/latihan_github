#suka buryam/tidak: tidak
#(jika ya)
#diaduk/tidak:
#golongan kami/bukan golongan kami
#(jika tidak)
#coba lagi deh kapan kapan



pil=str(input("Suka bubur ayam? (iya/tidak): "))
pilA=pil.lower()
if  "ya" in pilA:
    pil1=str(input("Kalian tim mana? (diaduk/tidak): "))
    pilB=pil1.lower()
    if "diaduk" in pilB and ("tidak" or "ga") not in pilB:
        print("Kalian golongan KAMI")
    else:
         print("Kalian bukan golongan KAMI")
elif "tidak" or "ga" in pilA:
    print("coba makan deh kapan kapan")