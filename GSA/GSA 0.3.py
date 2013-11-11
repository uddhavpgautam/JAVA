# -*- coding: utf-8 -*-
"""
@author: Matko

"""

import sys
from enka import Enka
from dka import Dka

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

    listaPraznih = []
    # Popuni listu praznih znakova.
    for znak in mapa:
        for item in mapa[znak]:
            if item[0] == '$':
                listaPraznihZnakova.append(znak)

    listaPraznih = []
    dictZapocinje = {}

    # # - točka, $ eps, % znak za kraj (obrnuti T)

    lsTrenutnihStanja = []
    lista = []
    stanja = []

    #u lsTrenutnihStanja dodaj pocetna stanja

    lsPocetNezavrsni = [pocetni_nezavrsni,'->','#']
    #print lsPocetNezavrsni

    for i in range(len(mapa[pocetni_nezavrsni])):
        lsTrenutnihStanja.append(mapa[pocetni_nezavrsni][i])


    enka = Enka(mapa,listaPraznih,dictZapocinje)

    for i in range(len(lsTrenutnihStanja)):
        lsTrenutnihStanja[i] = lsPocetNezavrsni + lsTrenutnihStanja[i]
        #usput popuni listu listu
        lista.append('%')
        stanja.append(enka.stvoriStanje(lsTrenutnihStanja[i],lista[i]))

    i = 0
    while i < len(stanja):
        primljeno = []
        primljeno = enka.nadiEpsPoc(stanja[i])
        if primljeno[0] == '#' or primljeno[0] == '{':
            i+=1
            continue
        #dodaje novonastalu listu listi stanja
        stanja.extend(primljeno)
        #izlazi iz petlje kad su u listi stanja sva stanja u koje se dolazi eps prijelazom
        #duljina liste se povecava za 1,
        i += 1

    #dodaj novu produkciju u mapu i stanja
    ls_poc_nez = []
    ls_poc_nez.append(pocetni_nezavrsni)
    mapa['<NoviNezZnak>'] = ls_poc_nez
    tmp = '<NoviNezZnak>->#'+pocetni_nezavrsni+'{%}'
    stanja.append(tmp)

    #stvori dka
    dka = Dka()

    #makni znak eps tamo di je tocka (#) dosla na kraj
    for i in range(len(stanja)):
        pom = stanja[i]
        broj = pom.find('#$')
        if broj != -1:
            pom = pom.replace("#$","#")
            stanja[i] = pom

    print mapa
    print stanja

    #sada imam nekakvu pocetnu listu stanja u kojima sam trenutno
    #idem od svih pocetnih stanja
























if __name__ == '__main__':
  main()


