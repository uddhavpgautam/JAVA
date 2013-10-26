# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 15:57:29 2013

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
        prijelaz = str(c)+','+'BEL'+'->'+str(d)+'##'
        datoteka.write(prijelaz) 
    def dodaj_prijelaz(self,c,d,zn):
        prijelaz = ""
        prijelaz = str(c)+','+str(zn)+'->'+str(d)+'##'
        datoteka.write(prijelaz)
    
    
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
        i = 0
        while i < len(izraz):
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
                    i += 1
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
                    j = i
                    br_zagrada1 = 0
                    while (1):
                        if izraz[j] == '(' and je_operator (izraz,j):
                            br_zagrada1 = br_zagrada1 + 1
                        elif izraz[j] == ')' and je_operator(izraz,j):
                            br_zagrada1 = br_zagrada1 - 1
                            if br_zagrada1 == 0:
                                break
                        j += 1
                    privremeno= []
                    #pošalji u pretvori izraz između zagrada
                    temp = []
                    temp = izraz[(i+1):(j)]
                    privremeno = pretvori(temp,automat)
                    a = privremeno[0]
                    b = privremeno[1]
                    i = j

                
            
            if i+1 < len(izraz) and izraz[i+1] == '*':
                x = a
                y = b
                a = automat.novo_stanje()
                b = automat.novo_stanje() 
                automat.dodaj_eps(a,x)
                automat.dodaj_eps(y,b)
                automat.dodaj_eps(a,b)
                automat.dodaj_eps(y,x)
                i += 1
        
            automat.dodaj_eps(zadnje_stanje,a)
            zadnje_stanje = b
            i += 1
        automat.dodaj_eps(zadnje_stanje,desno_stanje)
        
    retList = []
    retList.extend([lijevo_stanje,desno_stanje])
    return retList
    
def zamjenaOstatkaReda(lista, dictionary):
    
    string = ("").join(lista)
    for substring in dictionary.keys():  
        if substring in string:
            tempS = ''.join(dictionary[substring])
            string = string.replace(substring,tempS)
            
    lista = list(string)         
    return lista
    
def izmedjuZagrada(red):
    tmp = red.split(">")[0]
    tmp = list(tmp)
    del tmp[0]
    tmp = ("").join(tmp)
    return tmp
    
def ostatakReda(red): 
    tmp = list(red)
    for i in range(len(tmp)):
        if tmp[i] == '>':
            del tmp [:(i+1)]
            break
    return tmp
    
def makniLfIzReda(red):
    tmp = []
    tmp = list(red)
    del tmp [-1]
    tmp = ''.join(tmp)
    return tmp
    

def main():
    global datoteka
    ulaz = open ('ulazna4.txt','r')
    datoteka = open(os.path.join('analizator','datoteka.txt' ), "w")
    
    keys = []    
    
    mapa = {}
    #ucitavaj redove i stvori dict
    while (1):
        red = ulaz.readline().split(' ')
        
        #prvi provjeri je li valja reg def
        poc = red [0]
        poc = list(poc)
        if poc[0] == '%':
            break
        
        #makni znak za novi red s kraja
        red [-1] = red[-1].strip()
        
        desnaStrana = red[1]
        
        #ako u desnoj strani ima string koji je u mapi zamjeni ga sa vrijednoscu iz mape     
        for i in range(len(keys)):
            tmpstr = str(keys[i])
            desnaStrana = desnaStrana.replace(tmpstr,mapa[tmpstr])
        
        #dodaj zagrade
        desnaStrana = '('+desnaStrana+')'
        mapa[red[0]] = desnaStrana
        keys.append(red[0])    
    
    for key in mapa:
        mapa[key] = list(mapa[key])
    
    #ovo sluzi samo da preskocim ejdan red i dodem do PRAVILA
    red = ulaz.readline().split(' ')
        
    for red in ulaz:
        red = makniLfIzReda(red)
        listica = [] 
        poc = red [0]
        poc = list(poc)
        
        if poc[0] == '<':  
            automat1 = Automat()
            stanje = izmedjuZagrada(red)
            ostatak_reda = ostatakReda(red)
            ostatak_reda = zamjenaOstatkaReda(ostatak_reda, mapa)
            ret = pretvori(ostatak_reda, automat1)
            stanje ='__'+stanje + '|'
            datoteka.write(stanje)
            poc = str(ret[0])
            prih = str(ret[1])
            poc = poc+'|'
            prih = prih+'__'
            datoteka.write(poc)
            datoteka.write(prih)
        elif poc[0] == '{':
            for red in ulaz:
                poc = red [0]
                poc = list(poc)
                red = makniLfIzReda(red)
                if poc[0] == '}':
                    break
                
                tmp = red.split(' ')
                for item in tmp:
                    listica.append(item)
                    listica.append('|')
            del listica[-1]
            unf = ''.join(listica)
            datoteka.write(unf)
            datoteka.write('\n')
            
    ulaz.close()
    datoteka.close()


if __name__ == '__main__':
  main()