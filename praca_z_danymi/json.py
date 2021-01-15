import json
import os

def openFile(path):
    if os.path.isfile(path):
        with open(path, "r") as file:
            return json.load(file)
    else:
        return []

def printData(data):
    for i in range(0, len(data)):
        print("\n" + str(i+1)+".")
        print("name:", data[i]["name"])
        print("surname:", data[i]["surname"])
        print("year:", data[i]["year"])

def add():
    print("\n")
    name = input("name: ")
    surname = input("surname: ")
    year = input("year: ")

    record = {"name": name, "surname": surname, "year": year}
    return record


def remove():
    print("\n")
    n = int(input("\t" + "Podaj numer do usuniecia: "))
    return n-1

def saveFile(data, path):
    with open(path, "w") as file:
        json.dump(data, file, indent=4)


path = "files/file.json"
data = openFile(path)

while(1):
    printData(data)
    print("\nWybierz opcję: ")
    print("1. Dodaj pozycję")
    print("2. Usuń pozycję")
    print("3. Zakończ")
    x = float(input("Podaj numer: "))
    if x == 1:
        data.append(add())
    elif x == 2:
        data.pop(remove())
    elif x == 3:
        print("Zamykam program")
        break
    saveFile(data, path)


