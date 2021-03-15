
list1 = []
list2 = []

total = int(input("Please enter the total number of each list element: "))
for _ in range(total):
    list1.append(int(input(f"Please enter element-{_} of List 1: ")))
    list2.append(int(input(f"Please enter element-{_} of List 2: ")))

addition = [a + b for a,b in zip(list1, list2)]
subtraction = [a - b for a,b in zip(list1, list2)]
division =[a / b for a,b in zip(list1, list2)]
multiplication = [a * b for a,b in zip(list1, list2)]
modulus = [a % b for a,b in zip(list1, list2)]

print("")
print(f"Addition       : {addition}")
print(f"Subtraction    : {subtraction}")
print(f"Division       : {division}")
print(f"Multiplication : {multiplication}")
print(f"Modulus        : {modulus}")