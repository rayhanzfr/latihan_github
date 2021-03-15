n=int(input("Masukkan nilai n = "))
spasi=" "
diamond="*"
index=["1","2","3","4","5","6","7","8","9","10"]
odd=len(index)
for i in range (1,n+1,1): 
    odd[i-1] = 2*i-1
for i in range(0,n,1):
    for x in range (0,n-i,1):
        print(spasi)
    for x in range (0,odd[i],1):
        print(diamond)
    for x in range(0,n-i,1):    
        print(spasi)
    print("\n")
for j in range (n-2,0,-1):
    for x in range (0, n-i,1): 
        print(spasi)
    for x in range (0,odd[i],1): 
        print(diamond)
    for x in range (0,n-i,1): 
        print(spasi)
    print("\n")