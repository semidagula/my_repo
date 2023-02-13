"""
1. Declaram expected results - user, password, sold
2. Introducem un username
3. Verificam corectitudinea userului
4. Introducem o parola valida
5. Verificam corectitudinea parolei
6. If all ok - simulat press enter to login
7. Afisam mesaj string in care afisam 'expected sold'
8. Intampinam userul cu un mesaj "cat cash doriti sa transferati?"
9. Afisam in consola daca tranzactia are loc - cat sold ii ramane
10. Extragem si lungimea parolei
11. If lung parolei<5 codul va da "error" (assert)
12. Afisam in consola username-ul, dar parola sa fie inlocuita cu stelute in loc de caracterele propriuzise
"""

user: str = 'andreea'
password: str = 'Abc123'
sold: int = 50000

# 2
actual_user = input('Introduce nume user: ').lower()

print(actual_user)

# 3
assert user == actual_user
# 4
actual_password = input('Introdu parola: ').strip()  # scoate orice spatiu din parola
print(actual_password)
assert password == actual_password
# 6
input('Press Enter to login ')
# 7
print(f'Soldul dvstra este: {sold}')
# 8
cash = int(input('Ce suma doriti sa retrageti?: '))

assert sold - cash >= 0
# dam update la sold!
sold = sold - cash
print(f'Tranzactia a fost efectuata cu succesc. Noul Sold este: {sold}')

# # 10
# print(len(password))

# 11
len_password = len(password)
assert len_password > 5
print(f'Parola introdusa este ok')

# TODO checkul de parola sa il mutam la inceput
# 1 tema: daca am introdus un spatiu parola nu mai e corecta - sa eliminam orice spatiu fie ca e la inceput, la sfarsit, etc
# 2 sa verificam ca ea contine macar o litera mare si un caracter special (parola)
a, b, c, d, e = ' ! ', ' § ', ' % ', ' & ', '='
assert a in password or b in password or c in password or e in password

# 1
password = 'pass!'
a = password.count('!')
assert a > 0
print('! found')

# 2
password2 = 'pasS'
b = password2.isupper()
print('password2 is upper')
