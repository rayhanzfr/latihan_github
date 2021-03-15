# class purwadhika:
# 	nilaiUjian=10

# Bandung=purwadhika
# Bandung.siswa1= "Fana"
# Bandung.siswa2="Ivan"
# Siswa1="Lidya"
# print(Bandung)#Menyatakan "Bandung" itu apa
# print(Bandung.nilaiUjian)
# print(Bandung.siswa1)
# print(Bandung.siswa2)
# print(Siswa1)
# print(type(Bandung.siswa1))
# print(type(Siswa1))
# manusia1=Manusia('Rayhan',24)
# manusia2=Manusia('Ryan',24)


# class Manusia:
# 	def __init__(self,name,age):
# 		self.nama=name
# 		self.umur=age
# 	def kenalan(self,katakata):
# 		print("Halo nama saya {} Umur {}, {}".format(self.nama, self.umur,katakata))
# 	def kenalan1(self):
# 		print("Halo nama saya {} Umur {}".format(self.nama, self.umur))
# 	def kenalan2(self,Angka):
# 		x=self.umur+10
# 		return x

# manusia1=Manusia("Rayhan",24)
# manusia1.kenalan('kamu dimana dengan siapa')
# manusia2=Manusia("WW",23)
# manusia2.kenalan1()
# print("Umur sebenarnya adalah: ",manusia2.kenalan2(25))
# print(manusia1)
# print(manusia1.nama)
# print(manusia2.nama)
# print(manusia1.__dict__)
# kamus_S1=manusia1.__dict__
# print(kamus_S1.values())

class HeroML:
	# banyak=0 			#Class Var
	def __init__(self,name,AP,AS,armor,defend,HP):
		self.nama=name #Instance Var
		self.attpow=AP
		self.attspd=AS
		self.armor=armor
		self.defend=defend
		self.darah=HP  #Instance Var
	def serang(self,musuh):
		print(self.nama, "sedang menyerang",musuh.nama)
		musuh.diserang(self,self.attpow)
		# print("Sisa HP",self.nama,":",self.darah,"karena diserang",musuh.nama)
	def diserang(self,musuh,attpow_lawan):
		print(self.nama, "sedang diserang",musuh.nama)
		Damage=attpow_lawan-self.armor
		self.darah-=Damage
		print("Total Damage dan HP {}: {} dan {}".format(self.nama,str(Damage),str(self.darah)))
hero1=HeroML("Guin",100,100,3,10,2000)
hero2=HeroML("Lunox",200,90,2,8,1900)
print(hero1.__dict__)
print(hero2.__dict__)

hero1.serang(hero2)
# hero2.diserang(hero1)


