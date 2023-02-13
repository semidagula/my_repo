# Mostenirea - ai acces la metodele din parinte si in copil
from abc import ABC, abstractmethod


class CarModel(ABC):
    @abstractmethod
    def volan(self):
        raise NotImplemented

    @abstractmethod
    def roti(self):
        raise NotImplemented

    @abstractmethod
    def scaune(self):
        raise NotImplemented

    def sistem_audio(self):
        print('Avem sistem audio')


class OldCar(CarModel):
    def scaune(self):  # metode publice
        print('Are 4 scaune')

    def volan(self):
        print('Masina are volan pe stanga')

    def motor(self):
        print('Masina are motor diesel')

    def roti(self):
        print('Masina are roti de lemn')

    def __pilot_automat(self):  # privata are acces doar orice alta met din interiorul clasei
        print('Bunicu i pilot')

    def _valoare_sentimentala(self):  # protected
        self.__pilot_automat()
        print('Masina de colectie')


class ModernCar(OldCar):
    def oglinzi(self):
        print('Are 5 oglinzi')

    def roti(self):  # suprascriere
        print('Masina are roti de sticla')

    def absenabled(self):
        print('Are sistem abs')

    def airbag(self):
        print('Are airbaguri')

    def extra_optiuni(self):
        self._vaoare_sentimentala()



class BritishCar(ModernCar):
    def volan(self):
        print('Volan pe dreapta')

    def gps(self):
        print('Masina are gps')


class AlienCar(CarModel):

    def roti(self):
        print('Roti verzi')

    def scaune(self):
        print('Scaune verzi')

    def volan(self):
        print('Volan verde')


dacia = OldCar()
renault = ModernCar()
british_renault = BritishCar()

alien = AlienCar()
renault.roti()
dacia.roti()
british_renault.volan()
renault.volan()
renault._valoare_sentimentala()
alien.roti()

'TODO:' \
'creaza un pachet care sa se numeasca car si fiecare clasa sa fie mutata intr un fisier nou( clasa  - modulul)'
'crearea unui mini proiect oop care sa simuleze teste: framework pt o testare taste case. ce contine un teste plan, teste grup, test suite'
