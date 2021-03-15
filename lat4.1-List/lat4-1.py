baris = int(input("Banyaknya baris :"))
bahan=""

for i in range (baris,0,-1):
	for j in range(0,i):
		bahan += " "		
	bahan += "\t"
for k in range (1,baris+1):
    bahan += "\t"
    for l in range(0,k):
        bahan += " * "		
    bahan +="\n"
print (bahan)