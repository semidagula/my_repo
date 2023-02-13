class ContBancar:
    def __init__(self, titularCont, iban):  # CONSTRUCTOR --------- DEFINIM ATRIBUTELE CONTULUI BANCAR
        self.titularCont = titularCont
        self.iban = iban
        self.sold = 0
        self.active = False
        self.pin = 7777
        self.incercari_activare = 0

    def salut(self):
        print(f'Buna ziua {self.titularCont}')

    def interogare_sold(self):
        print(f'Titular {self.titularCont}')
        print(f'IBAN {self.iban}')
        print(f'Soldul dv: {self.sold}')
        print(f'Contul dv este : {self.active}')
        print(f'Introduceti pinul : {self.pin}')
        print(f'Mai aveti : {self.pin}, incercari')

    def activa_cont(self, pin_utilizator):
        self.salut()
        if pin_utilizator == self.pin:
            print('Card activat')
            self.active = True
        else:
            print('Pin gresit')
            self.incercari_activare += 1

    def alimenatre(self, suma):
        suma += self.sold
        print(f'Ati alimentat contul cu suma{suma}')
        print(f'Aveti in cont suma de : {self.sold}')

    def plata_Card(self, suma):
        if suma > self.sold:
            self.sold -= suma
            print(f'Ati cheltuit suma de: {suma}')
            print(f'Aveti in cont suma de: {self.sold}')
        else:
            print('Fonduri insuficente. ')
