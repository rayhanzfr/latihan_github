import math
x = float (input('Masukan nilai X:'))
y = float (input('Masukan nilai Y:'))
z = float (input('Masukan nilai Z:'))
w=math.pow((x+y*z)/(x*y),z)
print('nilai W adalah ',math.ceil(w))