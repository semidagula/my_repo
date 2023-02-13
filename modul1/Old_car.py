from car_factory import CarModel

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

