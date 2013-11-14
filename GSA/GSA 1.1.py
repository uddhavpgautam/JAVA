# -*- coding: utf-8 -*-
"""
@author: Matko

"""

import sys
import copy

from enka import Enka
from dka import Dka
from TablicaAkcija import TablicaAkcija
from TablicaNovoStanje import TablicaNovoStanje


def nadiZvjezdice(znak,dict):
    #prima liejvi znak i dictIzravnoZnakom, a vraća listu (desnu stranu jedinice i zvijedzdice)
    ret = []
    ret += dict[znak]
    for kzna in ret:
        if kzna in zavrsni:
            pass
        else:
            tmp = []
            tmp = nadiZvjezdice(kzna,dict)
            ret.extend(tmp)
    return ret

def main ():
    #print "HelloWorld"
    #print "Ovo je promjena"

    ulaz = open('ulaznaKnjiga','r')

    #učitavanje prva 3 reda

    nezavrsni = ulaz.readline().split(' ')
    del nezavrsni[0]
    nezavrsni [-1] = nezavrsni[-1].strip()
    pocetni_nezavrsni = nezavrsni[0]

    global zavrsni
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

    #dodaj novu produkciju u mapu
    ls_poc_nez = []
    ls_poc_nez.append(pocetni_nezavrsni)
    mapa['<NoviNezZnak>'] = []
    mapa['<NoviNezZnak>'].append(ls_poc_nez)

    listaPraznih = []
    # Popuni listu praznih znakova s lijevim stranam eps produkcija
    for znak in mapa:
        for item in mapa[znak]:
            if item[0] == '$':
                listaPraznih.append(znak)

    #provjeri ima li jos praznih

    while 1:
        added = 0
        for lijevo in mapa:
            if lijevo in listaPraznih:
                continue
            for desno in mapa[lijevo]:
                for clan in desno:
                    if clan not in listaPraznih:
                        added = 0
                        break
                    added = 1
                if added:
                    break
            if added:
                listaPraznih.append(lijevo)
        if not added:
            break

    #računanje započinje izravno znakom
    dictZapocinjeIzravno= {}

    for lijevo in mapa:
        tmp = []
        for desno in mapa[lijevo]:
            if desno[0] == '$':
                continue
            elif desno[0] in listaPraznih:
                if len(desno)>= 2:
                    tmp.append(desno[1])
            tmp.append(desno[0])
        dictZapocinjeIzravno[lijevo] = tmp

    #računanje započinje znakom
    dictZapocinjeZnakom = {}

    for lijevo in dictZapocinjeIzravno:
        zvjezdiceIjedinice = []
        zvjezdiceIjedinice = nadiZvjezdice(lijevo,dictZapocinjeIzravno)
        dictZapocinjeZnakom[lijevo] = zvjezdiceIjedinice
        #ako je nema dodaj dijagonalu
        if lijevo not in dictZapocinjeZnakom[lijevo]:
            dictZapocinjeZnakom[lijevo].append(lijevo)
        #pobrisi duplikate
        dictZapocinjeZnakom[lijevo] = list(set(dictZapocinjeZnakom[lijevo]))

    #izračunaj skup započinje za svaki nezavrsni znak (samo izbaci nezavrsne iz desnih strana
    for lijevo in dictZapocinjeZnakom:
        dictZapocinjeZnakom[lijevo] = list(set(dictZapocinjeZnakom[lijevo]) - set(nezavrsni))


    dictZapocinje = {}
    dictZapocinje = dictZapocinjeZnakom

    # # - točka, $ eps, % znak za kraj (obrnuti T)

    #stvori dka
    dka = Dka()

    enka = Enka(mapa,listaPraznih,dictZapocinje,zavrsni)

    stanja = []
    prijelazi = []
    pocetnoStanje = '<NoviNezZnak>->#'+pocetni_nezavrsni+'{%}'
    stanja.append(pocetnoStanje)

    i = 0
    while i < len(stanja):
        primljenoE = []
        primljenoPiZnak = []

        primljenoPiZnak = enka.nadiPrijelaz(stanja[i],stanja,dka)
        if primljenoPiZnak[0] == '{':
            #nema prijelaza
            pass
        else:
            #dodaj u listu prijelaza staro stanje, znak i novo stanje ako
            prijelazi.append(stanja[i])
            prijelazi.append(',')
            prijelazi.append(primljenoPiZnak[1])
            prijelazi.append('BEL')
            prijelazi.append(primljenoPiZnak[0])
            prijelazi.append('|')

            #u listu stanja dodaj novo stanje samo ako vec nije u stanju
            if primljenoPiZnak[0] not in stanja:
                stanja.append(primljenoPiZnak[0])

        primljenoE = enka.nadiEpsPoc(stanja[i],dka)
        if primljenoE[0] == '#' or primljenoE[0] == '{':
            #nema epsilon prijelaza
            pass
        else:
            #u prijelaze dodaj primljena stanja
            for stanje in primljenoE:
                prijelazi.append(stanja[i])
                prijelazi.append(',')
                prijelazi.append('$')
                prijelazi.append('BEL')
                prijelazi.append(stanje)
                prijelazi.append('|')

                if stanje not in stanja:
                    stanja.append(stanje)
        i += 1

    print mapa
    print prijelazi
    print stanja


if __name__ == '__main__':
  main()


