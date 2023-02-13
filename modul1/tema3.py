"""
1. Declara o lista note_muzicale in care sa pui do re mi etc pana la do
a. Afiseaz-o
b. Inversează ordinea folosind slicing si suprascrie aceasta lista, apoi printeaza
varianta actuala (inversata)
c. Pe aceasta lista, aplica o metoda care banuiesti ca face același lucru, adica sa ii
inverseze ordinea (Nu trebuie sa o suprascrii în acest caz, deoarece metoda face
asta automat) si apoi printeaza varianta actuala a listei. Practic ai ajuns înapoi la
varianta inițială
Concluzii: slicing e temporar, dacă vrei sa pastrezi noua varianta va trebuie sa
suprascrii lista sau sa o salvezi intr-o listă nouă. Metoda gasita de tine face
suprascrierea automat și permanentizeaza aceste modificări. Ambele variante își
găsesc utilitatea în funcție de ce ne dorim in acel moment.
"""
import keyword

note_muzicale = ["do", "re", "mi", "fa", "sol", "la", "si", "do"]
reverse_list = note_muzicale[::-1]
print(note_muzicale)

x = note_muzicale.reverse()
print(note_muzicale)

# 2. Afiseaza pe ecran de cate ori apare nota ‘do’ in lista.
print(note_muzicale.count("do"))


# 3. Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4], gaseste 2 variante sa le unesti intr-o singura lista.
def Union(lst1, lst2):
    final_list = list(set(lst1) | set(lst2))
    return final_list


lst1 = [3, 1, 0, 2]
lst2 = [6, 5, 4]
print(Union(lst1, lst2))
x = Union(lst1, lst2)
print(x)
# 4. Sorteaza si afiseaza lista generata la exercitiul anterior. Sterge numarul 0 din lista folosind o functie si apoi afiseaza din nou lista
x.sort()
print(x)
del x[0]
print(x)

"""
5. Folosind un if, verifica lista generata la exercitiul 3 si afiseaza pe fiecare ramura
urmatoarele:
- Lista este goala (IF)
- Lista nu este goala (ELSE)
"""

if len(x) == 0:
    print("lista este goala")
else:
    print("lista nu este goala")

# 6. Foloseste o functie care sa goleasca lista de la exercitiul 3
x.clear()
print(x)

# 7. Rescrie if-ul de la exercitiul 5 si verifica inca o data rezultatul. Acum ar trebui sa se afiseze ca lista e goala #OK

if len(x) == 0:
    print("lista este goala")
else:
    print("lista nu este goala")

# 8. Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}, foloseste o functie ca sa  afisezi Elevii (cheile)

dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
print(dict1.keys())

# 9. Printeaza cei 3 elevi din dictionarul de mai sus si respectiv notele lor
# Ex: ‘Ana a luat nota {x}’.
# Doar nota o vei lua folosindu-te de cheie

new_output = list(dict1.values())
print('Ana a luat nota :', new_output[0])
print('Gigel a luat noa :', new_output[1])
print('Dorel a luat nota:', new_output[2])

# 10. Imagineaza-ti ca Dorel a facut contestatie si a primit nota 6.
# - Modifica nota lui Dorel in 6
# - Printeaza nota lui dupa modificare

new_output[2] = 6
print('Dorel a luat nota:', new_output[2])

# 11. Imagineaza-ti ca Gigel se transfera din clasa.
# - Cauta o functie care sa il stearga
# Vine un coleg nou.
# - Adaugati-l in lista pe Ionica, cu nota 9
# - Printati dictionarul cu noii elevi


print(dict1.pop('Gigel'))
print(dict1)
dict1.update()

new_key = 'Ionica'
new_value = '9'

updated_dict = {**dict1, new_key: new_value}
print(updated_dict)

"""
12. Ai urmatoarele seturi:
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
- Incearca sa adaugi in setul zilele_sapt ziua de ‘luni’ si observa ce se intampla.
- Afiseaza setul zile_sapt si constata rezultatul adaugarii anterioare.
"""

zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}

zile_sapt.add('luni')
print(zile_sapt)  # s-au amestecat elementele. nu s ordonate

"""
13. Foloseste un if si verifica daca:
- Weekend este un subset al zilelor din sapt (adica daca elementele din setul weekend se
regasesc intre elementele din setul zile_sapt)
- Weekend nu este un subset al zilelor din sapt
Hint: Va puteti folosi fie de operatorul de comparatie fie de o functie. Rezultatul fiecarui
punct de mai sus va fi un boolean
"""
if zile_sapt == weekend:
    print(bool('Weekend este un subset al zilelor sapt'))
else:
    print(bool('Weekend este un subset al zilelor sapt'))

# 14. Afiseaza diferentele dintre aceste 2 seturi (adica elementele care sunt in zile_sapt si nu sunt in weekend si invers)
print(zile_sapt.difference(weekend))
print(weekend.difference(zile_sapt))

# 15. Afiseaza intersectia elementelor din aceste 2 seturi (adica elementele care exista in ambele seturi). Hint: Va puteti folosi de o functie
print(zile_sapt.intersection(weekend))
print(weekend.intersection(zile_sapt))
