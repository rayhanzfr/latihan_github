iniDictionary={
	'nama' : 'Budi',
	'usia' : 40,
	'pekerjaan:': 'Data Analyst',
	'jenis Kelamin': 'Laki-Laki',
	'nama2':'Budi'
}
x=set(iniDictionary.values())
print(x)

x.add('futsal')
print(x)
x.remove('futsal')
print(x)