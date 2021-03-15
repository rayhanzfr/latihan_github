def inputan(data_list):
	temp_list=list(i for i in input("Masukkan Angka : ").split(','))
	y=[int(j) for j in temp_list]
	return y
def asc(data_list,inputan):
	sorted_list = []
	while inputan:
		minimum = inputan[0]  # arbitrary number in list 
		for x in inputan:
			if x < minimum:
				minimum = x
		sorted_list.append(minimum)
		inputan.remove(minimum)
	return sorted_list
data_list=[]
# print(inputan(data_list))
print("Nilai Terurut: ",asc(data_list,inputan(data_list)))
# n=(int(input("masukkan banyak input: ")))
# for i in range (n):
# 	x=int (input("data ke-%d:"%(i+1)))
# 	data_list.append(x)
# new_list=data_list.copy()