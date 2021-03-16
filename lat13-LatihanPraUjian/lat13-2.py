def validasi(x):
    low=0
    up=0
    special=0
    numerik=0
    if (6<=len(x)<=16): 
        for i in x: 
            if (i.islower()): 
                low+=1            
            if (i.isupper()):
                up+=1            
            if(i=='@' or i=='#' or i=='$' ): 
                special+=1            
            if (i.isdigit()):
                numerik+=1            
    if (low>=1 and up>=1  and numerik>=1 and special>=1 and low+up+numerik+special==len(x)): 
        print("Valid Password\nPassword yang dimasukan adalah: {}".format(x)) 
    else: 
        print("Invalid Password") 
x = input("Masukkan Password: ")
validasi(x)