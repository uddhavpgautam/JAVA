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
    
def eNKA(prijelazi,poc_prih,lsUlaznihZnakova):
    ret = 0
    #ret = 0,1 ili 2 - N,P,M    
    
    return ret  
    
#ova funkcija ucitava redak po redak iz ulazne datoteke(koju je stvorio GLA)
#i stvara Glavnu listu koju vraca, a članovi te liste su redovi
#npr. glavnaLsAutomata = [1.red,2.red,3.red...] i tu listu vraca 
#obavezno treba skinuti znak za novi red koji je na kraju!!!
def ucitajAutomate():
    datoteka = open('datoteka.txt','r')
    

    
def main():
    #datoteka = open('datoteka.txt','r')
    
    global brojac_redova = 0
    global stanjeAnaliz = 'S_pocetno'
    
    
    ul_ls = ucitajListu()
    print ul_ls    
    
    i = 0
    p = 0
    kraj = len(ul_ls)
    
    
    lsAutomata = ucitajAutomate()

    #čitanje ualznog programa sa postupkom oporavka od greske i kraj citanja kad se obradi cijeli ulazni niz
    #(program u c-u)
    while i < kraj:
        ex = 0 #pocento stanje svih automata je neprihvatljivo        
        #inicijaliziraj buffer
        buff =[]
        p = i #p je "pokazivac" na pocetak buffera, odnosno na dio niza koji jos nije obraden
        #i je "pokazivac" na dio niza gdje smo trenutno
        
        buff.append(ul_ls[i])
        i += 1
        #dodaj jedan znak u buffer i pomakni trenutni pokazivac
        #probaj prvi znak po automatima
        for j in range(len(lsAutomata)):
            automat = lsAutomata[j]
                #automat je sada string(odnosno 1 red)
#                split automat1 u 3 liste: listu prijelaza, listu stanja i 3. listu akcija
#                pretvori listu prijelaza u string i posalji u f-ju
#                iz 2. liste izvuci 1. clan i dodaj ga u globalnu varijablu stanjeAnalizAutomata
#                ostala 2 clana 2. liste spremi u string poc_prih
#                
            while (1):
                #ako je stanjeAnaliz == stanjeAnalizAutomata zovi f-ju inace probaj drugi automat(break)
                povr = simumuliraj trenutni automat eNKA(prijelazi,poc_prih,buff)
                if povr == M: #ako je umro
                    if ex == 0: #u neprihvatljivom je, probaj drugi
                        break
                    elif ex == 1: #u prihvatljivom je zavrsio
                        ret = -2
                        indeks = prihvatljivo(indeks automata - odnosno retka u kojem se nalazi)   
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
                #ako nije umro, u ex stavi u kojem je sada, 
                #povecaj buffer za jos jedan znak pomakni trenutni pokazivac i
                else:
                    ex = povr
                    buff.append(ul_ls[i])
                    i += 1
                    continue
                

            #inače učitaj još jedan znak, funkcija provjeri je zatražila još
            #jedan znak
            
        
        
        
if __name__ == '__main__':
  main()
