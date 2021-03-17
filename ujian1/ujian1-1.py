# it must start with a hastag(#) 
# all words must have their first letter capitalized
# if the final result is longer than 140 chars it must return False
# if the input or the result is an empty string it must return False
def Hashtag(string):
    a=""
    if len(x)>0 and len(x)<=140:
        string=string.split(" ")
        for i in string:
            i=i.capitalize()
            a+=i
        print("#"+a)
    else:
        print(False)
x=input("Masukkan kata: ")
Hashtag(x)