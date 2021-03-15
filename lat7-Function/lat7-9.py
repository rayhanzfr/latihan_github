def evenfunc(a):
	if a%2 == 0:
		return "even"
	else:
		return "odd"
num=list(int (i) for i in input("Masukkan Angka : ").split(','))
# samples = [int(j) for j in num]
num1=list(map(lambda x: x*3,num))
print(num1)
print(list (map(evenfunc,num)))#argument: 1,2,3,4