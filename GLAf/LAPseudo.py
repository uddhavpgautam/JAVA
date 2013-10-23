# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 12:36:58 2013

@author: Matko
"""
import sys


    
def ucitajListu():
    txt=open('ulazProg.txt','r')  #ucitava datoteku(ovdje treba ici stdin umjesto txt jel)
    sve=txt.readlines()      #ucitavam retke
    n=len(sve)
    sve1=[]
    konacna=[]

    i=0  
    while i<n:
        sve[i]=sve[i].split(" ")         #razdvajam rijeci po retcima
        i=i+1

    i=0
    while i<n:
        j=0
        m=len(sve[i])
        while j<m:
            if j>0:
                sve[i][j]=list(sve[i][j])  
                sve[i][j].insert(0," ")           #umetanje praznina
            j=j+1
        i=i+1

    i=0
    n=len(sve)
    while i<n:
        j=0
        m=len(sve[i])
        while j<m:
            sve1.append(list(sve[i][j]))    #nova lista, razdvajanje slova u rijecima
            j=j+1
        i=i+1

    n=len(sve1)
    i=0
    while i<n:
        konacna=konacna+sve1[i]            #konacna lista,svako slovo je poseban element
        i=i+1
    return konacna
    
    
def prihvatljivo(indeks):
    ILI ČAK OVA NE MORA NIŠTA VRAĆAT SAMO MJENJAT NEKE STVARI ODNOSNO ISPISTIVAT!!!
    procitaj 3. listu tog retka (listu akcija)
    ako treba ispisi sto treba i vrati -2 (-2 ok, -1 greska)
    ako je vrati se vrati indeks na koji se treba vratiti
    ako novi red digni global brojac_novog_reda za 1 i vrati -2
    ako udji u stanje promijeni global STANJE u ono koje treba i vrati -2
    ILI ČAK OVA NE MORA NIŠTA VRAĆAT SAMO MJENJAT NEKE STVARI ODNOSNO ISPISTIVAT!!!
    
def eNKA(prijelazi,stanja,lsUlaznihZnakova):
    ret = 0
    #ret = 0,1 ili 2 - N,P,M    
    
    return ret  

def provjeri(lista): 
    ret = -3#po defaultu ova funkcija trazi jos jedan znak
    lsAutoamta = [1.redak,2.redak,3.redak...]
    
    for i in range(lelen(lsAutomata)):
        lsAutomat1 = lsAutomata[i]
        split lsAutomat1 u 3 liste, listu prijelaza, listu stanja i 3. listu akcija
        povr = simumuliraj trenutni automat eNKA(prijelai,stanja,lista)
        if povr == M:
            if ex == 0: #u neprihvatljivom je, probaj drugi
                continue
            elif ex == 1: #u prihvatljivom je zavrsio
                ret = -2
                prihvatljivo(indeks automata - odnosno retka u kojem se nalazi)                    
                break
        ex = povr
    

    #ako niti ejdan autoamt ne nade rjesenje za znakove vrati da je greska i ocekuj
    #novi buffer    
    return ret
    

    
def main():
    datoteka = open('datoteka.txt','r')
    
    ul_ls = ucitajListu()
    print ul_ls    
    i = 0
    p = 0
    kraj = len(ul_ls)

    #čitanje ualznog programa sa postupkom oporava od pogreške  
    while i < kraj:
        buff =[]
        p = i
        while(1):
            if i >= kraj:
                break
            buff.append(ul_ls[i])
            i += 1
            indeks = provjeri(buff)
            if indeks >= 0: #ako je VRATI_SE
                i=p+indeks
                break
            elif indeks == -1: #ako je greška
                print buff[0]
                p += 1
                i = p
                break
            elif indeks == -2: #ako je ok i pročitano
                p = i
                break
            #inače učitaj još jedan znak, funkcija provjeri je zatražila još
            #jedan znak
            
        
        
        
if __name__ == '__main__':
  main()
