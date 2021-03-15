def inputan():
	x= list(int(i) for i in input("Masukkan Angka : ").split())
	for i in x:
		if i>9:
	# while x > 9:
			x = int(input('Masukkan angka: '))
	return x
def gambar(l):
	y=inputan()
	for x in y:
		if x==0:
			print(l[0][0])
			print(l[1][0]+" "+l[1][2])
			print(l[2][0]+l[2][1]+l[2][2])
		if x==1:
			print("  "+l[1][2])
			print("  "+l[2][2])
		if x==2:
			print(l[0][0])
			print("  "+l[1][1]+l[1][2])
			print(l[2][0]+l[2][1])
		if x==3:
			print(l[0][0])
			print("  "+l[1][1]+l[1][2])
			print("  "+l[2][1]+l[2][2])
		if x==4:
			print(l[1][0]+l[1][1]+l[1][2])
			print("   "+l[2][2])
		if x==5:
			print(l[0][0])
			print(l[1][0]+l[1][1])
			print("  "+l[2][1]+l[2][2])
		if x==6:
			print(l[0][0])
			print(l[1][0]+l[1][1])
			print(l[2][0]+l[2][1]+l[2][2])
		if x==7:
			print(l[0][0])
			print("   "+l[1][2])
			print("   "+l[2][2])
		if x==8:
			print(l[0][0])
			print(l[1][0]+l[1][1]+l[1][2])
			print(l[2][0]+l[2][1]+l[2][2])		
		if x==9:
			print(l[0][0])
			print(l[1][0]+l[1][1]+l[1][2])
			print("  "+l[2][1]+l[2][2])	
	return ""
l=[
	['  _  ']
	,[' |','_','| ']
	,[' |','_','|']
	]

print(gambar(l))
# print(l[0][0])
# print(l[1][0]+l[1][1]+l[1][2])
# print(l[2][0]+l[2][1]+l[2][2])

# pl = [  [ ' ','___', '' ]
#   ,     [ '|','___','|']
#   ,     [ '|','___','|']]

# # for i in pl:
# #     for j in i:
# #         print(j)

# def inputan():
#     x = int(input('Masukkan angka: '))
#     while x > 9:
#         x = int(input('Masukkan angka: '))
#     return x


# def bikin(pl):
#     x = inputan()
#     if x == 0:
#         pl[1][1] = '   '
#     elif x == 1:
#         pl[1][1:5] = ' '
#         pl[2][1:5] = ' '
#         pl.remove(pl[0])
#     elif x == 2:
#         pl[1][0] = ' '
#         pl[2][2] = ' '
#     elif x == 3:
#         pl[1][0], pl[2][0] = ' ', ' '
#     elif x == 4:
#         pl[2][0] = ' '
#         pl[2][1] =  '   '
#         pl.remove(pl[0])
#     elif x == 5:
#         pl[1][2] = ' '
#         pl[2][0] = ' '
#     elif x == 6:
#         pl[1][2] = ' '
#     elif x == 7:
#         pl[1][0], pl[1][1] =  ' ', '   '
#         pl[2][0], pl[2][1] = ' ', '   '
#     elif x == 8:
#         return pl
#     elif x == 9:
#         pl[2][0] = ' '
#     return pl

# def main(pl):
#     x = bikin(pl)
#     for i in x:
#         j = ''.join(i)
#         print(j)

# main(pl)


