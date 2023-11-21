def elsoFeladat():
    hettelOszthato = 0
    index = 0
    while index < 1001:
        if index % 7 == 0:
            hettelOszthato += 1
        index+=1

    print(f"Ennyi 7-el oszthato van: {hettelOszthato}")


def masodikFeladat():
    tizenkettovelOszthato= 0
    index = 2000
    while index <= 20000:
        if index % 12 == 0:
            tizenkettovelOszthato += 1
        index+=1
    print(f"Ennyi szam oszthato 12-vel {tizenkettovelOszthato}")


def harmadikFeladat():
    osszeg = 0
    index = 0
    while index < 21:
        haromOszthato = index * 3
        osszeg += haromOszthato ** 2
        index += 1
    print(f"Harommal oszthato 1. 20 negyzete: {osszeg} db")

def negyedikFeladat():
    szam = int(input("Szeretnek kerni egy egesz szamot: "))
    listaOszthatok = []
    index = 1
    while index <= szam:
        if szam % index == 0:
            listaOszthatok.append(index)
        index+=1
    print(f"Oszthatok: {listaOszthatok}")

def otodikFeladat():
    max = 0
    szam = int(input("Szeretnek kerni egy szamot: "))
    index = 1
    while index <= szam:
        if szam % index == 0:
            if max < index:
                max = index
        index+=1
    print(f"legnagyobb osztoja: {max}")


def hatodikFeladat():
    szam = int(input("Kerek egy szamot, hogy megnezzem primszam e: "))
    if szam > 1:
        for i in range(2, int(szam ** 0.5) + 1):
            if szam % i == 0:
                print(f"Nem {szam} <- ez nem egy prímszám")
                
        else:
            print(f"Igen {szam} <- ez egy prímszám")
    else:
        print(f"Nem {szam} <- ez nem egy prímszám")

def hetedikFeladat():
    negyzetSzamDb = 0
    index = 0
    while index < 100001:
        negyzet = index ** 2
        if negyzet <= 100000:
            negyzetSzamDb += 1
        index+=1
    print(f"Ennyi negyzetszam: {negyzetSzamDb}")

def nyolcadikFeladat():
    negyzetSzamDb = 0
    index = 1
    while index ** 2 <= 100000:
        negyzetSzamDb += 1
        index+=1
    print(f"Ennyi negyzetszam: {negyzetSzamDb}")


def kilencedikFeladat():
    negyzetSzamokOsszge = 0
    index = 0
    while index < 10001:
        negyzetszam = index ** 2
        negyzetSzamokOsszge += negyzetszam
        index+=1
    print(f"Ennyi a vegosszege: {negyzetSzamokOsszge}")







