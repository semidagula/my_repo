# extragem din lista mare "_",  ultimul 6, 2 din mijloc (putem folosi if si count)


lista_1 = [1, 2, 3, 4, 5, 6]
lista_2 = ["apple", "mac", "iphone", "ipad", "apple"]
lista_3 = [1, True, "_", False, 5.2]
lista_matrice = [lista_1, lista_2, lista_3]
lista_mare = [lista_matrice, [0, 1, lista_1], ['a', 'b', 'c'], [lista_matrice], {}, True]

# extras 2 din mijloc
x = int((len(lista_mare) / 2) - 1)
print(x)
print(f'eliminam {x} din lista_mare')
# extras ultimul6
print(lista_mare[0][0][-1])
# extras '_'
print(lista_mare[0][-1][2])

lista_2 = ["apple", "mac", "iphone", "ipad", "apple"]
count = len([lista_2.count(item) for item in lista_2])
print(count)
