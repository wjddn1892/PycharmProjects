def gcd(m, n):
    if m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n

class Fraction:
    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom
    def __str__(self):
        return str(self.top) + "/" + str(self.bottom)
    def show(self):
        print(self.top, "/", self.bottom)
    def __add__(self, otherFraction):
        newtop = self.top * otherFraction.bottom + self.bottom * otherFraction.top
        newbottom = self.bottom * otherFraction.bottom
        common = gcd(newtop, newbottom)
        return Fraction(newtop // common, newbottom // common)
    def __sub__(self, otherFraction):
        newtop = self.top * otherFraction.bottom - self.bottom * otherFraction.top
        newbottom = self.bottom * otherFraction.bottom
        common = gcd(newtop, newbottom)
        return Fraction(newtop // common, newbottom // common)
    def __mul__(self, otherFraction):
        newtop = self.top * otherFraction.top
        newbottom = self.bottom * otherFraction.bottom
        common = gcd(newtop, newbottom)
        return Fraction(newtop // common, newbottom // common)

a = Fraction(3, 5)
b = Fraction(5, 7)
a.show()
b.show()