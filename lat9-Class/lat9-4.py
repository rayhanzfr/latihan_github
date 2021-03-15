class datadiri:
	# nama ,no induk, umur
	def __init__(self,nama,no,umur):
		self.nama=nama
		self.no=no
		self.umur=umur
	def prindiri(self):
		print("Nama Siswa Ini Adalah {}, Nomo Induk Siswanya yaitu {},Dan Umurnya Adalah {} Tahun".format(self.nama,self.no,self.umur))

diri1=datadiri("Arief","10001",21)
diri2=datadiri("Ariyanda","10002",23)
diri3=datadiri("Raihan","10003",20)
diri4=datadiri("Prisilia","10004",22)
diri5=datadiri("Farhan","10005",21)
diri1.prindiri()
diri2.prindiri()
diri3.prindiri()
diri4.prindiri()
diri5.prindiri()
x=(diri1.umur+diri2.umur+diri3.umur+diri4.umur+diri5.umur)/5
print("Rata Rata Umur Siswa di kelas ini adalah: ",x)

