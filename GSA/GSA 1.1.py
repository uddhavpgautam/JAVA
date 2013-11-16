# -*- coding: utf-8 -*-
"""
@author: Matko

"""

import sys
import copy
import os

from enka import Enka
from dka import Dka

def nadiEpsOkr(stanja,mapa):
    novaS = stanja
    novaS3 = []
    zarez = ','
    cash = '$'
    added = 0

    for tempS in stanja:
        kljuc = tempS+zarez+cash
        if kljuc in mapa:
            novaS3.extend(mapa[kljuc])
        del kljuc
    for tempS1 in novaS3:
        if tempS1 not in novaS:
            novaS.append(tempS1)
            added = 1
    if added == 1:
        novaS = nadiEpsOkr(novaS,mapa)
    return novaS

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

    TablicaAkcija = open(os.path.join('analizator','TablicaAkcija.txt' ), "w")
    TablicaNovoStanje = open(os.path.join('analizator','TablicaNovoStanje.txt' ), "w")
    Sinkronizacijski = open(os.path.join('analizator','Sinkronizacijski.txt' ), "w")

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

    znakovi = zavrsni+nezavrsni

    sinkronizacijski = ulaz.readline().split(' ')
    del sinkronizacijski[0]
    sinkronizacijski [-1] = sinkronizacijski[-1].strip()

    sinkronizacijski = ' '.join(sinkronizacijski)
    Sinkronizacijski.write(sinkronizacijski)

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

    enka = Enka(mapa,listaPraznih,dictZapocinje,zavrsni)

    stanja = []
    prijelazi = []
    pocetnoStanje = '<NoviNezZnak>->#'+pocetni_nezavrsni+'{%}'
    stanja.append(pocetnoStanje)

    i = 0
    while i < len(stanja):
        primljenoE = []
        primljenoPiZnak = []

        primljenoPiZnak = enka.nadiPrijelaz(stanja[i])
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

        primljenoE = enka.nadiEpsPoc(stanja[i],prijelazi)
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

    del prijelazi[-1]
    prijelazi = ''.join(prijelazi)

    prijelazi = prijelazi.split('|')

    dictPrijelazi = {}
    for line in prijelazi:
        #razdijeli key od value
        strCmp = line.split("BEL")
        key  = strCmp [0]
        value = strCmp[1:]
        tmp = ''.join(value)
        if key in dictPrijelazi:
            dictPrijelazi[key].append(tmp)
        else:
            dictPrijelazi[key] = value

    listaDKA = []

    #prvo nadi eps okruzenje svakog stanja, a onda sredi hijerarhiju
    for stanje in stanja:
        trenS = []
        trenS.append(stanje)
        trenS = nadiEpsOkr(trenS,dictPrijelazi)
        listaDKA.append(trenS)

    brojevi = []

    for stanja in listaDKA:
        i = 0
        for stanje in stanja:
            i +=1
        brojevi.append(i)

    yx = zip(brojevi,listaDKA)
    yx.sort(reverse = True)

    listaDKANew = [x for y, x in yx]

    listaDKAfinal = []

    #riješavanje manjih eps okruženja
    for stanja in listaDKANew:
        dodaj = 1
        for stanja1 in listaDKAfinal:
            for stanje in stanja:
                if stanje not in stanja1:
                    dodaj = 1
                    break
                dodaj = 0
            if dodaj == 0:
                break

        if dodaj:
            listaDKAfinal.append(stanja)

    dictDKA = {}

    i = -1
    for stanja in listaDKAfinal:
        i +=1
        dictDKA[i] = stanja

    print dictDKA
    print dictPrijelazi

    #najprije dodajem pomakni, a onda i reduciraj određenim redosljedom tako da se izbjegnu nejednoznačnosti

    #napravi tablicuAkcija, prvo pomakni, a onda i reduciraj
    for kljuc in dictDKA:
        for znak in zavrsni:
            for stanje in dictDKA[kljuc]:
                tmp = stanje+','+znak
                if tmp in dictPrijelazi:
                    #ukoliko nađeš prijelaz pogledaj gdje ideš, ideš u samo jedno
                    #stanje, nađi u kojem je DKA stanju to stanje
                    odrediste = dictPrijelazi[tmp]
                    odrediste = ''.join(odrediste)
                    for key in dictDKA:
                        if odrediste in dictDKA[key]:
                            odredisteDKA = key
                            break
                    ispis = str(kljuc)+' '+znak+' Pomakni '+str(odredisteDKA)
                    TablicaAkcija.write(ispis)
                    TablicaAkcija.write('\n')
                else:
                    pass
                    #inače odbaci, odnosno "ostavi to mejsto u tablici prazbno
                    #ne zapisuj ništa u datoteku


    ulaz.close()
    TablicaAkcija.close()
    TablicaNovoStanje.close()
    Sinkronizacijski.close()


if __name__ == '__main__':
  main()


