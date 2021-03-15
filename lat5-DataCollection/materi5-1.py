listbaru=[]
nbaru=(int(input("masukkan banyak input: ")))
for i in range (nbaru):
	x=input("data ke-%d:"%(i+1))
	listbaru.append(x)
print(listbaru[1:nbaru])

iniList=[1,2,3,False,'Hai']
print(iniList)
print(type(iniList))

coba=[str(i) for i in iniList]
print(coba)

coba2=(1,2,3,4)
coba2=list(coba2)
print(coba2)