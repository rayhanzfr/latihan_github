# You are given a list of integers. Your task is to sort odd numbers within the list in ascending
# order, and even numbers in descending order but keep all the odds or the evens number in
# the same index group (35 Points).
# Note that zero is an even number. If you have an empty list, you need to return it

def sort_odd_even(num):
    even=[i for i in num if i%2==0]
    odd=[i for i in num if i%2!=0]
    even.sort(reverse=True)
    odd.sort()
    index0=0
    index1=0
    even_index=[]
    odd_index=[]
    sorted=[]
    for i in range(len(num)):
        if num[i]%2==0:
            num[i]=even[index0]
            sorted.append(num[i])
            index0+=1
            even_index.append(i)
        else:
            num[i]=odd[index1]
            sorted.append(num[i])
            index1+=1
            odd_index.append(i)
    print("Even index: {}".format(even_index))
    print("Odd index: {}".format(odd_index))
    return sorted
x=list(int(i) for i in input("Masukan data: ").split(","))
print(sort_odd_even(x))

# [5,3,2,8,1,4]=[1,3,8,4,5,2]