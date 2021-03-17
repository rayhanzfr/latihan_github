# Write a function that accepts a list of 10 integers (between 0 and 9), that returns a string
# of those numbers in the form of a phone number (10 points).

def create_phone_number(number):
    a=""
    b=""
    c=""
    for i in number:
        if i==number[0] or i==number[1]  or i==number[2]:
            a+=i
        elif i==number[3] or i==number[4] or i==number[5]:
            b+=i
        else:
            c+=i
    print("({}) {}-{}".format(a,b,c))
x=input("Masukkan angka:").split(",")
create_phone_number(x)