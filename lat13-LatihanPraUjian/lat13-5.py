def seleksi(mydata,n):
    selection=[]
    indexing=[]
    ind=0
    for i in mydata:
        if (i>=n):
            selection.append(i)
            indexing.append(ind)
        ind+=1
    print("\nElemen Pada List yang lebih besar dari 1500 Terdapat Pada Index\n{}\n".format(indexing))
    return selection
mydata=list(input("Masukan data: ").split(","))
mydata=list(map(int, mydata))
print("\nOriginal List: \n{}".format(mydata))
n=int(input("Masukkan angka batas: "))
print("Nilai Dari Index Tersebut adalah: \n{}".format(seleksi(mydata,n)))