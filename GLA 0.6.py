# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 23:36:19 2013

@author: Matko
"""

import sys

class Automat(object):
    
    """Nacrt za sve $-NKA automate koji će se ostvarivati """
    
    def __init__(self):
        pass
    
    br_stanja = 0
    
    def novo_stanje(self):
        self.br_stanja = self.br_stanja + 1
        return self.br_stanja - 1 
    def dodaj_eps(self,c,d):
        pass
    def dodaj_prijelaz(self,c,d,z):
        pass
    
        
def je_operator(izraz,i):
    br = 0
    while i-1 >= 0 and izraz[i] == '\':  #ili ide '\\' ili '\'
        br = br+1
        i = i-1
    return br%2 == 0    
    
def pretvori(izraz,automat,tablica):
    izbori = []
    br_zagrada = 0
    j = 0
    for i in range(len(izraz)):
        if izraz[i] == '(' and je_operator (izraz,i):
            br_zagrada = br_zagrada + 1
        elif izraz[i] == ')' and je_operator(izraz,i):
            br_zagrada = br_zagrada - 1
        elif br_zagrada == 0 and izraz [i] == '|' and je_operator(izraz,i):
            izbori[j] = izraz[:i]
            j += 1
    
    lijevo_stanje = automat.novo_stanje()
    desno_stanje = automat.novo_stanje()
    
    if j != 0:
        pass
    else:
        prefiksirano = 0
        zadnje_stanje = lijevo_stanje
        for i in range(len(izraz)):
            a = 0
            b = 0
            if prefiksirano:
                prefiksirano = 0
                prijelazni_znak = ""
                if izraz[i] == 't':
                    prijelazni_znak = '\t'
                elif izraz[i] == 'n':
                    prijelazni_znak = '\n'
                elif izraz[i] == '_':
                    prijelazni_znak = ' '
                else:
                    prijelazni_znak = izraz[i]
            a = automat.novo_stanje()
            b = automat.novo_stanje()
            automat.dodaj_prijelaz(a,b,prijelazni_znak)
            
            if prefiksirano == 0:
                if izraz[i] == '\':
                    prefiksirano = 1
                    continue
                if izraz[i] != '(':
                    a = automat.novo_stanje()
                    b = automat.novo_stanje()
                    if izraz[i] == '$':  #'$ označava prazan niz
                        automat.dodaj_eps(a,b)
                    else:
                        dodaj_prijelaz(a,b,izraz[i])
                else:
                    pass
           
                
            
            if i+1 < len(izraz) and izraz[i+1] == '*':
                x = a
                y = b
                a = automat.novostanje()
                b = automat.novostanje()
                automat.dodaj_eps(a,x)
                automat.dodaj_eps(y,b)
                automat.dodaj_eps(a,b)
                automat.dodaj_eps(y,x)
                i += i
        
            automat.dodaj_eps(zadnje_stanje,a)
            zadnje_stanje = b
        automat.dodaj_eps(zadnje_stanje,desno_stanje)
    return lijevo_stanje+desno_stanje

def main():
    ulaz = open ('ulazna.txt','r')

    izraz = []
    lista1 = []
    
    #pretvori u obične regularne izraze bez referenci
    #pohrani u liste, dictionary
    #šalji izraz, automat i mjesto gdje će se spremati (S_pocetno u 
    #tablica_s_pocetno.txt npr)
    
    automat1 = Automat()
    pretvori (lista1,automat1,"S_pocetno")






if __name__ == '__main__':
  main()