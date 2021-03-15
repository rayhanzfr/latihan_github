iniList=[1,2,3,False,"Hai"]
iniList2=iniList.copy()
iniList2.reverse()
print(iniList)
print(iniList2)
# print(type(iniList))

# print(iniList[-4:-1])
# print(iniList[1:])
# print(iniList[:3])
# print(iniList[-4:3])
for baru in iniList2:
	print(baru)
gabungan=iniList+iniList2
print(gabungan)
iniList2[1:]='test'#[1, 't', 'e', 's', 't']
print(iniList2)
iniList2.append('coba')
print(iniList2)##[1, 't', 'e', 's', 't', 'coba']
iniList2.insert(0,'Hai')
print(iniList2)#['Hai', 1, 't', 'e', 's', 't', 'coba']
iniList2.remove('coba')
print(iniList2)# ['Hai', 1, 't', 'e', 's', 't']
iniList2.pop()
print(iniList2)# ['Hai', 1, 't', 'e', 's']
del iniList2[2]
print(iniList2)# ['Hai', 1, 'e', 's']
del iniList2[0:2]
print(iniList2)# ['e', 's']
iniList2.clear()