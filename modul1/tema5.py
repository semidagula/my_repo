# 1.Funcție care să calculeze și să returneze suma a două numere
def sum(first_nr, second_nr):
    suma = first_nr + second_nr
    return suma


first_nr = int(input('Enter first_nr: '))
second_nr = int(input('Enter the second_nr: '))
print('Suma celor doua numere este: ', sum(first_nr, second_nr))


# 2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar

def even_odd(number):
    if number % 2 == 0:
        return True
    else:
        return False


print(even_odd(8))


# 3. Funcție care returnează numărul total de caractere din numele tău complet.(nume, prenume, nume_mijlociu)
def lun_char(nume, prenume):
    lun = len(nume + prenume)
    return lun


nume = input('Enter your name: ')
prenume = input('Enter your surname: ')
print('Lungimea caractreor din numele dv complet este: ', lun_char(nume, prenume))


# 4. Funcție care returnează aria dreptunghiului

def area_Rectangle(width, height):
    area = 2 * (width + height)
    return area


width = float(int(input('Enter the width of the Rectangle: ')))
height = float(int(input('Enter the height of the Rectangle: ')))
print('The area of the rectangle is ', area_Rectangle(width, height))

# 5. Funcție care returnează aria cercului
import math


def area_circle(Radius):
    area = Radius ** 2 * math.pi
    return area


Radius = float(input('Enter the radius of a circle: '))
print('The area of the circle is : ', area_circle(Radius))


# 6. Funcție care returnează True dacă un caracter x se găsește într-un string dat și False dacă nu găsește.

def char_x(String):
    if lit in String:
        return True
    else:
        return False


lit = input('Introuceti litera pe care doriti sa o verificati in string: ')
String = input('Introduceti o prop: ')
print(char_x(String))


# 7. Funcție fără return, primește un string și printează pe ecran:
# ● Nr de caractere lower case este x
# ● Nr de caractere upper case exte y

def upperlower(String):
    d = {'Upper_case': 0, 'Lower_case': 0}
    for i in String:
        if i.isupper():
            d['Upper_case'] += 1
        elif i.islower():
            d['Lower_case'] += 1
        else:
            pass
    print('Stringul este: ', String)
    print('Nr de upper : ', d['Upper_case'])
    print('Nr de lower : ', d['Lower_case'])


upperlower('ANA are MERE')


# 8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu numerele pozitive
def PrintEven(itr, list1):
    if itr == len(list1):
        return
    if list1[itr] >= 0:
        print(list1[itr], end=" ")
    PrintEven(itr + 1, list1)
    return


list1 = [-5, 7, -19, 10, 9]
PrintEven(0, list1)


# 9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
# ● Primul număr x este mai mare decat al doilea nr y
# ● Al doilea nr y este mai mare decat primul nr x
# ● Numerele sunt egale.

def num(x, y):
    if x > y:
        print('x este mai mare decat y')
    elif x < y:
        print('x este mai mic decat y')
    else:
        print('X si Y sunt egale')


x = int(input('Introduceti un nr : '))
y = int(input('Introduceti un al doilea nr : '))

print(num(x, y))


# 10. Funcție care primește un număr și un set de numere.
# ● Printeaza ‘am adaugat numărul nou în set’ + returnează True
# ● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ + returnează False
def my_set(numar, set):
    if numar in set:
        print('numarul deja este in set. nu mai adauga')
        return False
    else:
        set.add(numar)
        print('adauga numarul in set')
        return True


set = {1, 2, 3}
print(my_set(3, set))
