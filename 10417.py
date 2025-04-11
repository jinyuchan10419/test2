class Complex:
    def __init__(self, r=0, i=0):
        self.r = r
        self.i = i

    def add(self, num):
        return Complex(self.r + num.r, self.i + num.i)
    
    def sub(self, num):
        return Complex(self.r - num.r, self.i - num.i)

    def mul(self, num):
        return Complex(self.r * num.r - self.i * num.i, self.r * num.i + self.i * num.r)

    def __str__(self):
        if self.i == 0:
            return str(self.r)
        elif self.i == 1:
            return str(self.r) + "+i"
        elif self.i == -1:
            return str(self.r) + "-i"
        else:
            return str(self.r) + "+" + str(self.i) + "i"

 
# a = Complex(1, 2) # 1+2i
# b = Complex(3, -1) # 3-i
# c = Complex()
# print(a)
# print(b)
# print(c)
# print(a.add(b))
# print(a.sub(b)) # -2+3i
# print(a.mul(b))
