from os import path

if(path.exists("haslo.txt") == False):
    code = open("haslo.txt", 'w+')
    code.write(input("Podaj nowy kod: "))
    code.close()

else:
    code = open("haslo.txt", 'r')
    x = code.readline()
    code.close()

code_new = input("Podaj kod: ")

if(code_new == x):
    print("Kod poprawny")
else:
    print("Kod niepoprawny")