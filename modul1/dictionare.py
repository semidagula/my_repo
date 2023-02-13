my_dict = {
    'animal': 'pisica',
    123: 'this is a number',
    True: [
        {
            'user': 'rares',
            'parola': 'andrei'
        },
        {   'user': 'ion',
            'parola': 'marcel'
        }
    ],
    52.2: 'latitudinea Romaniei'
}

my_dict2 = dict(animal='pisica', numbers='this is a number',
                my_boolean=[dict(user='rares', parola='andrei'), dict(user='ion', parola='marcel')],
                parole={
                    1: 1,
                    True: 'Yes',
                })

#extragerea de date:
print(my_dict[True][1]['parola']) # accesam o valoare: marcel

my_dict['email'] = 'gmail@gmail.com' # adaugam un element
print(my_dict)

del my_dict['email']
print(my_dict)




