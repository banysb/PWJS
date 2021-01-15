import math as m

class complex:

    real = 0
    imag = 0

    def __init__(self, re, im):
        self.real = re
        self.imag = im

    def __add__(self, other):
        return complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return complex(self.real*other.real-self.imag*other.imag, self.real*other.imag+self.imag*other.real)

    def mag(self):
        return m.sqrt(self.real**2+self.imag**2)

    def ang(self):
        return m.atan2(self.imag, self.real)

    def print(self):
        if self.imag>0:
            print(str(self.real), ' + ', str(self.imag), 'i')
        elif self.imag == 0:
            print(str(self.real))
        else:
            print(str(self.real), '-', str(abs(self.imag)), 'i')
