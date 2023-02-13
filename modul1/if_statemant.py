ferrari_price = 50000000
varsta = int(input('ASL PLS'))
apt_de_munca = True
sold = int(input('sold: '))
cash = int(input('cash: '))
sold = sold - cash
print(sold)

if sold < cash:
    print('Sold insuficient')
    if varsta < 18:
        print('Cere bani parintilor')
    else:
        print('Bravo esti mare')
        if apt_de_munca:
            print('Angajeaza-te!')
elif sold == cash:
    print('Soldul dv este 0 daca se extrag banii ')
else:
    print('sold')
    if sold > ferrari_price:
        print('Cumpara-ti ferrari')
        sold = sold - ferrari_price
        print(sold)
        ferrari_discount = ferrari_price - 15 / 100
        if sold > ferrari_discount:
            print('Cumpara ti a doua masina ferrari')
    else:
        print('Ia-ti Dacie')
