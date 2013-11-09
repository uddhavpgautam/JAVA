# -*- coding: utf-8 -*-
"""
@author: Matko

"""

import sys
from enka import Enka

# Ako je prazan vraca 1.
def jeliPrazan(lista, element):
    if element not in lista:
        return 0
    else:
        return 1

# Ako je zavrsan vraca 1.
def jeliZavrsan(zavrsni, znak):
    if znak not in zavrsni:
        return 0
    else:
        return 1
# Poziva se sa parametrima liste praznih znakova, listom relacija, mapom sa
# prijelazima, te listom zavrsnih znakova.
# Funkcija provjerava jeli prvi znak eps, ako nije provjerava jeli prvi znak
# zavrsan, prazan, te prema tome odredjuje spada li on u listu relacija.
# Gradivo na 101. stranici udzbenika:
# Racunanje relacije ZapocinjeIzvravnoZnakom
def zapocinjeIzravnoZnakom(listaP, listaR, mapa, zavrsni):
    for znak in mapa:
        listaR[znak] = []
        for item in mapa[znak]:
            for element in item:
                if element == '$':
                    break
                if jeliPrazan(listaP, element) == 0 and jeliZavrsan(zavrsni, item) == 0:
                    listaR[znak].append(element)
                    break
                elif jeliPrazan(listaP, element) == 0 and jeliZavrsan(zavrsni, item) == 1:
                    listaR[znak].append(element)
                    break
                elif jeliPrazan(listaP, element) == 1:
                    listaR[znak].append(element)
                

def main ():
    #print "HelloWorld"
    #print "Ovo je promjena"

    ulaz = open('ulaznaKnjiga','r')

    #učitavanje prva 3 reda

    nezavrsni = ulaz.readline().split(' ')
    del nezavrsni[0]
    nezavrsni [-1] = nezavrsni[-1].strip()
    pocetni_nezavrsni = nezavrsni[0]

    zavrsni = ulaz.readline().split(' ')
    del zavrsni[0]
    zavrsni [-1] = zavrsni[-1].strip()

    sinkronizacijski = ulaz.readline().split(' ')
    del sinkronizacijski[0]
    sinkronizacijski [-1] = sinkronizacijski[-1].strip()

    mapa = {}

    #sredi produkcije
    while 1:
        red = list(ulaz.readline())
        if not red:
            break

        #pobrisi znak za novi red
        del red [-1]

        #provjeri prvi znak reda

        if red[0] == '<':
            lijevaStrana = ''.join(red)
            if lijevaStrana in mapa:
                pass
            else:
                mapa[lijevaStrana] = []
            continue

        else:
            del red[0]
            tmp = ''.join(red)
            desnaStrana = tmp.split(' ')
            mapa[lijevaStrana].append(desnaStrana)
    
    listaPraznihZnakova = []
    # Popuni listu praznih znakova.
    for znak in mapa:
        for item in mapa[znak]:
            if item[0] == '$':
                listaPraznihZnakova.append(znak)
    
    # Provjeravamo krajnje lijeve znakove desne strane.
    relacijaPrva = {}
    zapocinjeIzravnoZnakom(listaPraznihZnakova, relacijaPrva, mapa, zavrsni)
    #print relacijaPrva


    listaPraznih = []
    dictZapocinje = {}
    print mapa

    #točka će biti #,eps prijelaz $,% znak za kraj (obrnuti T)

    lsTrenutnihStanja = []
    lista = []
    stanja = []

    #u lsTrenutnihStanja dodaj pocetna stanja

    lsPocetNezavrsni = [pocetni_nezavrsni,'->','#']
    #print lsPocetNezavrsni

    for i in range(len(mapa[pocetni_nezavrsni])):
        lsTrenutnihStanja.append(mapa[pocetni_nezavrsni][i])

    #print lsTrenutnihStanja
    enka = Enka(mapa,listaPraznih,dictZapocinje)

    for i in range(len(lsTrenutnihStanja)):
        lsTrenutnihStanja[i] = lsPocetNezavrsni + lsTrenutnihStanja[i]
        #usput popuni listu listu
        lista.append('%')
        stanja.append(enka.stvoriStanje(lsTrenutnihStanja[i],lista[i]))


    i = 0
    while i < len(stanja):
        primljeno = []
        primljeno = enka.nadiEps(stanja[i])
        if primljeno[0] == '#':
            i+=1
            continue
        print stanja
        #dodaje novonastalu listu listi stanja
        stanja.extend(primljeno)
        print stanja
        #izlazi iz petlje kad su u listi stanja sva stanja u koje se dolazi eps prijelazom
        #duljina liste se povecava za 1,
        i += 1

















if __name__ == '__main__':
  main()


