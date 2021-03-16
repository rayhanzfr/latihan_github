def int_or_not():
    userinput=(input("Masukkan Inputan: "))
    userinput=userinput.strip()
    userinput=userinput.replace(" ","")
    if userinput.isalnum():
        if userinput.isdigit():
            print("INTEGER")
            return " "
        else:
            print("BUKAN INTEGER")
            return " "
    else:
        print("Masukkan input yang benar")
        return int_or_not()
print(int_or_not())