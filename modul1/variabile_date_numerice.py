x = 3
# int x = 3
print(x)
print(type(x))
y = 3.0
print(y)
print(type(y))
x = float(x)
print(x)
print(type(x))

# Operatii aritmetice:
# Adunare:            3 + 2
# Scadere:            3 - 2
# Inmultire: 		  3 * 2
# Impartire:          3 / 2
# Impartire intreaga: 3 // 2
# Ridicare la putere: 3 ** 2
# Modulo:             3 % 2

print(3 + 2)
print(3 -2)
print(3 * 2)
print(3 / 2)
print(type(3/2))
print(3 // 2)
print(3 // 2.0)
print(3 ** 2)
print(3 % 2)
print(4 % 2)

# functii build in
# abs()
# pow()
# round()
# min()
# max()

print(abs(-4))
abs_value = abs(-3)
print(abs_value)

print(pow(3,2))

print(round(3.43))
print(round(3.56))
print(round(3.48,1))

print(min(3, 2))
print(max(3,1,2,4,7,8))


# Comparatii:

# Egal:               3 == 2
# Diferit:            3 != 2
# Mai mare:           3 > 2
# Mai mic:            3 < 2
# Mai mare sau egal:  3 >= 2
# Mai mic sau egal:   3 <= 2

print(3 == 2)
x = 3
y = 3.0
print(type(x) == type(y))



# Aplicatie


from math import sqrt as radical

a = int(input('Prima latura a triunghiului: '))
b = int(input('A doua latura a triunghiului: '))
c = int(input('A treia latura a triunghiului: '))
perimetrul = a + b + c
print('perimetrul este: ', perimetrul)
p = (a + b + c)/2
aria = radical(p*(p-a)*(p-b)*(p-c))
print("aria este: ", aria)
h = 2*aria/b
print('inaltimea este: ', h)