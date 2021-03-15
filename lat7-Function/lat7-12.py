def sort_ganjil(data):
    l = []
    #while akan jalan selama list awal belom kosong
    while len(data) !=0:

        #cari angka terkecil di list
        data = [int(i) for i in data]
        m = min(data)
        #append ke list kosong
        l.append(int(m))
        
        #remove angka terkecil dari list awal
        data.remove(m)
    return  l
    
def sort_genap(data):
    l = []
    #while akan jalan selama list awal belom kosong
    while len(data) !=0:

        #cari angka terbesar di list
        data = [int(i) for i in data]
        m = max(data)
        #append ke list kosong
        l.append(int(m))
        
        #remove angka terbesar dari list awal
        data.remove(m)
    return  l

def pisah(data):
    # intialise list
    l = []
    l2 = []
     
    for i in range(len(data)):
        if data[i] % 2 != 0:
            l.append(data[i]) 
        else:
            l2.append(data[i])
    return  l,l2


def main(x):  
	x = x.split(',')
	x = [int(i) for i in x]
	x.sort()

	#proses pemisahan odd even
	i,j = pisah(x)

	#proses sorting
	ev = sort_genap(j)
	od = sort_ganjil(i)

	#jadiin satu list
	res = od + ev
	print(res)
    
main(input('masukkan angka: '))