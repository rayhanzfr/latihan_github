def int_or_not():
    userinput=(input("Masukkan Inputan: "))
    if userinput.isdigit()==True:
        print("INTEGER")
        return " "
    elif userinput.isalnum():
        print("BUKAN INTEGER")
        return " "
    else:
        print("Masukkan yang bener")
        return int_or_not()
print(int_or_not())