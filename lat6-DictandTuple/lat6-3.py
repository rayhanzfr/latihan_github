set1={item for item in input("Masukkan 5 Film Kesukaan anda dipisahkan dengan koma : ").split(',')}
set2={item1 for item1 in input ("Masukkan 5 Film Kesukaan teman anda dipisahkan dengan koma : ").split(',')}

set3=set1.intersection(set2)
n=len(set3)*100*2/(len(set1)+len(set2))

print(set3)
print('%',n)