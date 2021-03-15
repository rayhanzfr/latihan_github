def kali(a,b):
	z=a*b
	return z
def pangkat(a,b):
	z=b**a
	return z
def hasil(fungsi, nilai1,nilai2):
	result=fungsi(nilai1,nilai2)
	return result

print(hasil(kali,10,2))
print(hasil(pangkat,10,2))

def evenfunc(a):
	if a%2 == 0:
		return "even"
	else:
		return "odd"
num=list(int (i) for i in input("Masukkan Angka : ").split(','))
num1=list(map(lambda x: x*3,num))
print(num1)
print(list (map(evenfunc,num)))#argument: 1,2,3,4