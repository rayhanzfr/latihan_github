def find_short(s):
    panjang = len(s[0])
    for i in s:
        if len(i)<panjang:
            panjang=len(i)
    return panjang
s=list(input("Masukan data: ").split(" "))
print(find_short("Many people get up early in the morning"))
print(find_short("Every office would getting newest monitor"))
print(find_short("Create new file after this morning"))