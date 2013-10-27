# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 12:36:58 2013

@author: Matko
"""

import sys


    
def ucitajListu(): 
    #txt=open('UlazuLA4.txt','r')  #ucitava datoteku(ovdje treba ici stdin umjesto txt jel)
    txt = sys.stdin
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
    
    
#prijelazi dolaze kao lista
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
    
    brRedaka = 1
     

    ul_ls = ucitajListu()  
    
    for i in range(len(ul_ls)):
        if '\n' == ul_ls[i]:
           ul_ls[i] = '\\n'
        if '\t' == ul_ls[i]:
            ul_ls[i] = '\\t'
    

    #print ul_ls
    lsAutomata = ucitajAutomate() 
    
    lsPrijelaza = []
    lsStanja = []
    lsAkcija = [] 
    
    for j in range(len(lsAutomata)):
        
        automat = str(lsAutomata[j])
        lista = automat.split('__') 
   
        strprijelazi = lista[0]
        prijelazi = strprijelazi.split('##') 
        del prijelazi[-1]
        lsPrijelaza.append(prijelazi)

        strstanja = lista[1]
        stanja = strstanja.split('|')
        lsStanja.append(stanja)
            
#        stanjeAnalizTrenAutomata = stanja[0]  
#        del stanja[0]
#        poc_prih = stanja 
 
        strakcije = lista[2]
        akcije = strakcije.split('|') 
        lsAkcija.append(akcije)
    
    #print lsStanja[0]
    stanjeAnaliz = lsStanja[0][0]
    #print stanjeAnaliz
    
    buff = []
    lsEx = []
    lsTren = []
    lsBuffera = []
    lsDodan = []
    
    #postavi ih sve na 0
    for j in range(len(lsAutomata)):
        lsTren.append(0)
        lsEx.append(0) 
        lsDodan.append(0)
        lsBuffera.append('SOH')
        
    added = 0
    povr = -1
    prihvatljivo = -69
    p = 0 #pocetak buffera
    i = 0 #pointer na trenutni dio u nizu
    z = 0
    
    kraj = len(ul_ls)
    #print ul_ls
    
    while i < kraj:
        #print i
        buff.append(ul_ls[i])
        #print buff
        #print buff
        j = 0
        
        while j < len(lsAutomata):
            stanjeAnalizTrenAutomata = lsStanja[j][0]
            if stanjeAnaliz != stanjeAnalizTrenAutomata:
                lsTren[j] = 2 
                j += 1
                continue
            
            poc_prih = lsStanja[j][1:]
            lsTren[j] = eNKA(lsPrijelaza[j],poc_prih,buff)            
            
            j +=1
        #print lsTren
        
                
        for k in range(len(lsTren)):
#            print lsTren[k]
            if lsTren[k] == 1:
                prihvatljivo = k
                break
#        print 'prihvatljivo'
#        print prihvatljivo
        
        if 0 not in lsTren and 1 not in lsTren:
#            print buff
#            print 'svi su mrtvi'
            if prihvatljivo == -69:
                #print 'greska'
                p = p + 1
                i = p
            else:
#                print buff
#                print prihvatljivo
                del buff [-1]
#                print buff
#                print 'brisem buff'
                if 'VRATI_SE' in lsAkcija[prihvatljivo]:
                    indOdVRATI = lsAkcija[prihvatljivo].index('VRATI_SE')
                    povr = lsAkcija[prihvatljivo][indOdVRATI+1]
#                print lsAkcija[prihvatljivo]
                povr = int(povr)
                if povr < 0:
                    p = i
                    if lsAkcija[prihvatljivo][0] != '-':
                        ispis = ''.join(buff)
                        ispis = ispis.rstrip()
                        ispis = ispis.rstrip('\n')
                        ispis = ispis.rstrip('\t')
                        print str(lsAkcija[prihvatljivo][0])+' '+str(brRedaka)+' '+ispis
                else:
                    p = p + povr
                    i = p
                    del buff[povr:]
                    if lsAkcija[prihvatljivo][0] != '-':
                        ispis = ''.join(buff)
                        ispis = ispis.rstrip()
                        ispis = ispis.rstrip('\n')
                        ispis = ispis.rstrip('\t')
                        print str(lsAkcija[prihvatljivo][0])+' '+str(brRedaka)+' '+ispis
                if 'NOVI_REDAK' in lsAkcija[prihvatljivo]:
                    brRedaka +=1
                if 'UDJI_U_STANJE' in lsAkcija[prihvatljivo]:
                    indOdUDJI = lsAkcija[prihvatljivo].index('UDJI_U_STANJE')
                    stanjeAnaliz = str(lsAkcija[prihvatljivo][indOdUDJI+1])
#                print stanjeAnaliz
                povr = -1
                prihvatljivo = -69
            buff = []
        else:
             i += 1
                
        
        
        
if __name__ == '__main__':
  main()
