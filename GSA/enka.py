# -*- coding: utf-8 -*-
"""
@author: Matko
"""



class Enka(object):


    def __init__(self,mapa,listaPraznih,dictZapocinje):
        self.mapa = mapa
        self.listaPraznih = listaPraznih
        self.dictZapocinje = dictZapocinje

    def stvoriStanje(self,ime,lista):
        stanje = ''
        lista = list(lista)
        stanje += ''.join(ime)
        stanje += '{'
        stanje += ''.join(lista)
        stanje += '}'
        return stanje

    def nadiEps(self,stanje):
        #dobiva jedno stanje
        #nalazi sva stanja u koje se prelazi eps prijalzima iz tog stanja (samo prvu razinu)
        #vraća string svih stanja u koje se prešlo odvojenih znakom '|'

        tmp = stanje.split('{')
        lista = list(tmp[1])
        del lista[-1]

        ime = tmp[0]

        #prvo vidi di je točka
        ind = ime.find('#')

        #je li na kraju, ili je poslije nje zavrsni znak, ako je vrati #
        falseRet = []
        if ind+1 == len(ime) or ime[ind+1] != '<':
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












