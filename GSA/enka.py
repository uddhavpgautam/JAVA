# -*- coding: utf-8 -*-
"""
@author: Matko
"""

from dka import Dka

class Enka(object):


    def __init__(self,mapa,listaPraznih,dictZapocinje,zavrsni):
        self.mapa = mapa
        self.listaPraznih = listaPraznih
        self.dictZapocinje = dictZapocinje
        self.zavrsni = zavrsni

    def stvoriStanje(self,ime,lista):
        stanje = ''
        lista = list(lista)
        stanje += ''.join(ime)
        stanje += '{'
        stanje += ''.join(lista)
        stanje += '}'
        return stanje

    def nadiEpsPoc(self,stanje):
        #dobiva jedno stanje
        #nalazi sva stanja u koje se prelazi eps prijalzima iz tog stanja (samo prvu razinu)
        #vraća string svih stanja u koje se prešlo odvojenih znakom '|'

        tmp = stanje.split('{')
        lista = list(tmp[1])
        del lista[-1]

        ime = tmp[0]

        #prvo vidi di je točka
        ind = ime.find('#')

        #je li na kraju,
        falseRet = []
        if ind+1 == len(ime):
            falseRet.append('{')
            return falseRet
        #ili je poslije nje zavrsni znak
        elif ime[ind+1] != '<':
            falseRet.append('#')
            return falseRet
        #ako smo tu u kodu znaci da slijedi nezavrsni znak
        #pogledaj koji je to znak

        znak1 = list(ime)
        del znak1 [:ind+1]
        znak1 = ''.join(znak1)
        ind = znak1.find('>')
        znak1 = list(znak1)
        del znak1 [ind+1:]
        znak1 = ''.join(znak1)
        #u znak1 je sada znak koji moramo obraditi


        #opcija 1
        """
        #provjeri ide li nakon njega nezavrsni znak i ako da koji, a prvo vidi je li poslije njega kraj
        ind = ime.find('#<')
        znak2 = list(ime)
        del znak2 [:ind+1]
        znak2 = ''.join(znak2)
        ind = znak2.find('>')
        znak2 = list(znak2)


        if ind+1 == len(znak2) or znak2[ind+1] != '<':
            #u listi ostaju isti znakovi
            pass
        else:
            #u listu dodaj znakove iz skupova praznih znakova i skupa zapocinje (točke 4.c.1,4.c.2 iz udžbenika str. 148)
            znak2 = ''.join(znak2)
            ind = znak2.find('>')
            znak2 = list(znak2)
            del znak2 [:ind+1]
            del znak2 [ind+1:]
            znak2 = ''.join(znak2)
            #dodaj te znakove u listu... - FALI KOD
            lista.extend(self.dictZapocinje[znak2])


        #opcija 2

        lista = []
        ind = ime.find('#<')
        znak2 = list(ime)
        del znak2 [:ind+1]
        znak2 = ''.join(znak2)
        indPom = znak2.find('>')
        znak2 = list(znak2)
        print 'znak2'
        print znak2

        if indPom+1 == len(znak2):
            #ako nije ništa ostalo u znaku, točka je došla do kraja
            lista.append('%')
        else:
            #inače provjeri skup započinje od zanka2 (ono što je ostalo desno od točke)
        """

        #opcija 3
        #provjeri ide li nakon njega nezavrsni znak i ako da koji, a prvo vidi je li poslije njega kraj
        ind = ime.find('#<')
        znak2 = list(ime)
        del znak2 [:ind+1]
        znak2 = ''.join(znak2)
        ind = znak2.find('>')
        znak2 = list(znak2)
        lista = []
        if ind+1 == len(znak2):
            lista.append('%')
        else:
            for i in range(len(znak2)):
                if znak2[i] == '>':
                    znak2.insert(i+1,' ')
            znak2 = ''.join(znak2)
            znakovi = znak2.split(' ')
            for item in znakovi:
                if item in self.listaPraznih:
                   lista.append('%')
                if item in self.zavrsni:
                    lista.append(item)
                elif item in self.dictZapocinje:
                    lista.extend(self.dictZapocinje[item])

        #pobrisi duplikate
        lista = list(set(lista))

        #u znak1 je sada znak za koji moramo stvoriti nova stanja, a u listi je ono što im pridružujemo

        lsTrenutnihStanja = []
        stanja = []

        for i in range(len(self.mapa[znak1])):
            lsTrenutnihStanja.append(self.mapa[znak1][i])

        lsZnak1 = [znak1, '->', '#']

        for i in range(len(lsTrenutnihStanja)):
            lsTrenutnihStanja[i] = lsZnak1 + lsTrenutnihStanja[i]
            stanja.append(self.stvoriStanje(lsTrenutnihStanja[i], lista))
        return stanja


    def nadiEps(self,stanje):
        pass






    def nadiPrijelaz(self,stanje):
        #funkcija dobiva jedno stanje i vraca jedno stanje u koje je presla zbog procitanog znaka
        #pomaknute tocke, pritom ne mijenja listu
        #dodatno vraca i znak (bilo zavrsni ili nezavrsni) koji je procitala kao drugi clan liste
        ind = stanje.find('#')
        falseRet = []

        #ako nema prijelaza
        if stanje[ind+1] == '{':
            falseRet.append('{')
            return falseRet

        #inače generiraj novo stanje
        staro = ''
        staro += stanje

        staro = list(staro)
        prviDio = staro[:ind]
        prviDio = ''.join(prviDio)
        del staro[:ind+1]
        staro = ''.join(staro)

        znak = ''

        if stanje[ind+1] == '<':
            ind2 = staro.find('>')
            staro = list(staro)
            staro.insert(ind2+1,'#')
            staro = ''.join(staro)
            znak = staro[:ind2+1]
        else:
            ind3 = staro.find('<')
            ind4 = staro.find('{')
            if ind3 != -1:
                staro = list(staro)
                staro.insert(ind3,'#')
                staro = ''.join(staro)
                znak = staro[:ind3]
            elif ind4 != -1:
                staro = list(staro)
                staro.insert(ind4,'#')
                staro = ''.join(staro)
                znak = staro[:ind4]

        novo = prviDio+staro
        ret =[]
        ret.append(novo)
        ret.append(znak)
        return novo
















