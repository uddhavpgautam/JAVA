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
                novaS3.extend(mapa[kljuc])
            del kljuc
        for tempS1 in novaS3:
            if tempS1 not in novaS:
                novaS.append(tempS1)
                added = 1
        if added == 1:
            novaS = cash_prijelaz(novaS,mapa)
        return novaS

    def stvoriDict(self,prijelazi):
        pass


    def stvoriDka(self):
        pass









