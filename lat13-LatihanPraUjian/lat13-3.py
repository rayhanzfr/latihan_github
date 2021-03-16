for i in range(0,7):
    for j in range(0,5):
        if (i==0 and (j==0 or j==4)) or (i==1 and (j==0 or j==4)) or (i==5 and (j==0 or j==4)) or (i==6 and (j==0 or j==4)):
            print("*",end="")
        elif (i==2 and (j==1 or j==3)) or (i==4 and (j==1 or j==3)):
            print("*", end="")
        elif i==3 and j==2:
            print("*",end="")
        else:
            print(end=" ")
    print(" ")
            
