"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Martina Spieszová
email: mspieszova@gmail.com
discord: MartinaSpi
"""
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
pocet_mala_pismena = 0
pocet_zacinajici_velka = 0
pocet_velka_pismena = 0
cislice = 0
pocet_cislic = 0
oddelovac = 32*"-"
prihlasovaci_udaje = {"bob":"123", "ann":"pass123", "mike":"pasword123", "liz":"pass123" }
jmeno = input("Zadejte přihlašovací jméno: ")
heslo = input("Zadejte heslo: ")
if jmeno in prihlasovaci_udaje.keys() and prihlasovaci_udaje[jmeno] == heslo:
    print(f"{oddelovac}\n Welcome to the app, {jmeno}\n We have 3 texts to be analyzed.\n {oddelovac}")
    vyber=input("Enter a number btw. 1 and 3 to select: ")
    if not vyber.isdigit() or int(vyber) >= 4:
        print(f"Výběr musí být číslo 1,2 nebo 3")               
    else:
        print(oddelovac)
        slova_rozdelena = TEXTS[int(vyber)-1].split()
        pocet_slov = len(slova_rozdelena)
        for slovo in slova_rozdelena:
            slovo_ciste = slovo.strip(",.-")    
            if slovo_ciste.islower():
                pocet_mala_pismena += 1
            elif slovo_ciste.isupper() and slovo_ciste.isalpha():
                pocet_velka_pismena += 1                
            elif slovo_ciste.isdigit():
                slovo = int(slovo_ciste)
                cislice += slovo
                pocet_cislic += 1
            elif len(slovo_ciste) > 0 and slovo_ciste.istitle():
                pocet_zacinajici_velka += 1             
        print(f"There are {pocet_slov} words in the selected text.")
        print(f"There are {pocet_zacinajici_velka }titlecase words")
        print(f"There are {pocet_velka_pismena }uppercase words")
        print(f"There are {pocet_mala_pismena }lowercase words")
        print(f"There are {pocet_cislic }numeric strings")
        print(f"The sum of all numbers {cislice}.")
        print(oddelovac)
        print("LEN|  OCCURENCES  |NR.")
        print(oddelovac)
        delka_slov={}
        for slovo in slova_rozdelena:
            slovo=slovo.strip(",.-")
            if len(slovo) in delka_slov.keys():
                delka_slov[len(slovo)] += 1
            else:
                delka_slov[len(slovo)] = 1
        sorted_delka_slov = dict(sorted(delka_slov.items()))
        for delka,pocet in sorted_delka_slov.items():
            print(f"{delka:>3}|{pocet*"*":<15}|{pocet}")


else:
    print("unregistered user, terminating the program..")
