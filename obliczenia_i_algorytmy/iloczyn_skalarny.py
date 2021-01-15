a = [1, 2, 12, 4]
b = [2, 4, 2, 8]

#ręczne obliczenia
wynik = 0
for i in range(0, 4):
    wynik += a[i]*b[i]
print(wynik)

#funckja do obliczania iloczynu skalarnego dla dowolnych wektorów
def iloczyn_skalarny(x, y):
    return sum(x[i]*y[i] for i in range(len(x)))
print(iloczyn_skalarny(a, b))