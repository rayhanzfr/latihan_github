baris=int(input("Banyaknya baris: "))
bahan=""
x=baris
while baris>=0:
	spasi=baris
	while spasi>0:
		bahan=bahan+"   "
		spasi = spasi-1
	kiri=1
	while kiri<(x-(baris-1)):
		bahan=bahan+" * "
		kiri=kiri+1
	kanan=1
	while kanan<kiri-1:
		bahan=bahan+" * "
		kanan=kanan+1
	bahan =bahan+"\n"
	baris=baris-1
print(bahan)