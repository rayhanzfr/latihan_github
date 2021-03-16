# ori=input("Masukan data: ").split(",")
# ori=list(map(int, ori))
ori=list(int(i) for i in input("Masukan data: ").split(","))
pembagi=int(input("Masukkan Pembagi: "))
hasil=[]
x=0
for i in ori:
    x+=1
    if x<len(ori):
        hasil.append((i+ori[x])/pembagi)
print("Original List:\n",ori)
print("Hasil perubahan list:\n",hasil)