def find_short(data):
    x = len(data[0])
    for i in data:
        if len(i)<x:
            x=len(i)
    return x
data=list(input("Masukan data: ").split(" "))
print(find_short(data))
#done