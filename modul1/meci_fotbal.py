#- Efectuam schimbarea daca jucatorul e in lista de rezerve si nu exista in jucatorii de pe teren
#
lista_jucatori_interen= ['Messi', 'Ion', 'Hagi', 'Mutu', 'Leoni']
lista_jucatori_rezerva = ['Jucator1', 'Jucator2', ' Jucator3', 'Jucator4', 'Jucator5']
lista_jucatori_scosi = [""]
schimbari_max = lista_jucatori_scosi.count(4)
schimbari_efectuate = 0


schimbarea1 =input(f'Alegeti un jucator din {lista_jucatori_interen} pe care doriti sa-l scoateti: ')
print(schimbarea1)

if schimbarea1 in lista_jucatori_interen :

    print(f'{schimbarea1} este pe teren si mai sunt 3 schimburi')
    first = lista_jucatori_interen.remove(schimbarea1)
    first = lista_jucatori_scosi.append(schimbarea1)
    first_rezerva = input(f'Alegeti un jucator din lista de jucatori din rezerva cu care doriti sa il inlocuiti pe {schimbarea1}: {lista_jucatori_rezerva} : ')
    print(first_rezerva)
    lista_jucatori_rezerva.remove(first_rezerva)
    lista_jucatori_interen.append(first_rezerva)
    print(f'Daca a iesit {schimbarea1} si a intrat {first_rezerva} mai aveti 3 schimbari.')
    print(f'Jucatorul {schimbarea1} este acum scos iar in teren este {first_rezerva}')
    print(lista_jucatori_interen)
    print(lista_jucatori_rezerva)
    print(lista_jucatori_scosi)

    schimbarea2 = input(f'Alegeti un al doilea jucator din {lista_jucatori_interen} pe care doriti sa-l scoateti: ')
    if schimbarea2 in lista_jucatori_interen :
        print(f'{schimbarea2}  este pe teren si mai sunt 2 schimburi')
        second = lista_jucatori_interen.remove(schimbarea2)
        second = lista_jucatori_scosi.append(schimbarea2)
        second_rezerva = input(f'Alegeti un jucator din lista de jucatori din rezerva cu care doriti sa il inlocuiti pe {schimbarea2}: {lista_jucatori_rezerva} : ')
        print(second_rezerva)
        lista_jucatori_rezerva.remove(second_rezerva)
        lista_jucatori_interen.append(second_rezerva)
        print(f'Daca a iesit {schimbarea2} si a intrat {second_rezerva} mai aveti 2 schimbari.')
        print(f'Jucatorul {schimbarea2} este acum scos iar in teren este {second_rezerva}')
        print(lista_jucatori_interen)
        print(lista_jucatori_rezerva)
        print(lista_jucatori_scosi)

        schimbarea3 = input(f'Alegeti un al treilea jucator din {lista_jucatori_interen} pe care doriti sa-l scoateti: ')
        if schimbarea3 in lista_jucatori_interen :
            print(f'{schimbarea3} este pe teren si mai este un singur schimb.')
            third = lista_jucatori_interen.remove(schimbarea3)
            third = lista_jucatori_scosi.append(schimbarea3)
            third_rezerva = input(f'Alegeti un jucator din lista de jucatori din rezerva cu care doriti sa il inlocuiti pe {schimbarea3}: {lista_jucatori_rezerva} : ')
            print(third_rezerva)
            lista_jucatori_rezerva.remove(third_rezerva)
            lista_jucatori_interen.append(third_rezerva)
            print(f'Daca a iesit {schimbarea3} si a intrat {third_rezerva} mai aveti 1 schimbari.')
            print(f'Jucatorul {schimbarea3} este acum scos iar in teren este {third_rezerva}')
            print(lista_jucatori_interen)
            print(lista_jucatori_rezerva)
            print(lista_jucatori_scosi)
            if lista_jucatori_scosi.count(3):
                print('Nu mai puteti face nicioschimbare')
            else:
                print('schimburile de jucatori s-au incheiat')




