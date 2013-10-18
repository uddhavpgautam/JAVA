# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 13:58:00 2013

@author: Matko
"""

class Simululator(object):
    """ja simuliram po automatima"""
    
    def __init__(self):
        pass
    
    def simuliraj(self,znak,automat):
        pass
        
        



class Checker(object):
    
    """ja provjeravam detalje"""
    
    def __init__(self):
        pass

    def noviRedak (self,stanje,znak,automati):#dobije sve automate
        ret = 0
        return ret #vraća 1 ako je pročitan znak za novi redak
    
    def mjenjajStanje(self,stanje,znak):
        ret = 0
        #dio koda
        return ret #ako treba promijeniti vraća novo stanje
        
    def vratiSe(self,stanje,znak):
        ret = 0
        #dio koda
        return ret #vraća indeks znaka u bufferu na koji se treba vratiti , odnosno
                    #govori glavnom programu koji dio niza da odbaci
    def odrediUnfZnak(self, stanje, znak):
        #
        pass        
        
        
        
def eNKA (znak,poc,prih,prijelazi):
    pass
    #vraća 1 ako je ušao u prihvatljivo, 2 ako je u neprihvatljivom, a 0 ako
    #nema prijelaza(mrtav je)
    
def main():
    #otvori sve i zovi Checker malo po malo
    #te na kraju koda (petlje) ispisi što ti ej simulator rekao
    #(samo neke stvari, ne sve)

    #važno je uvidjeti kako će se checker pozivati dosta puta, i to sa različitim zadatcima
    #tek nakon što je ciklus checkera zavšio main može na izlaz nešto ispisati
    #kraj ciklusa označava povratna vrijednost za unfZnak

    #stvorim buffer u koji se stavljaju znakovi sve dok funkcija unfZnak ne dobije
    # povratnu vrijednost dokle god je povratna vrijednost 0 funkcija se poziva
    #a buffer se puni

if __name__ == '__main__':
  main()
