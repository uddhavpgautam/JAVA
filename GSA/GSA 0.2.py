# -*- coding: utf-8 -*-
"""
@author: Matko
"""

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

    ulaz = open('Ulazna.txt','r')

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
    #print mapa
    
    listaPraznihZnakova = []
    # Popuni listu praznih znakova.
    for znak in mapa:
        for item in mapa[znak]:
            if item[0] == '$':
                listaPraznihZnakova.append(znak)
    
    # Provjeravamo krajnje lijeve znakove desne strane.
    relacijaPrva = {}
    zapocinjeIzravnoZnakom(listaPraznihZnakova, relacijaPrva, mapa, zavrsni)
    print relacijaPrva




if __name__ == '__main__':
  main()


