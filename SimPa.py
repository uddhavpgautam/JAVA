# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 21:13:48 2013

@author: Matko
"""
import sys

def izvuciStanje (vrijed):
    temp = ''.join(vrijed)
    ret = temp.split(',')
    return ret[0]   

#f-ja za manipulaciju stogom, dodaje ostavlja ili mice znakove sa stoga
def stogF(vrijed,stog):   
    temp1 = ''.join(vrijed)
    temp2 = temp1.split(',')
    stogValue = temp2[1]
    #stogValue je sada ili 2 znaka ili jedan znak ili $
    #ako su 2 znaka, na stog dodam lijevi
    if len(stogValue) > 1: 
        del stog[-1]
        for i in reversed(stogValue):
            stog.append(i)
    #ako je jedan znak stog ostavljam kakav je
    if len(stogValue) == 1 and stogValue != '$':
        del stog [-1]
        stog.append(stogValue) 
    #ako je $, treba skinut znak sa stoga
    if stogValue == '$':
        del stog [-1]
    
def cash_prijelaz(stanje,stog,mapa):
    zarez = ','
    space ='|'
    hash1 = '#'
    cash = '$'
    kljuc = stanje+zarez+cash+zarez+stog[-1]
    if kljuc in mapa:
        stanje = izvuciStanje(mapa[kljuc])
        stogF(mapa[kljuc],stog)
        if len(stog) == 0:
            sys.stdout.write(stanje+hash1+cash+space) 
        else:
            sys.stdout.write(stanje+hash1+stog[-1]+space) 
        return stanje
        
        

def main ():
    ulaz = sys.stdin
    #1. red spremi u listu
    ulazni_nizovi = ulaz.readline().split('|')

    #2. red spremi u listu
    skup_stanja = ulaz.readline().split(',')
    skup_stanja [-1] = skup_stanja[-1].strip()
    
    #3.red spremi u listu
    abeceda = ulaz.readline().split(',')
    
    #4. red spemi u listu
    skup_znakova_stoga = ulaz.readline().split(',')

    #5. red spremi u listu
    skup_prih_stanja = ulaz.readline().split(',')
    skup_prih_stanja [-1] = skup_prih_stanja[-1].strip()

    #6. red spremi u string (1 je pocetno stanje)
    pocetno =  ulaz.readline().split(',')
    pocetno[-1] = pocetno[-1].strip()
    pocetnoS = ''.join(pocetno)
    #7.red
    pocetni = ulaz.readline().split(',')
    pocetni[-1] = pocetni[-1].strip()
    pocetniS = ''.join(pocetni)
    #liste ključeva i vrijednosti
    keys = []
    values = [] 
   
    #stvori dictionary takad da za svaki procitani red od 6. na dalje ono
    #lijevo od znaka "->" bude tuple(stanje,znak), a desno value
    for line in ulaz.readlines():
        #razdijeli key od value
        strCmp = line.split("->")
        key  =strCmp [0]
        value = strCmp[1:] 
        value[-1]=value[-1].strip()
        keys.append(key)
        values.append(value)
    
    #stvori dictionary, mapu      
    mapa = dict(zip(keys,values))
    
    zarez = ','
    space ='|'
    hash1 = '#'
    i = 0
    while i < len(ulazni_nizovi):
        #postoavi trenutno stanje i postavi stog
        trenS = pocetnoS 
        stog = [pocetniS]
        sys.stdout.write (pocetnoS+hash1+pocetniS+space)
        s1 = ulazni_nizovi[i]
        ulazni_znakovi = s1.split(',')
        j = 0
        while j < len(ulazni_znakovi):
            fail = 0
            if (j+1) == len(ulazni_znakovi):
               ulazni_znakovi [-1] = ulazni_znakovi[-1].strip()
              #st je zadnji znak na stogu
            if len(stog) == 0:
                sys.stdout.write('fail')
                sys.stdout.write (space)
                fail = 1
                break
            kljuc = trenS+zarez+ulazni_znakovi[j]+zarez+stog[-1]
            if kljuc not in mapa:
                sys.stdout.write('fail')
                sys.stdout.write (space)
                fail = 1
                break
            else:
                trenS = izvuciStanje(mapa[kljuc])
                stogF(mapa[kljuc],stog)
                stogIsp = []
                stogIsp.extend(stog)
                stogIsp.reverse()
                stogIspS = ''.join(stogIsp)
                sys.stdout.write(trenS+hash1+stogIspS+space) 
                #sada još pogledaj ako postoji prijelaz sa cashom

                temp3 = cash_prijelaz(trenS,stog,mapa)
                if temp3 in skup_stanja:
                    trenS = temp3

            j += 1
        #ispisi prihvatljivost
        if trenS in skup_prih_stanja and fail == 0:
            sys.stdout.write ('1')
        else:
            sys.stdout.write ('0')
        sys.stdout.write("\n")
        i+=1
    
    ulaz.close()

if __name__ == '__main__':
  main()