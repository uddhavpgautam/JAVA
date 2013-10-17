# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 12:35:57 2013

@author: Matko
"""

import sys

class Dict(object):
    
    def __init__(self):
        pass 

    def napraviDict(self, ulazna_lista):
        dict1 = {}
        for redak in ulazna_lista:
            if list(redak)[0] == "%":
                break
            odvoji = redak.split(" ")
            prvi_clan = odvoji[1].split("|")[0]
            if prvi_clan in dict1:
                value = dict1[prvi_clan]
                temp = odvoji[1].split(prvi_clan)
                for slovo in list(temp[1]):
                    value.append(slovo)
            else:
                value = list(odvoji[1])
            del value[-1]
            dict1[odvoji[0]] = value
        return dict1

class Automat(object):
    
    """Nacrt za sve $-NKA automate koji će se ostvarivati."""
    
    def __init__(self):        
        pass
    
    br_stanja = 0
    
    def novo_stanje(self):
        self.br_stanja = self.br_stanja + 1
        return self.br_stanja - 1 
    def dodaj_eps(self,c,d):
        prijelaz = ""
        prijelaz = str(c)+','+'$'+'->'+str(d)+'|'
        datoteka.write(prijelaz) 
    def dodaj_prijelaz(self,c,d,zn):
        prijelaz = ""
        prijelaz = str(c)+','+str(zn)+'->'+str(d)+'|'
        datoteka.write(prijelaz)
    
#ako ima paran broj \ ispred onda je operator
def je_operator(izraz,i):
    br = 0 
    while ( ((i-1) >= 0) and izraz[i-1] == '\\'): 
        br = br+1
        i = i-1
    return br%2 == 0   
    
def pretvori(izraz,automat):
    izbori = []
    br_zagrada = 0
    j = 0
    for i in range(len(izraz)):
        if izraz[i] == '(' and je_operator (izraz,i):
            br_zagrada = br_zagrada + 1
        elif izraz[i] == ')' and je_operator(izraz,i):
            br_zagrada = br_zagrada - 1
        elif br_zagrada == 0 and izraz [i] == '|' and je_operator(izraz,i):
            izbori.append(izraz[i-1])
            j = 1

    if j != 0:
        izbori.append(izraz[-1]) 
    
    lijevo_stanje = automat.novo_stanje()
    desno_stanje = automat.novo_stanje()
    
    if j != 0:
        for i in range(len(izbori)):
            privremeno = []
            privremeno = pretvori(izbori,automat)
            automat.dodaj_eps(lijevo_stanje,privremeno[0]) #privremeno[0] je 
            automat.dodaj_eps(privremeno[1],desno_stanje) #privremeno lijevo stanje
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
                if izraz[i] == '\\':
                    prefiksirano = 1
                    continue
                if izraz[i] != '(':
                    a = automat.novo_stanje()
                    b = automat.novo_stanje()
                    if izraz[i] == '$':  #'$ označava prazan niz
                        automat.dodaj_eps(a,b)
                    else:
                        automat.dodaj_prijelaz(a,b,izraz[i])
                else: #provjerava ako je izraz[i] == zatvorena_zagrada - (')')
                    #int j = *pronadji odgovarajucu zatvorenu zagradu - FALI!!!
                    #j je indeks odgovarajuće zatvorene zagrade
                    #j = i 
                    k = i
                    while 1:
                        if izraz[k] == ')' and je_operator(izraz,k):
                            break
                        k += 1
                    privremeno= []
                    #pošalji u pretvori izraz između zagrada
                    privremeno = pretvori(izraz[(i+1):(k-1)],automat)
                    a = privremeno[0]
                    b = privremeno[1]
                    i = k
                
            
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
        
        retList = []
        retList.extend([lijevo_stanje,desno_stanje])
        return retList
        
        
    
def main():
    ulaz = open ('ulazna.txt','r')
    datoteka = open ('datoteka.txt','w')
    dictionary1 = Dict()
    ulazna_lista = ulaz.readlines()
    dict2 = dictionary1.napraviDict(ulazna_lista)
    for item in dict2:
        print str(item) + " " + str(dict2[item])
    
    stanja1 = []
    ls1 = [0,'|',1,'|',2,'|',3,'|',4,'|',5,'|',6,'|',7,'|',8,'|',9]
    automat1 = Automat()
    stanja1 = pretvori (ls1,automat1)    

if __name__ == '__main__':
  main()
