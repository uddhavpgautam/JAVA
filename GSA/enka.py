# -*- coding: utf-8 -*-
"""
@author: Matko
"""



class Enka(object):


    def __init__(self):
        pass

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

        #je li na kraju, ili je poslije nje zavrsni znakako je vrati #
        if ind+1 == len(ime) or ime[ind+1] != '<':
            return '#'

        #ako smo tu u kodu znaci da slijedi nezavrsni znak
        #pogledaj koji je to znak

        znak1 = list(ime)
        del znak1 [:ind+1]
        znak1 = ''.join(znak1)
        ind = znak1.find('>')
        znak1 = list(znak1)
        del znak1 [ind+1:]
        znak1 = ''.join(znak1)
        print ime
        #u znak1 je sada znak koji moramo obraditi

        #provjeri ide li nakon njega nezavrsni znak i ako da koji
        ind = ime.find('#<')
        znak2 = list(ime)
        del znak2 [:ind+1]
        znak2 = ''.join(znak2)
        ind = znak2.find('>')
        znak2 = list(znak2)
        if znak2[ind+1] != '<':
            pass
        else:
            znak2 = ''.join(znak2)
            ind = znak2.find('>')
            znak2 = list(znak2)
            del znak2 [:ind+1]
            del znak2 [ind+1:]
            znak2 = ''.join(znak2)

        print znak1
        print znak2











