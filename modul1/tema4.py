# 1Folosește un for că să iterezi prin toată lista și să afișezi;
# ● ‘Mașina mea preferată este x’.
# ● Fă același lucru cu un for each.
# ● Fă același lucru cu un while.

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
masina_pref = input('Masina dv preferata este:')
for masina_pref in masini:
    print('Masina dv preferata este: ' + str(masina_pref))
    break

masina_preferata = input('Masina mea preferata este: ')
while masina_preferata in masini:
    print('Masina dv preferata este: ' + str(masina_preferata))
    break

# 2.Aceeași listă:
# Folosește un for else
# În for
# - Modifică elementele din listă astfel încât să fie scrie cu majuscule,exceptând primul și ultimul.

# În else:
# - Printează lista.

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

for masina in range(2, len(masini)):
    masina -= 1
    print(masini[masina].upper())
else:
    print(masina)

# 3. Aceeași listă:
# Vine un cumpărător care dorește să cumpere un Mercedes.
# Itereaza prin ea prin modalitatea aleasă de tine.
# Dacă mașina e mercedes:
# Printează ‘am găsit mașina dorită de dvs’
# Ieși din ciclu folosind un cuvânt cheie care face acest lucru
# Altfel:
# Printează ‘Am găsit mașina X. Mai căutam‘

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
m_dorita = 'Mercedes'
for masini in masini:
    if m_dorita == 'Mercedes':
        print('Am gasit masina dorita de dvs : ' + str(m_dorita))
    break
else:
    print('Am gasit alte masini, mai cautam')

    # 4. Aceași listă;
    # Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu excepția Trabant și Lăstun.
    # - Dacă mașina e Trabant sau Lăstun:
    # Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
    # - Printează S-ar putea să vă placă mașina x.

    masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
    for masini_excluse in masini:
        if masini_excluse == 'Lastun':
            masini.remove(masini_excluse)
        elif masini_excluse == 'Trabant':
            masini.remove(masini_excluse)
        continue
    print('S-ar putea sa va placa masinile urmatoare: ' + str(masini))

    # OK5. Modernizează parcul de mașini:
    # ● Crează o listă goală, masini_vechi.
    # ● Itereaza prin mașini.
    # ● Când găsesti Lăstun sau Trabant:
    # - Salvează aceste mașini în masini_vechi.
    # - Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
    # ● Printează Modele vechi: x.
    # ● Modele noi: x.

    masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
    masini_vechi = []
    for masina in masini:
        if 'Lastun' in masini:
            masini.remove('Lastun')
            masini_vechi.append('Lastun')
            print(masini)
        elif 'Trabant' in masini:
            masini.remove('Trabant')
            masini_vechi.append('Trabant')
            masini.append('Tesla')
        continue
    print('Modele vechi : ' + str(masini_vechi))
    print('Modele noi : ' + str(masini))

    # 6. Având dict:
    # Vine un client cu un buget de 15000 euro.
    # ● Prezintă doar mașinile care se încadrează în acest buget.
    # ● Itereaza prin dict.items() și accesează mașina și prețul.
    # ● Printează Pentru un buget de sub 15000 euro puteți alege mașină xLastun
    # ● Iterează prin listă.

    pret_masini = {
        'Dacia': 6800,
        'Lăstun': 500,
        'Opel': 1100,
        'Audi': 19000,
        'BMW': 23000
    }
    buget = 15000
    for k, v in pret_masini.items():
        if v <= buget:
            print('Masinile care se incadreasa la acest buget sunt : ', k, v)

    # OK7. Având lista:
    # ● Iterează prin ea.
    # ● Afișează de câte ori apare 3 (nu ai voie să folosești count).

    numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
    for i in numere:
        if i == 3:
            numar = i + 1
            print(i)

    # OK8. Aceeași listă:
    # ● Iterează prin ea
    # ● Calculează și afișează suma numerelor (nu ai voie să folosești sum).

    num = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
    count = 0
    total = 0

    for number in num:
        count += 1
        total += number

    print(total)
    print(count)

    # print(f"Suma calculata printata din else este: {index}")
    # breakpoint = modalitate prin care putem sa anuntam sistemul ca trebuie sa opreasca executarea codului
    # la o instructiune specifica

    # OK#9. Aceeași listă:
    # ● Iterează prin ea.
    # ● Afișază cel mai mare număr (nu ai voie să folosești max).

    numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
    mare = None
    for nr in numere:
        if mare is None or mare < nr:
            mare = nr
    print(mare)

    # 10. Aceeași listă:
    # ● Iterează prin ea.
    # ● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
    # Ex: dacă e 3, să devină -3
    # ● Afișază noua listă.

    numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
    new_list = [-number for number in numere]
    print(new_list)
