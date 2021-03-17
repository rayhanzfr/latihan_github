def multTable(row,col) :
    for r in range(1, row+1) :
        for c in range(1, col+1) :
            print("%d " % (r*c), end="")
 
        print()
print(multTable(5,3))