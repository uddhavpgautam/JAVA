# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 20:28:01 2013

@author: Antec
"""
prijelaziDict = {}
# Funkcija kojom se prijelazi iz prve liste dodaju u rjecnik.
def dodajPrijelaz(elt):
    kljuc = elt.split("->")[0]
    value = elt.split("->")[1]
    prijelaziDict[kljuc] = value
# Funkcija kojom cemo provjeravati postoji li odredjeni prijelaz.
# Vraca listu stanja ako postoje, inace vraca praznu listu.
def traziPrijelaz(stanja, znak):
    povratnaLista = []
    for x in stanja:
        kljuc = x + ',' + znak
        if kljuc not in prijelaziDict:
            a = 0
        else:
            pom = prijelaziDict[kljuc]
            for x in pom:
                povratnaLista.append(x)
    return povratnaLista
        
def traziEpsPrijelaz(stanja):
    povratnaLista = []
    for x in stanja:
        kljuc = x + ',$'
        if kljuc not in prijelaziDict:
            a = 0
        else:
            pom = prijelaziDict[kljuc]
            for x in pom:
                povratnaLista.append(x)
    return povratnaLista
            
# Uzima dictionary sa prijelazima, pocetno stanje te LISTU ulaznih,
# znakova.
def eNKA(prijelaziDict, pocStanje, ulazniZnakovi):
    trenStanja = []
    novaTrenStanja = []
    for znak in ulazniZnakovi:
        trenStanja.append(pocStanje)
        if traziEpsPrijelaz(trenStanja):
            novaTrenStanja = traziEpsPrijelaz(trenStanja)
            print novaTrenStanja
            
        for st in novaTrenStanja:
            del trenStanja[0:len(trenStanja)]
            trenStanja = traziPrijelaz(st, znak)
            
        if traziEpsPrijelaz(trenStanja):
            novaTrenStanja = traziEpsPrijelaz(trenStanja)
            print novaTrenStanja
    print trenStanja


ulaznaDat = open('datoteka.txt', 'r')

# ulazniPodaci = lista u kojoj se nalaze linije ulazne datoteke ['','','']
sviUlazniPodaci = ulaznaDat.readlines()
#print sviUlazniPodaci
i = 0
# Lista prijelaza.
prvaLista = [] 
# Lista stanja analizatora, prihvatljivog i pocetnog stanja
# automata.
drugaLista = []
# Format upisa iz datoteke u liste.
for i in range(len(sviUlazniPodaci)):
    prvaLista.append(sviUlazniPodaci[i].split("__")[0])
    drugaLista.append(sviUlazniPodaci[i].split("__")[1])
    i += 1

i = 0
for i in range(len(prvaLista)):
    prvaLista[i] = prvaLista[i].split("|")
    prvaLista[i] = prvaLista[i][:-1]
    i += 1
    
i = 0
for i in range(len(drugaLista)):
    drugaLista[i] = drugaLista[i].split("|")
    i += 1
    
print prvaLista
#print drugaLista

for item in prvaLista:
    for element in item:
        dodajPrijelaz(element)