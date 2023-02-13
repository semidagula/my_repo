
#1. Funcție care primește o lună din an și returnează câte zile are acea luna
from calendar import monthrange
def number_of_days_in_month(year,month):
    return monthrange(year, month)[1]

year = 2023
month = 5
print(number_of_days_in_month(2023, 3))


#2. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea,
#împărțirea a două numere.
#În final vei putea face:
#a, b, c, d = calculator(10, 2)
#● print("Suma: ", a)
#● print("Diferenta: ", b)
#● print("Inmultirea: ", c)
#● print("Impartirea: ", d)


def a (x,y):
    sum = x+y
    return sum
def b (x,y):
    dif = x-y
    return dif
def c(x,y):
    ori = x*y
    return ori
def d(x,y):
    imp = x/y
    return imp

print('Suma:', a(20, 30))
print('Diferenta:', b(23, 3))
print('inmultirea:', c(23, 2))
print('impartirea:', d(45, 5))

"""3. Funcție care primește o lista de cifre (adică doar 0-9)
Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returnează un DICT care ne spune de câte ori apare fiecare cifră"""
def count_nr(lista_nr):
  nr = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0
    }
  for n in lista_nr:
    nr[n]+= 1
  return nr
lista_nr = [2,3,5,5,6,6,8,7,9,9,2,3,5,4, 0,0,0,5]
print(count_nr(lista_nr))

#4. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele

def get_max(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>c):
        return b
    else:
        return c

a = int(input('Enter a:'))
b = int(input('Enter b:'))
c = int(input('Enter c:'))
ans = max(a,b,c)
print('The largest of three numbers=', ans)

#5. Funcție care să primească un număr și să returneze suma tuturor numerelor de la 0 la acel număr
#Exemplu: daca dam nr 3. Suma va fi 6 (0+1+2+3)

def getSum(n):
    sum = 0
    while (n > 0):
        sum += int(n % 10)
        n = int(n / 10)

    return sum


if __name__ == "__main__":
    n = 235
    print(getSum(n))


#1.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați numerele comune
"""Exemplu:

Răspuns: {2, 3}   """

def com_num(list1, list2):
    return set(list1) & set(list2)

list1 = [1, 1, 2, 3, 4]
list2 = [2, 2, 3, 4]
print('Raspuns: ', com_num(list1, list2))

#2.. Funcție care să aplice o reducere de preț
#Dacă produsul costa 100 lei și aplicăm reducere de 10%. Pretul va fi 90
#Tratați cazurile în care reducerea e invalida. De exemplu o reducere de 110% e invalidă.

def procentaj(procent, intreg):
    if procent > 100:
        print('REducere invalida')
        breakpoint()
    return (procent*intreg)/100

procent= float(input('Introduceti procentul de reducere: '))
intreg = float(input('Introduceti pretul intreg caruia ii aplicati reducerea: '))
print('Pretul redus este: ', procentaj(procent, intreg))


#3 3. Funcție care să afișeze data și ora curentă din ro (bonus: afișați și data și ora curentă din China)

def datetime_Ro():
    import datetime
    datetime_Ro = datetime.datetime.now()
    return datetime_Ro
print(datetime_Ro().strftime("%m/%d/%Y %H:%M"))

def china_time():
    import datetime
    from pytz import timezone
    china_timezone = timezone('Asia/Shanghai')
    china_time = datetime.datetime.now(china_timezone)
    print("Data si ora din China sunt: ", china_time.strftime("%m/%d/%Y %H:%M"))


#4. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la
#Crăciun dacă nu vrei să ne zici cand e ziua ta :

def cate_zile_ziuamea(zi, luna, an):
    from datetime import date
    azi = date.today()
    data_nasterii = date(an, luna, zi)
    dif_zile = data_nasterii - azi
    return dif_zile.days
print(cate_zile_ziuamea(10, 2, 2023))