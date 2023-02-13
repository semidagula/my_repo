from Old_car import OldCar

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
