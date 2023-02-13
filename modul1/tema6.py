import math


# 1
class Cerc:
    def __init__(self, raza, culoare):
        self._raza = raza
        self._culoare = culoare

    def descriere_cerc(self):
        descriere = f'Cercul are culoarea {self._culoare} si raza {self._raza}'
        return descriere

    def area_circle(self):
        area = self._raza ** 2 * math.pi
        return area

    def diametru_circle(self):
        diametru = self._raza * 2
        return diametru

    def circumferinta_circle(self):
        circumferinta = math.pi * 2 * self._raza
        return circumferinta


cercul = Cerc(365, 'yellow')
print(cercul.descriere())
print(cercul.area_circle())
print(cercul.diametru_circle())
print(cercul.circumferinta_circle())


# 2
class Dreptunghi:
    def __init__(self, lungime, latime, culoare):
        self._lungime = lungime
        self._latime = latime
        self._culoare = culoare

    def descrie(self):
        descriere = f'Dreptunghiul are lungimea de {self._lungime}, latimea {self._latime}, iar culoarea {self._culoare}.'
        print(descriere)
        return descriere

    def aria_dreptunghi(self):
        aria = self._latime * self._lungime
        return aria

    def perimetru_dreptunghi(self):
        perimetru = (self._latime + self._lungime) * 2
        return perimetru

    def schimba_culoarea(self, noua_culoare):
        self._culoare = noua_culoare
        print(noua_culoare)


deptunghiul = Dreptunghi(20, 35, 'Alba')
print(deptunghiul.descrie())
print(deptunghiul.aria_dreptunghi())
print(deptunghiul.perimetru_dreptunghi())
noua_culoare = 'mov'
print(deptunghiul.schimba_culoarea(f'Noua culoare a dreptunghiului este: {noua_culoare}'))


# 3

class Angajat:
    def __init__(self, nume, prenume, salariu):
        self._nume = nume
        self._prenume = prenume
        self._salariu = salariu

    def descriere(self):
        descriere = f'Angajatul cu numele : {self._nume} si prenumele {self._prenume} are salariul de: {self._salariu}'
        return descriere

    def nume_complet(self):
        nume = f'Numele angajatului este : {self._nume} {self._prenume}'
        return nume

    def salariu_lunar(self):
        lunar = f'Salariul lunar al angajatului este : {self._salariu} EUR'
        return lunar

    def salariu_anual(self, luni):
        anual = f'Salariul anual al angajatului este : {self._salariu * luni} EUR'
        return anual

    def marire_salariu(self, procent):
        marire = f'Angajatul a prmit o marire de salariu de {procent} %. Salariul angajatului acum este de : {procent * self._salariu / 100 + self._salariu} EUR.'
        return marire


angajat_1 = Angajat('Gula', 'Semida', 8000)
print(angajat_1.descriere())
print(angajat_1.nume_complet())
print(angajat_1.salariu_lunar())
print(angajat_1.salariu_anual(12))
print(angajat_1.marire_salariu(10))


# 4

class Cont:
    def __init__(self, iban, titular_cont, sold):
        self._iban = iban
        self._titular_cont = titular_cont
        self._sold = sold

    def afisare_sold(self):
        afisare_sold = f'Titularul {self._titular_cont} are in contul {self._iban}, suma de {self._sold} lei.'
        return afisare_sold

    def debitare_cont(self, suma):
        if suma < self._sold:
            self._sold -= suma
            print(f'Ati cheltuit suma de : {suma}')
            print(f'Mai aveti in cont suma de : {self._sold}')
        else:
            print('Fonduri insuficente. ')

    def creditare_cont(self, suma):
        self._sold += suma
        print(f'Ati adaugat in cont suma de: {suma}')
        print(f'Acuma aveti in cont suma de: {self._sold}')


cont_bancar = Cont('RO100', 'Semida', 1000)
print(cont_bancar.debitare_cont(250))
print(cont_bancar.creditare_cont(500))
