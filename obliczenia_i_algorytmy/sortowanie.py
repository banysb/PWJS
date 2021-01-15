import random

tab = []
for i in range(0, 50):
    tab.append(random.randint(1,1000))

tab1 = tab.copy()

def my_sort(array):
    n = len(array)
    for i in range(0, n):
        start_index = i
        for j in range(i+1, n):
            if array[start_index] > array[j]:
                start_index = j
        array[i], array[start_index] = array[start_index], array[i]
    return array

my_sort(tab)
tab1.sort()
print(tab)
print(tab1)
if(tab == tab1):
    print("Tablice takie same")
else:
    print("Blad")
