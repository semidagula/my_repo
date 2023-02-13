# 1. Interschimbati valorile a doua variabile.

# 2. Seintroduc 5 numere de la tastatura. Extrageti minimul si maximul

# 3. Afisati pe ecaran daca diferenta dintre 2 numere introduse de la tastatura este mai mica decat 10 (valoarea de adevar).

# 4. Calculati perimetrul unui triunghi dreptunghic, ale carui catete au valorile 3 si 4.

# 1
numar1 = 2
numar2 = 9

print(numar1, numar2)
nr_intermediar = numar1
numar1 = numar2
numar2 = nr_intermediar
print(numar1, numar2)

# 2
a = int(input('Introduceti primul nr: '))
b = int(input('Introduceti al doilea nr: '))
c = int(input('Introduceti al treilea nr: '))
d = int(input('Introduceti al patrulea nr: '))
e = int(input('Introduceti al cincilea nr: '))
print(max(a, b, c, d, e))
print(min(a, b, c, d, e))

# 3
valoarea_adevar = 10
a = float(input('Introduceti primul nr: '))
b = float(input('Introduceti al doilea nr: '))
print(bool(a - b) < valoarea_adevar)

# 4
from math import sqrt as radical

cateta_1 = 3
cateta_2 = 4
ipotenuza = radical(pow(3, 2) + pow(4, 2))
perimetrul = cateta_1 + cateta_2 + ipotenuza
print('ipotenuza este:', ipotenuza)
print('perimetrul este: ', perimetrul)

1
# O variabila este o zona dintr-o memorie care stocheaza valori.
metode_stringuri = ' Metode {} si {}metode {} etc {}e tc '
print(
    dir(metode_stringuri))  # 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
# <class 'str'>
print(metode_stringuri.capitalize())  # scriem prima litera mare
print(metode_stringuri.casefold())  # scriem prima litera mica
txt = ' " " xyz\t12345\tabüc'
num = '123'
x = txt.center(30,
               "9")  # incadram stringul intre lungime (alegem peste cifra 10) si caraterul(len. character <10): 999999999999banana999999999999

print(txt.count('a'))  # numaram un anumit char dintr-un string
txt_utf = txt.encode()
print(txt_utf)  # printam versiunea encodata a unui string ( daca contine ö,ä,ü) By default, Python uses utf-8 encoding.
print(txt.endswith('a'))  # returns True if the string ends with the specified value, otherwise False.
print(txt.expandtabs(
    10))  # sets the tab size to the specified number of whitespaces. elimina '\t' si baga un anumit nr de taburi,  The default tabsize is 8.
print(txt.find('ü'))  # ne gaseste locul unui caracter din string si ne printeaza indexul sau
print(metode_stringuri.format('Python', 3, 5.2,
                              '%'))  # introducem in string unde este pozitionat {} integers, floating point numeric constants, strings, characters and even variables. Only difference is, the number of values passed as parameters in format() method must be equal to the number of placeholders created in the string.

print(metode_stringuri.index('m'))  # arata indexul unui anumit char din string, pus intre paranteze "

print(
    txt.isalnum())  # returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
print(txt.isalpha())  # printeaza True daca caracterele din string sunt in ordine alfabetica.
print(
    txt.isascii())  # method returns True if the string is empty or all characters in the string are ASCII.ASCII stands for American Standard Code for Information Interchange
print(txt.isdigit())  # returneaza True daca stringul contine doar cifre
print(
    metode_stringuri.isidentifier())  # returns True if the string is a valid identifier, otherwise False. A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.
# returneaza true daca stringul nu are spatii deloc si nu incepe cu o cifrea
print(metode_stringuri.islower())  # returneaza True daca prima litera din string este mica
print(num.isnumeric())  # returneaza true daca stringul este numeric. contine doar numere

string = 'GeeksforGeeks\nname\nis\nCS portal'
newstring = ''
count = 0
for a in string:
    if (a.isprintable()) == False:
        count += 1
        newstring += ' '
    else:
        newstring += a
print(count)
print(newstring)

print(txt.isspace())  # returneaza True daca toate caracterele din string sunt whitespace ‘ ‘ – Space, ‘\t’ – Horizontal tab, ‘\n’ – Newline,‘\f’ – Feed, ‘\r’ – Carriage return, ‘\v’ – Vertical tab.
# returneaza False daca are stringul cel putin un whitespace

# 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip',
y = 'Ala Bala Portocala'
z = 'ALA BALA PORTOCALA'
s = 'EU'
print(
    y.istitle())  # True #returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False.
print(z.isupper())  # True daca toate literele sunt mari
print(s.join(z))  # inserezi un string intr un alt string dupa fiecare caracter/litera a acestuia
print(s.ljust(20,
              '!'))  # EU!!!!!!!!!!!!!!!!!! # adauga dupa string format dor dintrun cuvant/litera, nr de elemente pe care l scriem ca string (20, '!')
print(s.lower())  # printeaza toate charcterele  mici
print(y.lstrip('Ala'))  # sterge din partea stanga a stringului tot ce scriem noi in ('')

# first string
firstString = "abc"
secondString = "def"
string = "abc"
print(string.maketrans(firstString,
                       secondString))  # {97: 100, 98: 101, 99: 102} #method returns a mapping table that can be used with the translate() method to replace specified characters.

print(y.partition())  # separator

print(y.removeprefix('Ala'))  # sterge prefixul
print(y.removesuffix('la'))  # sterge caracterele care le alegem de la sfrasitul stringului
print(y.replace('a', 'i'))  # inlocuieste o litera cu alta,

print(y.rpartition())  # split the given string into three parts. rpartition()

print(y.strip())  # elimina white spaces daca sunt
'swapcase', 'title', 'translate', 'upper', 'zfill'

print(y.swapcase())  # inverseza literele mari cu cele mici
print(z.title())  # face doar prima litera a fiecarui cuv din string sa fie mare

print(y.translate(
    dict))  # returns a string where some specified characters are replaced with the character described in a dictionary, or in a mapping table
print(y.upper())  # face toate literele mari
print(y.zfill(10))  # adauga '0' in partea stanga a stringului atata cat ii dam in ()

"""
#2
nume: str ='Semida'
varsta: int = 31
greutate: float = 56.85
casatorita: bool = True

#3

print(type(nume))# class str
print(type(varsta))# class int
print(type(greutate))# class float
print(type(casatorita))# class bool

#4
greutate = float(56.85)
print(round(greutate))
greutate = (round(greutate))
print(type(greutate))

#5
print(f'Ma numesc {nume}.')
print(f'Am varsta de {varsta} ani.')
print(f'Am greutatea de {greutate} kg.')
print(f'Sunt casatorita {casatorita}.')

#6


nume = input('Numele tau este: ')
prenume = input(' Prenumele tau este: ')
len_numecomplet = int(len(nume) + len(prenume))

print(f'Numele complet contine: {len_numecomplet}')

#7
lungimea = int ( input('lungimea: '))
latimea = int (input('latimea: '))

print(f'Aria drepunghiului este: {lungimea * latimea}')

#8
s = ' Coral is either the stupidest animal or the smartest rock'
print( s.count('the'))

#9

print('Cuvantul "the" apare de ', s.count('the'), 'ori.')

#10
print(s.isnumeric())
assert s.isnumeric() != True


#1'


prop = input (' Introduceti numele: ')

lenght = len(prop)

mijloc_lenght= int(lenght / 2)
print(prop[round(mijloc_lenght)])


#2' # PALINDROM = un cuv care se citeste la fel si inapoi (madam, level, refer)

s = input("Enter a string:")
revstr = (s[::-1])
assert revstr == s,"This is a Palindrome"


#if revstr == s:
#    print("This is a Palindrome")
#else:
#    print("This is not a Palindrom")

#3' !!!

s1, s2 = input('Primul string: '), input('Al doilea string: '); print (s1 + ' ' + s2)

#4'

string1,  string2 = input ('First: '), input('Second: '); print( string1+ '  ' + string2)


#5'
user = input('user: ')
password= input('parola: ')
long = len(password)
stars = '*'
long_stars = len(stars)
print(long_stars)
password1 = password.replace(password, '*',long)
print(f'Parola pentru user :{user} este {password1} si are {long} caractere')
"""
