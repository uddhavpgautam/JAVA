# -*- coding: utf-8 -*-
"""
@author: Matko
"""



class Dka(object):

    prijelazi = []


    def __init__(self):
        pass

    def dodajLStanje(self,stanja):
        self.prijelazi.append(stanja)
        self.prijelazi.append(',')
    def dodajZnak(self,znak):
        self.prijelazi.append(znak)
        self.prijelazi.append('->')
    def dodajDStanje(self,stanja):
        self.prijelazi.append(stanja)
        self.prijelazi.append('|')

