# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 12:36:58 2013

@author: Matko
"""
import sys

brRedaka = 1
stanjeAnaliz = 'S_pocetno'  


    
def ucitajListu(): 
    txt=open('UlazuLA4.txt','r')  #ucitava datoteku(ovdje treba ici stdin umjesto txt jel)
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
    txt.close()
    return konacna 
    
    
def prihvatljivo(buff,akcije):
    global brRedaka
    global stanjeAnaliz      
    if akcije[0] == '-':
        pass
    else:
        ispis = ''.join(buff)
        print str(akcije[0])+' '+str(brRedaka)+' '+ispis
        
    if 'NOVI_REDAK' in akcije:
        brRedaka +=1
    if 'UDJI_U_STANJE' in akcije:
        indOdUDJI = akcije.index('UDJI_U_STANJE')
        stanjeAnaliz = str(akcije[indOdUDJI+1])
    if 'VRATI_SE' in akcije:
        indOdVRATI = akcije.index('VRATI_SE')
        indeks = akcije[indOdVRATI+1]
        return indeks
    return -1
               
   
def cash_prijelazb(stanja,mapa):
    ls1 = []
    ls2 = []    
        
    added = 0
    
    for tmp in stanja:
        key = str(tmp)+','+'$'
        if key in mapa:
            ls1.extend(mapa[key])
            added = 1
    
    if added:
        ls2 = cash_prijelaz(ls1,mapa) 
    ls1 = ls1+ls2
    return ls1
    
def cash_prijelaz(stanja,mapa):
    novaS = stanja
    novaS3 = []
    zarez = ','
    cash = 'BEL'  
    added = 0    
    
    for tempS in stanja:
        kljuc = tempS+zarez+cash
        if kljuc in mapa:
            novaS3.extend(mapa[kljuc])
        del kljuc 
    for tempS1 in novaS3:
        if tempS1 not in novaS:
            novaS.append(tempS1)
            added = 1
    if added == 1:
        novaS = cash_prijelaz(novaS,mapa)
    return novaS
    
def eNKA(prijelazi,poc_prih,buff):
    mapa = {}
    for line in prijelazi:
        #razdijeli key od value
        strCmp = line.split("->")
        key  = strCmp [0]
        value = strCmp[1:]
        tmp = ''.join(value)
        if key in mapa:
            mapa[key].append(tmp)
        else:
            mapa[key] = value

    trenS = []    
    iducaS = [] 
    ret = []
    poc = poc_prih[0] 
    poc = str(poc)
    trenS.append(poc) 
    prihS = poc_prih[1]
    prihS = str(prihS)
    

    
    trenS = cash_prijelaz(trenS,mapa)

    for i in buff:
        iducaS = []
        ret = []
        #print trenS
        for tempS in trenS:
            kljuc = str(tempS)+','+i
            if kljuc in mapa:
                tmp = mapa[kljuc]
                iducaS.extend(tmp)
        trenS = iducaS

        trenS = cash_prijelaz(trenS,mapa)

    #ret = 0,1 ili 2 - N,P,M
    if not trenS:
        return 2
    elif prihS in trenS:
        return 1
    else:
        return 0

    
def makniLF(ulazna_lista):
    lista = []
    for red in ulazna_lista:
        tmp = list(red)
        del tmp[-1]
        tmp = ("").join(tmp)
        lista.append(tmp)
    return lista
    

def ucitajAutomate():
    datoteka = open('datoteka.txt','r')
    
    lsRedova = []
    lsRedova = datoteka.readlines()
    lsRedova = makniLF(lsRedova)
    return lsRedova

    
def main():
    
    global brRedaka
    global stanjeAnaliz 

    ul_ls = ucitajListu()  
    
    for i in range(len(ul_ls)):
        if '\n' == ul_ls[i]:
           ul_ls[i] = '\\n'
        if '\t' == ul_ls[i]:
            ul_ls[i] = '\\t'
    
    greska = 1
    
    i = 0
    p = 0
    kraj = len(ul_ls)
    #print ul_ls
    lsAutomata = ucitajAutomate()
    while i < kraj-2: 
        ex = 0 
        buff =[] 
        buff.append(ul_ls[i])
        j = 0
        for j in range(len(lsAutomata)):
            greska = 1 
            automat = str(lsAutomata[j])
            lista = automat.split('__') 
   
            strprijelazi = lista[0]
            prijelazi = strprijelazi.split('##') 
            del prijelazi[-1]

            strstanja = lista[1]
            stanja = strstanja.split('|')
            
            stanjeAnalizTrenAutomata = stanja[0]  
            del stanja[0]
            poc_prih = stanja 
 
            strakcije = lista[2]
            akcije = strakcije.split('|') 
            print buff
            print akcije
            while (1):     
                if stanjeAnaliz != stanjeAnalizTrenAutomata:
                    break 
                povr = eNKA(prijelazi,poc_prih,buff)

                if povr == 2:
                    if ex == 0: 
                        del buff [1:] 
                        i = p
                        break
                    elif ex == 1: 
                        greska = 0
                        del buff[-1]
                        print 'prihvacen'
                        indeks = prihvatljivo(buff,akcije)
#                        print indeks
                        indeks = int(indeks)
                        if indeks >= 0:
#                            print 'vracam se'
#                            print stanjeAnaliz
                            i=p+indeks
                            break
                        elif indeks  < 0:
                            p = i
                            break
                else:
                    ex = povr
                    i += 1
                    if i < kraj:
                        buff.append(ul_ls[i])
                    
            if greska == 0:
                break
            
        if greska == 1:
            i += 1
            p += 1
            

        
        
        
if __name__ == '__main__':
  main()
