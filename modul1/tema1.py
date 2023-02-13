# ex.1
# O variabila este o zona dintr-o memorie care stocheaza valori.


# ex.2
nume: str = 'Semida'
varsta: int = 31
greutate: float = 56.85
casatorita: bool = True

# 3
print(type(nume))  # class str
print(type(varsta))  # class int
print(type(greutate))  # class float
print(type(casatorita))  # class bool

# 4
greutate = float(56.85)
print(round(greutate))
greutate = (round(greutate))
print(type(greutate))

# 5
print(f'Ma numesc {nume}.')
print(f'Am varsta de {varsta} ani.')
print(f'Am greutatea de {greutate} kg.')
print(f'Sunt casatorita {casatorita}.')

# 6
nume = input('Numele tau este: ')
prenume = input(' Prenumele tau este: ')
len_numecomplet = int(len(nume) + len(prenume))
print(f'Numele complet contine: {len_numecomplet}')

# 7
lungimea = int(input('lungimea: '))
latimea = int(input('latimea: '))
print(f'Aria drepunghiului este: {lungimea * latimea}')

# 8
s = ' Coral is either the stupidest animal or the smartest rock'
print(s.count('the'))

# 9
print('Cuvantul "the" apare de ', s.count('the'), 'ori.')

# 10
print(s.isnumeric())
assert s.isnumeric() != True

# 1
prop = input(' Introduceti numele: ')

lenght = len(prop)

mijloc_lenght = int(lenght / 2)
print(prop[round(mijloc_lenght)])

# 2 # PALINDROM = un cuv care se citeste la fel si inapoi (madam, level, refer)
s = input("Enter a string:")
revstr = (s[::-1])
assert revstr == s, "This is a Palindrome"

if revstr == s:
    print("This is a Palindrome")
else:
    print("This is not a Palindrom")

# 3
s1, s2 = input('Primul string: '), input('Al doilea string: ');
print(s1 + ' ' + s2)

# 4
string1, string2 = input('First: '), input('Second: ');
print(string1 + '  ' + string2)

# 5
user = input('user: ')
password = input('parola: ')
long = len(password)
stars = '*'
long_stars = len(stars)
print(long_stars)
password1 = password.replace(password, '*', long)
print(f'Parola pentru user :{user} este {password1} si are {long} caractere')
