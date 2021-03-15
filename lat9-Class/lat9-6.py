class Tinju:
	def __init__(self, name, power,hp):
		self.name = name
		self.power = power
		self.hp= hp

	def serang(self, musuh):
		print("{} sedang menyerang {} dengan power {}".format(self.name,musuh.name,self.power))
		musuh.diserang(self,self.power)

	def diserang(self,musuh,power_lawan):
		print("{} sedang diserang {} dengan HP {}".format(self.name,musuh.name,self.hp))
		damage=power_lawan
		self.hp-=damage
		if self.hp>0:
			print("{} menyerang balik dengan power {}".format(self.name,self.power))
			print()
			musuh.diserang(self,self.power)
		elif self.hp<=0:
			print("Total Damage dan HP {}: {} dan {}".format(self.name,str(damage),str(self.hp)))
			print("{} menang".format(musuh.name))

char1=Tinju("A",10,1000)
char2=Tinju("B",10,1000)

char1.serang(char2)
