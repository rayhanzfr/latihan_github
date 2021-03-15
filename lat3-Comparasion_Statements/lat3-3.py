#IMT =MASSA(KG)/TINGGI(METER)^2

kg=float (input("Masukkan massa(kg): "))
cm=float (input("Masukkan tinggi(cm): "))
m=cm/100
IMT=kg/(m**2)
print("Massa "+str(kg)+" kg & tinggi "+str(m)+" m")
if IMT<18.5:
    print("IMT= "+str(IMT)+" Berat badan kurang")
elif 18.5>=IMT<25:
    print("IMT= "+str(IMT)+" Berat badan ideal")
elif 25>=IMT<30:
    print("IMT= "+str(IMT)+" Berat badan berlebih")
elif 30>=IMT<40:
    print("IMT= "+str(IMT)+" Berat badan sangat berlebih")
else:
    print("IMT= "+str(IMT)+" Obesitas")

