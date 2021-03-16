def persistence(n):
    x=str(n)
    r=0
    while len(x)!=1:
        deltaN = 1
        for n in x:
            deltaN *= int(n)
        x=str(deltaN)
        r+=1
    return r
n=int(input("Masukkan Angka: "))
final = persistence(n)
print (final)
#done