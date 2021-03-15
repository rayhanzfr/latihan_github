# angka=str(input("masukkan angka: "))
# bil=len(angka)

# for i in range (bil-1,-1,-1):
#     balik=""   
#     balik += angka[i]
#     print(balik,end="")

	
awal=int(input("Masukkan batas awal: "))
akhir=int(input("Masukkan batas akhir: "))
n=0
for i in range (awal,akhir+1):
    if i > 1: 
        for j in range(2,i): 
            if (i % j) == 0:
                break 
        else: 
            print(i)
            n+=1 
print("Banyaknya bilangan prima: ",n)
