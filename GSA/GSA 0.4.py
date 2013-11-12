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

def jeLipotpuna(stanje):
        tmp = stanje.split('{')

        ime = tmp[0]

        #prvo vidi di je točka
        ind = ime.find('#')

        #je li na kraju,
        if ind+1 == len(ime):
            return 1
        else:
            return 0


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

    lsTrenutnihStanja = []
    lista = []
    stanja = []

    #u lsTrenutnihStanja dodaj pocetna stanja

    lsPocetNezavrsni = [pocetni_nezavrsni,'->','#']
    #print lsPocetNezavrsni

    for i in range(len(mapa[pocetni_nezavrsni])):
        lsTrenutnihStanja.append(mapa[pocetni_nezavrsni][i])

    #stvori dka
    dka = Dka()

    enka = Enka(mapa,listaPraznih,dictZapocinje,zavrsni)

    for i in range(len(lsTrenutnihStanja)):
        lsTrenutnihStanja[i] = lsPocetNezavrsni + lsTrenutnihStanja[i]
        #usput popuni listu listu
        lista.append('%')
        stanja.append(enka.stvoriStanje(lsTrenutnihStanja[i],lista[i]))


    i = 0
    while i < len(stanja):
        primljeno = []
        primljeno = enka.nadiEpsPoc(stanja[i],dka)
        if primljeno[0] == '#' or primljeno[0] == '{':
            i+=1
            continue
        #dodaje novonastalu listu listi stanja
        stanja.extend(primljeno)
        #izlazi iz petlje kad su u listi stanja sva stanja u koje se dolazi eps prijelazom
        #duljina liste se povecava za 1,
        i += 1




    #dodaj novu produkciju u mapu
    ls_poc_nez = []
    ls_poc_nez.append(pocetni_nezavrsni)
    mapa['<NoviNezZnak>'] = ls_poc_nez

    #namjesti da za pročitan stari nezavrsni znak ude se u stanja...
    NovoNez = []
    NovoNez.append('<NoviNezZnak>->#'+pocetni_nezavrsni+'{%}')
    dka.dodajLStanje(NovoNez)
    dka.dodajZnak(pocetni_nezavrsni)
    dka.dodajDStanje(stanja)

    #makni znak eps tamo di je tocka (#) dosla na kraj
    for i in range(len(stanja)):
        pom = stanja[i]
        broj = pom.find('#$')
        if broj != -1:
            pom = pom.replace("#$","#")
            stanja[i] = pom

    print dictZapocinjeZnakom
    print mapa
    print stanja

    #sada imam nekakvu pocetnu listu stanja u kojima sam trenutno
    #idem od svih pocetnih stanja

    for stanje in stanja:
        received = []
        received = enka.nadiPrijelaz(stanje,stanja,dka)
        if received[0] == '{':
            continue
        dka.dodajLStanje(stanja)
        dka.dodajZnak(received[1])
        dka.dodajDStanje(received[0])
        if isinstance(received[0], str):
            potpuna = jeLipotpuna(received[0])
            if not potpuna:
                pass
            else:
                dka.dodajLStanje(received[0])
                dka.dodajZnak(received[1])
                dka.dodajDStanje(received[0])

    print dka.prijelazi




if __name__ == '__main__':
  main()


