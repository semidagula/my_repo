# 1

from datetime import date

class Factura:
    serie = 'SV001'
    numar = 1

    def __init__(self, nume_produs, cantitate, pret_buc):
        self._nume_produs = nume_produs
        self._cantitate = cantitate
        self._pret_buc = pret_buc

    def schimba_cantitatea(self, cantitate):
        self._cantitate = cantitate
        print(f'Cantitatea actuala este: {cantitate}')
        return cantitate

    def schimba_pretul(self, pret):
        self._pret_buc = pret
        print(f'Pretul actual pe bucata este: {pret} Euro')
        return pret

    def schimba_nume_produs(self, nume):
        self._nume_produs = nume

        print(f'Produsul actual este: {nume}')
        return nume

    def pret_total(self):
        total = self._cantitate * self._pret_buc
        return total


numar = 1
today = date.today()
serie = 'SV001'
magazin = Factura('Iphone', 20, 500)

t = PrettyTable(['Produs', 'Cantitate', 'Pret_bucata', 'total'])
t.add_row([magazin.schimba_nume_produs('Iphone'), magazin.schimba_cantitatea(20), magazin.schimba_pretul(800),
           magazin.pret_total()])
t.add_row([magazin.schimba_nume_produs('Samsung'), magazin.schimba_cantitatea(30), magazin.schimba_pretul(900),
           magazin.pret_total()])

print(f'------------DATA:{today}-----------')
print(f'------------FACT:{serie} nr:{numar}-----------')
print(t)


# 2
class Masina:

    def __init__(self, model, viteza_max):
        self._model = model
        self._viteza_max = viteza_max
        self._marca = 'Audi'
        self._viteza_actuala = 0
        self._culoare = 'Gri'
        self._inmatriculata = False
        self._culori_disponibile = {'Negru', 'Alb', 'Mov', 'Roz', 'Galben', 'Albastru', 'Verde'}

    def descriere(self, marca, model, viteza_max, viteza_actuala, culoare, inmatriculata):
        print(
            f'Fabrica produce marca de masini {self._marca}, modelul: {model}, viteza maxima este de {self._viteza_max} km/h, '
            f'viteza actuala este {self._viteza_actuala}, culoarea standard este: {self._culoare}, inmatriculata: {self._inmatriculata}')

    def inmatriculare(self, inmatriculata):
        self._inmatriculata = inmatriculata
        inmatriculata = True
        print(f'Masina este acuma inmatriculata: {inmatriculata}')
        return inmatriculata

    def vopseste(self, culoare):
        if culoare in self._culori_disponibile:
            print(f'Masina vopsita : {culoare}')
        else:
            print('Eroare')

    def accelereza(self, viteza):
        if viteza == 0:
            print('Eroare')
        elif self._viteza_max > viteza:
            print(f'Accelereaza pana la {viteza} ')
        elif self._viteza_max < viteza:
            print(f'Accelereaza pana la {self._viteza_max}')
        else:
            print('Eroare')

    def franeaza(self, viteza):
        viteza = 0
        print(f'Masina s-a oprit')


auto = Masina('Q7', 260)
auto.descriere('Audi', 'Q7', 260, 0, 'gri', False)
auto.inmatriculare('')
auto.vopseste('Roz')
auto.accelereza(290)
auto.franeaza(0)

# 3
