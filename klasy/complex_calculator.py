from complex_class import complex
def main():
    print("***Kalkulator liczb zespolonych***")
    re1 = float(input("Podaj część rzeczywistą pierwszej liczby: "))
    im1 = float(input("Podaj część urojona pierwszej liczby: "))

    re2 = float(input("Podaj część rzeczywistą drugiej liczby: "))
    im2 = float(input("Podaj część urojona drugiej liczby: \n"))

    c1 = complex(re1, im1)
    c2 = complex(re2, im2)

    print("Pierwsza liczba: ")
    c1.print()
    print("\n")
    print("Druga liczba: ")
    c2.print()
    print("\n")
    ans = float(input("Wybierz operację:\n1. Dodawanie\n2. Odejmowanie\n3. Mnożenie\n4. Moduł\n5. Faza"))
    if ans == 1:
        (c1+c2).print()
    if ans == 2:
        (c1-c2).print()
    if ans == 3:
        (c1*c2).print()
    if ans == 4:
        print("Moduł pierwszej liczby: ", c1.mag())
        print("Moduł drugiej liczby: ", c2.mag())
    if ans == 5:
        print("Faza pierwszej liczby: ", c1.ang())
        print("Faza drugiej liczby: ", c2.ang())


if __name__ == '__main__':
    main()