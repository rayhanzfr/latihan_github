# def pindahNol(num, n): 
#     hitung = 0 
#     for i in range(n): 
#         if num[i] != 0:         
#             num[hitung] = num[i] 
#             hitung+=1
#     while hitung < n: 
#         num[hitung] = 0
#         hitung += 1

# num=list(int (i) for i in input("Masukkan Angka : ").split(','))
# n = len(num) 
# pindahNol(num, n) 
# print("hasil setelah:") 
# print(num)

class NOL:
    def __init__(self,inputan):
        self.awallist=inputan
        self.n=len(inputan)
    def pindahNol(self):
        self.listbaru = []
        self.listNol = []
        for i in range(self.n):
            if self.awallist[i] == 0 or self.awallist[i]=='0':
                if type(self.awallist[i])==type(False):
                    self.listbaru.append(self.awallist[i])
                else:
                    self.listNol.append(self.awallist[i])
            else:
                self.listbaru.append(self.awallist[i])
        return self.listbaru + self.listNol
# inputan=list(i for i in input("Input : ").split(','))
inputan=([False,1,0,1,'0',2,'0',1,'3','a'])
akhir=NOL(inputan) 
print("hasil setelah: {}".format(akhir.pindahNol()))















# def move_zeros(array):
#     #your code here
#     new = []
#     zeros = []
    
#     for i in range(len(array)):
#         if array[i] == 0 or array[i] == 0.0:
#             if type(array[i]) == int or type(array[i]) == float:
#                 zeros.append(array[i])
#             else: new.append(array[i])
#         else:
#             new.append(array[i])
    
#     return new + zeros
# print(move_zeros([1,2,0,1,0,1,0,3,0,1]), [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
# print(move_zeros([0,1,None,2,False,1,0]), [1, None, 2, False, 1, 0, 0])