# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 23:36:19 2013

@author: Matko
"""

import os
import sys


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
        prijelaz = str(c)+','+'$'+'->'+str(d)+'##'
        datoteka.write(prijelaz) 
    def dodaj_prijelaz(self,c,d,zn):
        prijelaz = ""
        prijelaz = str(c)+','+str(zn)+'->'+str(d)+'##'
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
    k = 0
    for i in range(len(izraz)):
        if izraz[i] == '(' and je_operator (izraz,i):
            br_zagrada = br_zagrada + 1
        elif izraz[i] == ')' and je_operator(izraz,i):
            br_zagrada = br_zagrada - 1
        elif br_zagrada == 0 and izraz [i] == '|' and je_operator(izraz,i):
            temp = []
            temp = izraz[k:i]
            izbori.append(temp) 
            k = i+1

    if k != 0:
        izbori.append(izraz[k:])      
    
    lijevo_stanje = automat.novo_stanje()
    desno_stanje = automat.novo_stanje() 
    
    if k != 0:
        
        for item in izbori:
            privremeno = []
            privremeno = pretvori(item,automat)
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
                    prijelazni_znak = '\\t'
                elif izraz[i] == 'n':
                    prijelazni_znak = '\\n'
                elif izraz[i] == '_':
                    prijelazni_znak = ' '
                else:
                    prijelazni_znak = izraz[i]
                a = automat.novo_stanje()
                b = automat.novo_stanje() 
                automat.dodaj_prijelaz(a,b,prijelazni_znak)
            
            elif prefiksirano == 0:
                if izraz[i] == '\\':
                    prefiksirano = 1
                    continue
                if izraz[i] != '(':
                    a = automat.novo_stanje()
                    b = automat.novo_stanje()
                    #ovaj dio kdoa ne razumijem...
                    if izraz[i] == '$':  #'$ označava prazan niz
                        automat.dodaj_eps(a,b)
                    else:
                        automat.dodaj_prijelaz(a,b,izraz[i])
                else: #provjerava ako je izraz[i] == zatvorena_zagrada - (')')
                    #int k = *pronadji odgovarajucu zatvorenu zagradu - FALI!!!
                    #k je indeks odgovarajuće zatvorene zagrade 
                    k = i
                    while k<=i:
                        if izraz[k] == ')' and je_operator(izraz,k):
                            break
                        k += 1
                    privremeno= []
                    #pošalji u pretvori izraz između zagrada
                    temp = []
                    temp = izraz[(i+1):(k)]
                    privremeno = pretvori(temp,automat)
                    a = privremeno[0]
                    b = privremeno[1]
                    i = k
                
            
            if i+1 < len(izraz) and izraz[i+1] == '*':
                x = a
                y = b
                a = automat.novo_stanje()
                b = automat.novo_stanje() 
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

def makniLF(ulazna_lista):
    lista = []
    for red in ulazna_lista:
        tmp = list(red)
        del tmp[-1]
        tmp = ("").join(tmp)
        lista.append(tmp)
    return lista

def izmedjuZagrada(red):
    tmp = red.split(">")[0]
    tmp = list(tmp)
    del tmp[0]
    tmp = ("").join(tmp)
    return tmp

#def ostatakReda(red): 
#    tmp = red.split(">")[1]
#    tmp = list(tmp)
#    return tmp

def ostatakReda(red): 
    tmp = list(red)
    for i in range(len(tmp)):
        if tmp[i] == '>':
            del tmp [:(i+1)]
            break
    return tmp


class Dict(object):
    
    def __init__(self, ulazna_lista):
        self.ulazna_lista = ulazna_lista
        self.last_row = 0

    def napraviDict(self):
        dict1 = {}
        for redak in self.ulazna_lista:
            self.last_row += 1
            if list(redak)[0] == "%":
                break
            odvoji = redak.split(" ")
            lista = odvoji[1].split("|")
            pomlist = []
            tmp = []
            for clan in lista:
                if clan in dict1:
                    pomlist.append("(")
                    for item in dict1[clan]:
                        if (item != "|"): pomlist.append(item)
                    pomlist.append(")")
                else:
                    pomlist.append(clan)
            for i in range(0, len(pomlist)):
                tmp.append(pomlist[i])
                if (pomlist[i] == "(" or i == len(pomlist) - 1 or pomlist[i+1] == ")"): continue
                tmp.append("|")
            dict1[odvoji[0]] = tmp
        return dict1

    def nadjiRed(self):
        row = 0
        for red in self.ulazna_lista:
            tmp = list(red)
            prvi_znak = tmp[0]
            tmp = ("").join(tmp)
            if prvi_znak == "<": return row
            row += 1
        return -1

def zamjenaOstatkaReda(lista, dictionary):
    
    string = ("").join(lista)
    for substring in dictionary.keys():  
        if substring in string:
            tempS = ''.join(dictionary[substring])
            string = string.replace(substring,tempS)
            
    lista = list(string)         
    return lista

def izmjeniRedak(redak):
    for i in range(0, len(redak)):
        redak[i] = str(redak[i])
        redak[i] = redak[i] + "|"
    return redak 
 

def main():
    global datoteka
    #ulaz = sys.stdin
    ulaz = open ('ulazna.txt','r')
    #datoteka = open('datoteka.txt','w')
    datoteka = open(os.path.join('analizator','datoteka.txt' ), "w")
    dictionary1 = Dict(makniLF(ulaz.readlines())) 
    dict2 = dictionary1.napraviDict()
    pozicija = dictionary1.nadjiRed() 
    dictionary1.last_row = pozicija

    while(dictionary1.last_row < len(dictionary1.ulazna_lista)):
        
        listica = []
        prvi_znak = list(dictionary1.ulazna_lista[dictionary1.last_row])[0]
        stanje = izmedjuZagrada(dictionary1.ulazna_lista[dictionary1.last_row])
        ostatak_reda = ostatakReda(dictionary1.ulazna_lista[dictionary1.last_row])
        
        automat1 = Automat()
        
        ostatak_reda = zamjenaOstatkaReda(ostatak_reda, dict2) 
        ret = pretvori(ostatak_reda, automat1)
        
        stanje ='__'+stanje + '|'
        datoteka.write(stanje)
        poc = str(ret[0])
        prih = str(ret[1])
        poc = poc+'|'
        prih = prih+'__'
        
        datoteka.write(poc)
        datoteka.write(prih)
        
        dictionary1.last_row += 2
        prvi_znak = list(dictionary1.ulazna_lista[dictionary1.last_row])[0]
        
        while (prvi_znak != '}'):
            for item in dictionary1.ulazna_lista[dictionary1.last_row].split(" "):
                listica.append(item)
                listica.append('|')
            redak = dictionary1.ulazna_lista[dictionary1.last_row].split(" ")
            redak = izmjeniRedak(redak)
            #zapisi sve clanove u datoteku
            dictionary1.last_row += 1
            prvi_znak = list(dictionary1.ulazna_lista[dictionary1.last_row])[0]
            
        dictionary1.last_row += 1
        if listica[-1] == '|':
            del listica[-1]
        unf = ''.join(listica)
        datoteka.write(unf)
        datoteka.write('\n')  
    ulaz.close()
    datoteka.close()

if __name__ == '__main__':
  main()
