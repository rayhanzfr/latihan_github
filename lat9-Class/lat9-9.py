class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def luas(self):
        return self.length * self.width

    def keliling(self):
        return 2 * self.length + 2 * self.width
class Square(Rectangle):
    def __init__(self, length,width):
        super().__init__(length, length)
class Cube(Square):
    def luas_permukaan(self):
        l_alas = super().luas()
        return l_alas * 6

    def volume(self):
        vol = super().luas()
        return vol * self.length
a=10
b=20
kubus=Cube(a,b)
persegi=Square(a,b)
persegi_panjang=Rectangle(a,b)

print("Luas Permukaan dan Volumenya adalah: {} dan {}".format(kubus.luas_permukaan(),kubus.volume()))