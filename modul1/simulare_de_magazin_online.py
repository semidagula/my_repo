"""
user introduce din consola numele, an nasterii, luna si ziua, cnp ul

verificam daca userul e minor - daca nu i llasam sa se logheze, daca nu il trmitem acasa

daca e major incercam sa extragem din cnp anul nasterii si daca  corespunde cu anul pe care l aintrodus el

daca nu e ok userul nu e lasat sa intre pe site

daca da, extragem pe baza primei cifer daca userul e barbat sau femeie

daca e femeie se afiseza un string cu parfumuri si genti
daca e barbat oun string cu ustensile

daca nu e nici barbat nici femeie :your are a robot get out of the store
#cnp ul are nr impar la barbati si par la femei
"""

nume = input('Nume : ')
an_nastere = int(input('Anul nasterii : '))
luna = int(input('Luna nasterii : '))
ziua = int(input('Ziua nasterii : '))
cnp = int(input('CNP : '))

import datetime

azi = datetime.date.today()
print(azi)
varsta = float(azi.year - an_nastere - ((azi.month, azi.day) < ( luna, ziua)))
print(varsta)
if varsta > 18:
    print('Ai acces la situl nostru')
else:
    print('Nu ai acces la situl nostru, esti minor')

cnp = str(cnp)
if len(cnp) != 13:
    print('CNP ul trebuie sa contina 13 cifre')
an_cnp = cnp[1] + cnp[2]
print(an_nastere)
an_nastere = str(an_nastere)
an_nastere = an_nastere[2:]
gen = cnp[0]
print(gen)
gen = int(gen)
if an_nastere == an_cnp:
    print('Anul nasterii introdus corespunde cu cel din CNP')
    if gen == 1:
        print('Aveti acces catre pagina cu unelte')
    elif gen == 2:
        print('Aveti acces catre pagina cu parfumuri ')
    else:
        print('You are a robot')
else:
    print('Anul nasterii nu corespunde cu el din CNP, nu aveti acces la situl nostru')





