#menukar huruf pertama
#x= str (input('Masukkan kata apa saja:'))
#y= str (input('Masukkan kata apa saja:'))

#tukar1=x.replace(str(x[0]), str(y[0]))
#tukar2=y.replace(str(y[0]), str(x[0]))
#gabungan=tukar1,tukar2
#print(str(gabungan))

a = input('Masukan huruf : ')
b = input('Masukan huruf : ')

new_a = b[:2] + a[2:]
new_b = a[:2] + b[2:]
hasil = new_a + ' ' + new_b
print (hasil)
