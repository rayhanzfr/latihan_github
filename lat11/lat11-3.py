# p0=penduduk awal
# p=penduduk akhir
# aug=penambahan penduduk asing pertahun
# percent=persentase pertumbuhan penduduk pertahun
# logic: 1year = p0+p0*percent+aug
def nbYear(p0, percent, aug, p):
	year= 0
	while p0 < p:
		p0 = p0 + (p0*percent/100) + aug
		year+=1
	if p0 >= p:
		return year
	return year

print("Banyaknya tahun yang dibutuhkan: {}".format(nbYear(1000, 2, 50, 1200)))
print("Banyaknya tahun yang dibutuhkan: {}".format(nbYear(1200, 2, 50, 1000)))
print("Banyaknya tahun yang dibutuhkan: {}".format(nbYear(1500, 5, 100, 5000)))
print("Banyaknya tahun yang dibutuhkan: {}".format(nbYear(1500000, 2.5, 10000, 2000000)))