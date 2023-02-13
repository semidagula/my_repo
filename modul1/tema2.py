# 1. Explica cu cuvintele tale in cadrul unui comentariu cum functioneaza un if else: Daca conditia este indeplinita atunci codul este executat, un if are nevoie de un else.
# 2  Verifica si afiseaza daca x este numar natural sau nu (un numar se considera natural


x = int(input('Alege un numar: '))
x_natural = x > 0
if x > 0:
    print('X este numar natural ')
else:
    print('X nu este nr natural ')

# 3. Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru
x = int(input('Alege un numar: '))
if x > 0:
    print('X este un numar pozitiv ')
elif x < 0:
    print('X este un numar negativ ')
else:
    print('X este un numar neutru ')

# 4. Verifica si afiseaza daca x este intre -2 si 13 (incluzand captele de interval).
a = int(input('Alege un numar: '))
if -2 <= a <= 13:
    print('true')
else:
    print('False')

# 5. Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5 (diferenta inseamna
# cate numere sunt intre x si y, nu rezultatul diferentei intre x si y). Hint: Se va folosi functia
# abs#
x = int(input('alege un nr: '))
y = int(input('alege al 2 lea nr : '))
if abs(x - y) < 5:
    print('True')
else:
    print('False')

# 6. Verifica daca x NU este intre 5 si 27, incluzand capetele de interval. (a se folosi ‘not’)
x = int(input('Enter a number : '))
is_not_between = x not in range(5, 27)
print(is_not_between)

# 7. Declara o noua variabila y de tip int si apoi verifica si afiseaza daca x si y sunt egale,
# daca nu, afiseaza care din ele este mai mare
y = int(input('y = '))
x = int(input('X = '))
if y == x:
    print('True')
elif x > y:
    print('x > y')
else:
    print('y < x')

# 8. Presupunand ca x, y, z (toate de tip int) - reprezinta laturile unui triunghi, afiseaza daca
# triunghiul este isoscel (doua laturi sunt egale), echilateral (toate laturile sunt egale) sau
# oarecare (nicio latura nu e egala).

p = int(input('Latura 1 : '))
r = int(input('Latura 2 : '))
s = int(input('Latura 3 : '))

if p == r and r != s or p == s and s != r or s == r and p != s:
    print('Triunghiul este isoscel. ')
elif p == r and p == s and s == r:
    print('Triunghiul este echilateral. ')
else:
    print(' Triunghiul este oarecare. ')

# 9. Citeste o litera de la tastatura apoi verifica si afiseaza daca este vocala sau nu. Atentie!
# Trebuie sa evaluati si cazurile uppercase si cazurile lowercase.
vocale = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
litera = str(input('Introduceti o litera : '))

vocale_in_litera = []

for char in litera:
    if char in vocale:
        print(f'{char} este o vocala. ')

        if char not in vocale:
            vocale_in_litera.append(char)
    else:
        print(f'{char} nu este o vocala')

# 10. Transforma si printeaza notele din sistem românesc in sistem american dupa cum
# urmeaza:
# a. Peste 9 => A
# b. Peste 8 => B
# c. Peste 7 => C
# d. Peste 6 => D
# e. Peste 4 => E
# f. 4 sau sub => F


nota = int(input('Introduceti nota :'))
if 0 <= nota <= 4:
    print('Nota F')
elif 4 < nota <= 5:
    print('Nota E')
elif 5 < nota <= 6:
    print('Nota D')
elif 6 < nota <= 7:
    print('Nota C')
elif 7 < nota <= 8:
    print('Nota B')
elif 8 < nota <= 10:
    print('Nota A')
else:
    print('Nota invalida')

# 1. Verifica daca x are minim 4 cifre (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
no = input('Enter a 4 digits number : ')
length = len(no)
print(length)
if length / 4 == 1:
    print('No are 4 digits')
else:
    print('No are mai mult de 4 cifre')

# 2. Verifica daca x are exact 6 cifre
x = input('Enter a 6 digits number : ')
length = len(x)
print(length)
if length / 6 == 1:
    print('No are 6 digits')
else:
    print('No nu are exact 6 cifre')

# 3. Verifica daca x este numar par sau impar
numar = int(input('Enter a number :'))
if (numar % 2) == 0:
    print("{0} is even number".format(numar))
else:
    print("{0} is odd number".format(numar))

# 4. Avand trei variabile x, y, z (toate int) afiseaza in consola care este cel mai mare dintre
# ele
x = 2
y = 5
z = 8
print(max(x, y, z))

# 5. Presupunand ca x, y, z - reprezinta unghiurile unui triunghi, verifica si afiseaza daca
# triunghiul este valid sau nu (un triunghi este valid daca suma tuturor unghiurilor este de
# 180 de grade sau daca suma lungimilor a oricare doua laturi este mai mare decat
# lungimea celei de-a treia laturi)

x = 150
y = 40
z = 20
sum = x + y + z
print(sum)

if sum == 180:
    print('Valid')
else:
    print('False')

# 6. Avand stringul: 'Coral is either the stupidest animal or the smartest rock' citește de
# la tastatura un număr x de tip int și afișează stringul fără ultimele x caractere. ex: dacă
# ați ales 7 se va afisa urmatorul string: 'Coral is either the stupidest animal or the
# smarte'
string = 'Coral is either the stupidest animal or the smartest rock'
len(string)
x = 10
string_nou = string[:10]
print(string_nou)

# 7. Folosindu-te de același string de la exercițiul 6, declara un string nou care sa fie format
# din primele 5 caractere + ultimele 5
string = 'Coral is either the stupidest animal or the smartest rock'[:5]
string_last_five = 'Coral is either the stupidest animal or the smartest rock'[-5:]
print(string + string_last_five)

# 8. Folosindu-te de același string de la exercițiul 6, salvează într-o variabila și afiseaza
# indexul de start al cuvântului rock - adică poziția in string la care începe cuvântul rock
# (hint: este o funcție care te ajuta sa faci asta). Folosind aceasta variabila + slicing,
# afișează tot stringul pana la acest cuvant. Output asteptat: 'Coral is either the stupidest
# animal or the smartest '

string = 'Coral is either the stupidest animal or the smartest rock'
print(string[:-5])

# 9. Citeste de la tastatura un string si verifica daca primul și ultimul caracter sunt la fel. Se
# va folosi un assert. Atentie: se dorește ca programul sa fie case insensitive, adica 'apA'
# e acceptat ca un string in care primul si ultimul caracter este la fel (hint, te poti folosi de o
# functie pentru a face string-ul case insensitive

prop = input('Introduceti o prop: ')
assert prop.casefold()[:1] == prop.casefold()[-1:]

# 10. Avand stringul '0123456789' afiseaza doar numerele pare si apoi doar numerele impare
# (hint: foloseste slicing si controleaza afisarea in slicing cu slicing step)
numbers = '0123456789'
print(numbers[::2], numbers[1::2])
