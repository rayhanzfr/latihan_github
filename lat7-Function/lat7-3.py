import math
def inputan(data,n):
	for i in range(n):
		temp = int(input("Masukkan data ke-%d: " %(i+1)))
		data.append(temp)
	return data
def ratarata(data,n):
	jum=0
	rata2=0
	for i in data:
		jum += i
		rata= jum / n
		rata2 = rata
	return rata2
def vsdv(data,n):
	atas=0
	for i in data:
		atas+=(i-ratarata(data,n))**2
	variansi=atas/(n-1)
	deviasi=math.sqrt(variansi)
	return variansi,deviasi
n = int(input("\nBanyaknya Data: "))
data=[]
print(inputan(data,n))
print("Rata Rata\t\t :%.2f"%ratarata(data,n))
variansi=vsdv(data,n)[0]
deviasi=vsdv(data,n)[1]
print("Variansi\t\t :%.2f"%variansi)
print("Standar Deviasi\t\t :%.2f\n"%deviasi)

# for i in range(0, n):
#     temp = int(input("Masukkan data ke-%d: " %(i+1)))
#     data.append(temp)
#     x+=data[i]**2
#     jum += data[i]
#     rata= jum / n
#     rata2 = rata
# for j in data:
#     atas+=(j-rata2)**2
#     print("ratarata",rata2)
# maxi=max(data)
# mini=min(data)
# rng=(maxi-mini)
# variansi=atas/(n-1)
# deviasi=math.sqrt(variansi)
# print(data)
# print("\nRata-Rata  = %0.2f" % rata2)
# print("\nVariansi  = %0.2f" %variansi)
# print("\nStandar Deviasi  = %0.2f" %deviasi)
# print("Range: ", rng)