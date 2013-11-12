# -*- coding: utf-8 -*-
"""
@author: Matko
"""



class Dka(object):

    prijelazi = []


    def __init__(self):
        pass

    def dodajLStanje(self,stanja):
        if isinstance(stanja,str):
            self.prijelazi.append(stanja)
        else:
            for stanje in stanja:
                self.prijelazi.append(stanje)
        self.prijelazi.append(',')
    def dodajZnak(self,znak):
        self.prijelazi.append(znak)
        self.prijelazi.append('->')
    def dodajDStanje(self,stanja):
        if isinstance(stanja,str):
            self.prijelazi.append(stanja)
        else:
            for stanje in stanja:
                self.prijelazi.append(stanje)
        self.prijelazi.append('|')

