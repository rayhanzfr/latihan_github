##mengubah semua huruf yang sama dengan huruf pertama selain huruf pertama diubah menjadi $

x= str (input('Masukkan kata apa saja:'))

#mytable = x.maketrans(str (x[0]),'$')
cek=x[0]
final=x.replace(cek,'$')
final=cek+final[1:]
#print(x[0]+x[1:].translate(mytable))
print(final)
