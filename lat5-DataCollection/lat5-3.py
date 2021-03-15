sorted_list = []
data_list=[]
n=(int(input("masukkan banyak input: ")))
for i in range (n):
	x=int (input("data ke-%d:"%(i+1)))
	data_list.append(x)
new_list=data_list.copy()
while new_list:
    minimum = new_list[0]  # arbitrary number in list 
    for x in new_list: 
        if x < minimum:
            minimum = x
    sorted_list.append(minimum)
    new_list.remove(minimum)    
print(data_list)
print(sorted_list)