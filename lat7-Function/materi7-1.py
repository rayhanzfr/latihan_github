# def iniFungsi(a,b):#->>>parameter
# 	c=a+b
# 	return c
# def iniKali():
# 	z=iniFungsi(10,11)*10
# 	return z
# a=float(input(""))
# b=float(input(""))
# print(iniFungsi(1,2))#->>>callback with argumen
# print(iniKali())


# ##Function without input and output
# def salam():
# 	print('Selamat datang')
# 	print("Semoga harimu menyenangkan")
# salam()
# ##Function with input but without output
# def data(a,b):
# 	print("Nama saya adalah {} dan saya berumur {}".format(a,b))
# a=input("Masukkan nama:\t")
# b=input("Usia:\t")
# data(a,b)


# #Default Parameter
# def salaam(nama='Unknown',usia=0):
# 	if (nama=='Unknown' and usia>0):
# 		print("Saya berusia {}".format(usia))
# 	elif(nama!='Unknown' and usia ==0):
# 		print("Hello nama saya {}".format(nama))
# 	elif(nama!='Unknown' and usia>0):
# 		print("Hello nama saya {}, dan usia saya {}".format(nama,usia))
# salaam(usia=25)
# salaam("Asep")
# salaam("Tatang",20)


# #Function With Input And Output
# def tambah(angka1,angka2):
# 	return angka1+angka2
# hasil=tambah(5,4)
# print(hasil)
# print(tambah(10,2))

# Local vs Global Variable
# x=5				#->global
# def coba():
# 	j=2				#->j local variable
# 	print(x+2)