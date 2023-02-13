"""ABSTRACTION
Clasa abstractă FormaGeometrica
Conține un field PI=3.14
Conține o metodă abstractă aria (opțional)
Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
probabil am colturi’
INHERITANCE
Clasa Pătrat - moștenește FormaGeometrica
constructor pentru latură

ENCAPSULATION
latura este proprietate privată
Implementează getter, setter, deleter pentru latură
Implementează metoda cerută de interfață (opțional, doar dacă ai ales să
implementezi metoda abstractă aria)
Clasa Cerc - moștenește FormaGeometrica
constructor pentru rază
raza este proprietate privată
Implementează getter, setter, deleter pentru rază
Implementează metoda cerută de interfață - în calcul folosește field PI
mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda
abstractă aria)
POLYMORPHISM
Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
Creează un obiect de tip Patrat și joacă-te cu metodele lui
Creează un obiect de tip Cerc și joacă-te cu metodele lui
3. Actualizează proiectul pe github facand un push la noul cod
În Foldereul de teme ajunge să pui doar linkul cu proiectul tău public"""
from abc import ABC, abstractmethod


class FormaGeometrica(ABC):  # ABSTRACTION
    PI = 3.14

    @abstractmethod
    def aria(self):
        raise NotImplemented

    def descrie(self):
        print('Cel mai probabil am colturi')


class Patrat(FormaGeometrica):  # INHERITANCE
    def __init__(self, latura):
        self.__latura = latura

    @property
    def latura(self):
        return self.__latura

    @latura.getter
    def latura(self, val):
        self.__latura = val

    @latura.setter
    def latura(self, val):
        self.__latura = val

    @latura.deleter
    def latura(self):
        del self.__latura

    def aria(self):
        return self.__latura * self.__latura


class Cerc(FormaGeometrica):
    def __init__(self, raza):
        self._raza = raza

    def __raza(self):
        print('Raza este privata')

    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self, val):
        self.__raza = val

    @raza.setter
    def raza(self, val):
        self.__raza = val

    @raza.deleter
    def raza(self):
        del self.__raza

    def descrie(self):
        print('Eu nu am colturi')

    def aria(self, PI):
        return self.__raza ** 2 * PI


patrat = Patrat(3)
patrat.descrie()
patrat.aria()

cerc = Cerc(1)
cerc.descrie()
print(cerc.aria())
