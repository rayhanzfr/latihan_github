inilist=[1,2,3,4,5]
print(inilist)
print(type(inilist))

angka=[]
n=int(input("banyak baris: "))
for i in range (n,0,-1):
    for j in range(0,i):
        angka.append('*')
    print(angka)
    print("\n")