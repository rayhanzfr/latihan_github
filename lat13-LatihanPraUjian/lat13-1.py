def penentuan():
    x=input("Masukkan huruf: ").lower()
    if len(x)==1 and x.isalnum():
        if x in"aiueo":
            print("Huruf '{}' termasuk ke dalam vokal".format(x))
        elif x in "0123456789":
            print("'{}' termasuk ke dalam angka. input ulang".format(x))
            return penentuan()
        else:
            print("Huruf '{}' termasuk ke dalam konsonan".format(x))
    else:
        print("Masukkan satu huruf aja")
        return penentuan()
penentuan()
