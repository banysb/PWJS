import math as m
a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))

delta = (b * b) - (4 * a * c)
if delta <0:
    print("Brak miejsc zerowych.")
elif delta == 0:
    x0 = (-1) * b / (2 * a)
    print("Jeden pierwiastek: x = ", x0)
elif delta>0:
    sqrt_delta = m.sqrt(delta)
    x1 = ((-1) * b - sqrt_delta) / (2 * a)
    x2 = ((-1) * b - sqrt_delta) / (2 * a)
    print("Dwa pierwiastki: x1 = ",x1, "; x2 = ", x2)