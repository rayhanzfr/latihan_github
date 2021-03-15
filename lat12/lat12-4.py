print("Masukan Sisi Segitiga")
s1=(int(input("Sisi 1: ")))
s2=(int(input("Sisi 2: ")))
s3=(int(input("Sisi 3: ")))

if s1==s2==s3:
    print("Segitiga Sama Sisi")
elif s1==s2 or s1==s3 or s2==s3:
    print("Segitiga Sama Kaki")
else:
    print("Segitiga Sembarang")