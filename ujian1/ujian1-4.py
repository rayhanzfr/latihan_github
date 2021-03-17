def hollowTriangle(x):
    if x==1:
        print(" # ")
    else:
        for i in range(x-1):
            for j in range(i,x-1):
                print("_",end="")
            for j in range(2*i+1):
                if j==0 or j==2*i or i==x-1:
                    print("#",end="")
                else:
                    print("_",end="")
            for j in range(i,x-1):
                print("_",end="")
            print("")
        for i in range(2*x-1) : 
            print ('#', end = '') 
x=int(input("Masukkan bilangan: "))
hollowTriangle(x)