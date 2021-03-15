baris = int(input("Banyaknya baris :"))
bahan=""
for i in range (baris,0,-1):
	for j in range(0,i):
		bahan = bahan + " * "		
	bahan = bahan + "\n"
for k in range (2,baris+1):
    for l in range(0,k):
        bahan = bahan + " * "		
    bahan = bahan + "\n"
print (bahan)