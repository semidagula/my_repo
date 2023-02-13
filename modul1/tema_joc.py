"""
2. Joc de noroc
- Cauta pe net si vezi cum se genereaza un numar random
- Imagineaza-ti ca dai cu zarul si salvezi acest numar intr-o variabila numita dice_roll.
Numarul salvat va fi generat random cu metoda gasita in online
- Introdu un numar de la tastatura care sa reprezinte numarul ales de la utilizator
- Verifica si afiseaza daca utilizatorul a ghicit numarul
- Vor exista 3 optiuni care vor trebui tratate:
● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
● Ai ghicit. Felicitari? Ai ales x si zarul a fost y
"""
import random

first = int(input('Introdu numarul random : '))
dice_roll = random.randint(1, 6)
print(dice_roll)

if dice_roll > first:
    print('Ai pierdut : ai ales un numar mai mic.')
elif dice_roll < first:
    print('Ai pierdut, ai ales un numar mai mare.')
else:
    print('Ai ghicit. Felicitari!')
