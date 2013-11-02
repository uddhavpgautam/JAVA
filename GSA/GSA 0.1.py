# -*- coding: utf-8 -*-
"""
@author: Matko
"""


def main ():
    print "HelloWorld"
    print "Ovo je promjena"

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
    print mapa






if __name__ == '__main__':
  main()


