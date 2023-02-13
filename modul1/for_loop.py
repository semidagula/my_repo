""" 1. declaram o lista ce contine doar numere, facem suma tuturor elementelor din lista prin 4 metode.functii cu for
cu while count.
    2. putin mai dificil: sa creem o alta lista cu elementele ce se gasesc de mai multe ori ___ gasim duplicatele dintr
     o lista  se face o lista noua in care se pun elementele dar unice.
    3. sortare  avem o lista cu deverse numere, si obtinem cel mai mare nr par.
    """
# 1
lista_nr = [2, 5, 8, 6, 3]
suma = sum(lista_nr)
print(suma)


# 2
def sum_of_list(l):
    total = 0
    for val in l:
        total = total + val
    return total
print("The sum of my_list is", sum_of_list(lista_nr))

# 3
total = 0
for nr in lista_nr:
    total += nr
    print(total)

# 4
total = 0
for i in range(0, len(lista_nr)):
    total = total + lista_nr[i]
print('', total)

# 2

my_list = ['Ana', 'Maria', 'Ioana', 'Ana', 2, 2, 45.2, 23, 48.1, 23, 45.2]
my_empty = []

for i in my_list:
    if i not in my_empty:
        my_empty.append(i)
    else:
        print(i)

# 3
lst = [6, 3, 8, 5, 7, 8, 2]
even = [x for x in lst if x % 2 == 0]
print("Largest odd number is ", max(even))
