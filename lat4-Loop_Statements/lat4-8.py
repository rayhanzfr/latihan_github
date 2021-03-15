kata=str(input("Masukan sebuah kata/kalimat: "))
k=0
n=0
x=''
for i in kata:
    if i.isalpha():
        k=k+1
    elif i.isdigit():
        n=n+1
    else:
        continue
print(k,n)