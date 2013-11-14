# -*- coding: utf-8 -*-
"""
@author: Matko
"""



class Dka(object):

    prijelaziDka = []


    def __init__(self,prijelazi,stanja):
        self.prijelazi = prijelazi
        self.stanja = stanja

    def cash_prijelaz(self,stanja,mapa):
        novaS = stanja
        novaS3 = []
        zarez = ','
        cash = '$'
        added = 0

        for tempS in stanja:
            kljuc = tempS+zarez+cash
            if kljuc in mapa:
                novaS3.append(mapa[kljuc])
            del kljuc
        if novaS3 not in novaS:
            novaS.append(novaS3)
            added = 1
        if added == 1:
            tmp = []
            tmp.append(novaS)
            novaS = self.cash_prijelaz(tmp,mapa)
        return novaS

    def stvoriDict(self,prijelazi):
        dict = {}
        for red in prijelazi:
            dijeli1 = red.split('BEL')
            dict[dijeli1[0]] = dijeli1[1]
        return dict


    def stvoriDka(self):
        prijelazi = ''.join(self.prijelazi)
        prijelazi = prijelazi.split('|')
        dict = self.stvoriDict(prijelazi)
        print dict
        listaListaStanja = []
        for red in prijelazi:
            print red
            tmp = []
            dijeli1 = red.split('BEL')
            lijevo1 = ''.join(dijeli1[0])
            dijeli2 = lijevo1.split(',')
            prvo = dijeli2[0]
            znak = dijeli2[1]
            ls = []
            ls.append(prvo)
            print znak
            if znak == '$':
                tmp = self.cash_prijelaz(ls,dict)
                print tmp








