import math
n = int(input("\nBanyaknya Data: "))

print() #Membuat baris baru
data = []
jum = 0
x=0
rata2=0
atas=0
for i in range(0, n):
    temp = int(input("Masukkan data ke-%d: " %(i+1)))
    data.append(temp)
    x+=data[i]**2
    jum += data[i]
    rata= jum / n
    rata2 = rata
for j in data:
    atas+=(j-rata2)**2
    print("ratarata",rata2)
maxi=max(data)
mini=min(data)
rng=(maxi-mini)
variansi=atas/(n-1)
deviasi=math.sqrt(variansi)
print(data)
print("\nRata-Rata  = %0.2f" % rata2)
print("\nVariansi  = %0.2f" %variansi)
print("\nStandar Deviasi  = %0.2f" %deviasi)
print("Range: ", rng)