# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 12:36:58 2013

@author: Matko
"""
import sys

brRedaka = 0
stanjeAnaliz = 'S_pocetno'

def cash_prijelaz(stanja,mapa):
    novaS = stanja
    novaS2 = []
    novaS3 = []
    zarez = ','
    cash = '$'  
    added = 0    
    for tempS in stanja:
        kljuc = str(tempS)+zarez+cash
        if kljuc in mapa:
            novaS1 = mapa[kljuc]
            str7 = ''.join(novaS1)
            novaS2 = str7.split(',')
            novaS2[-1] = novaS2[-1].strip()
            novaS3.extend(novaS2)
        del kljuc 
    for tempS1 in novaS3:
        if tempS1 not in novaS:
            novaS.append(tempS1)
            added = 1
    if added == 1:
        novaS = cash_prijelaz(novaS,mapa)
    return novaS
    
def ucitajListu(): 
    txt=open('ulazuLA.txt','r')  #ucitava datoteku(ovdje treba ici stdin umjesto txt jel)
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
    
    
def prihvatljivo(buff,akcije):
#   akcije dolaze kao lista, a buff kao lista
#    ako treba ispisi sto treba i vrati negativan broj
#    ako je vrati se vrati indeks na koji se treba vratiti
#    ako novi red digni global brojac_novog_reda za 1 i vrati negativan broj
#    ako udji u stanje promijeni global STANJE u ono koje treba i vrati negativan broj
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
               
   
#treba odluciti hoce li argumenti dolaziti kao lista ili kao stringovi

#v1.7 dolaze kao liste
def eNKA(prijelazi,poc_prih,buff):
    #print buff   
    keys = []
    values = []
    for line in prijelazi:
        #razdijeli key od value
        strCmp = line.split("->")
        key  =strCmp [0]
        value = strCmp[1:]      
        keys.append(key)
        values.append(value)
    
    #stvori dictionary, mapu      
    mapa = dict(zip(keys,values))
    #print mapa
    trenS = [] 
        
    poc = poc_prih[0]
    poc = str(poc)
    trenS.append(poc)
    prihS = poc_prih[1]
    prihS = str(prihS)
    
    
    iducaS = []
    
    #saji znak po znak u automat  
    for i in buff:
        #prvo udi u sva stanja u koja mozes epsilon prijalzima
        iducaS = []
        trenS = cash_prijelaz(trenS,mapa)
        for tempS in trenS:
            kljuc = tempS+','+str(i)
            if kljuc in mapa:
                tmp = mapa[kljuc]
                iducaS.extend(tmp)
        trenS = iducaS
        trenS = cash_prijelaz(trenS,mapa)
    #print trenS         
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
    
#ova funkcija ucitava redak po redak iz ulazne datoteke(koju je stvorio GLA)
#i stvara Glavnu listu koju vraca, a članovi te liste su redovi
#npr. glavnaLsAutomata = [1.red,2.red,3.red...] i tu listu vraca 
#obavezno treba skinuti znak za novi red koji je na kraju!!!    
def ucitajAutomate():
    datoteka = open('datoteka.txt','r')
    
    lsRedova = []
    lsRedova = datoteka.readlines()
    lsRedova = makniLF(lsRedova)
    return lsRedova

    
def main():
    #datoteka = open('datoteka.txt','r')
    
    global brRedaka
    global stanjeAnaliz 

    ul_ls = ucitajListu()  
    
    
    #p je "pokazivac" na pocetak buffera, odnosno na dio niza koji jos nije obraden
    #i je "pokazivac" na dio niza gdje smo trenutno
    i = 0
    p = 0
    kraj = len(ul_ls)
    greska = 1
    
    lsAutomata = ucitajAutomate()

    #čitanje ualznog programa sa postupkom oporavka od greske i kraj citanja kad se obradi cijeli ulazni niz
    #(program u c-u)
    while i < kraj:
        ex = 0 #pocento stanje svih automata je neprihvatljivo        
        #inicijaliziraj buffer
        buff =[]
        buff.append(ul_ls[i])
#        print 'buff'
#        print buff
        i += 1
        #dodaj jedan znak u buffer i pomakni trenutni pokazivac
        #probaj prvi znak po automatima
        for j in range(len(lsAutomata)):
            automat = str(lsAutomata[j])
                #automat je sada string(odnosno 1 red)
#                split automat1 u 3 liste: listu prijelaza, listu stanja i 3. listu akcija
#                pretvori listu prijelaza u string i posalji u f-ju
#                iz 2. liste izvuci 1. clan i dodaj ga u globalnu varijablu stanjeAnalizAutomata
#                ostala 2 clana 2. liste spremi u string poc_prih
#               
            lista = automat.split('__')
            
            strprijelazi = lista[0]
            
            #iduci dio koda ovdje ill u f-ji eNKA, u ovom slučaju bez dijela koda 
            #u f-ju se šalju stringovi koji se u f-ji moraju urediti iako bi bilo bolje da se 
            #tu uređuju, brže
            prijelazi = strprijelazi.split('|')
            del prijelazi[-1] #brise suvisni znak '|'
            #vrati prijelaze u string
            #print prijelazi
            #prijelazi = ''.join(prijelazi)
            
            strstanja = lista[1]
            stanja = strstanja.split('|')
            
            stanjeAnalizTrenAutomata = stanja[0]  
            del stanja[0]
            poc_prih = stanja
 
            #stanja.insert(1,'|')
            #poc_prih = ''.join(stanja)
            
            strakcije = lista[2]
            akcije = strakcije.split('|')
            
#            print 'ulazim u while'
            while (1):
#                print automat
#                print 'buff'
#                print buff
                #ako je stanjeAnaliz == stanjeAnalizAutomata zovi f-ju inace probaj drugi automat(break)
                if stanjeAnaliz != stanjeAnalizTrenAutomata:
#                    print 'nisam u istom stanju'
#                    print greska
                    break 
                #povr = simumuliraj trenutni automat eNKA(prijelazi,poc_prih,buff)
#                print 'zoven eNKA'
                povr = eNKA(prijelazi,poc_prih,buff)
#                print povr
#                print ex
                if povr == 2: #ako je umro
                    if ex == 0: #u neprihvatljivom je, probaj drugi
                        #pobrisi buffer, sve osim prvog clana (s njim smo i usli u ispitivanje ovog automata)
                        #vrati trenutni pokazivac na pokazivac p koji je pokazivac na pocetak onoga sto je uslo u buffer
                        del buff [1:] 
                        i = p
                        greska = 1
                        break
                    elif ex == 1: #u prihvatljivom je zavrsio 
                        greska = 0
                        #rijesi se suvisnog znaka
                        del buff[-1]
#                        indeks = prihvatljivo(buff te listuAckija - 3. listu)   
#                        print 'zovem prihvatljivo'
                        indeks = prihvatljivo(buff,akcije)
#                        print indeks
                        if indeks >= 0: #ako je VRATI_SE
                            #moram li ostati u istom automatu??? - valjda ne
                            i=p+indeks
                            break
                        elif indeks < 0: #ako je ok i pročitano
                            p = i
                            break
                        
                #ako nije umro, u ex stavi u kojem je sada, 
                #povecaj buffer za jos jedan znak pomakni trenutni pokazivac i
                else:
                    ex = povr
                    i += 1
                    buff.append(ul_ls[i])
                    
                
            #ako nema greske znaci da smo pronasli prihvatljivi automat i trebamo se pomaknuti u ulasnom nizu
            #prekidamo pretragu po automatima i krecemo dalje
            # i vec sada pokazuje na znak koji jos nije parsiran jer je taj znak uzrokovao smrt automata
            #koji je kasnije se ustvrdilo prihvatio niz zadan bufferom
            if greska == 0:
                break
            
       #ako niti jedan automat nije uspio isimulirati znak znaci da je greska == 1
        #ispisi znak koji je greska i pomakni pointer za iduci znak
        if greska:
            print buff[0]+'greska'
            i += 1
        
        
        
if __name__ == '__main__':
  main()
