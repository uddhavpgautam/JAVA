# -*- coding: utf-8 -*-
"""
@author: Matko
"""



class Dka(object):

    prijelaziDka = []


    def __init__(self,prijelazi,stanja):
        self.prijelazi = prijelazi
        self.stanja = stanja

    def stvoriDict(self,prijelazi):
        dict = {}
        for red in prijelazi:
            print red
            dijeli1 = red.split('BEL')
            dict[dijeli1[0]] = dijeli1[1]
        return dict

    def nadiEps(self,stanje,prijelazi,dict):


    def stvoriDka(self):
        prijelazi = ''.join(self.prijelazi)
        print prijelazi
        prijelazi = prijelazi.split('|')
        dict = self.stvoriDict(prijelazi)

        listaListaStanja = []
        for red in prijelazi:
            tmp = []
            print red
            dijeli1 = red.split('BEL')
            lijevo1 = ''.join(dijeli1[0])
            dijeli2 = lijevo1.split(',')
            prvo = dijeli2[0]
            znak = dijeli2[1]

            if znak == '$':
                tmp = self.nadiEps(prvo,prijelazi,dict)







