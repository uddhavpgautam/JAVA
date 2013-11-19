

def main():

    redak=0
    
    ulaz=open('ulaz2.txt','r')
    ulaz1=ulaz.readlines();
    
    TablicaAkcija=open('TablicaAkcija.txt','r')
    TA=TablicaAkcija.readlines();
    
    TablicaNovoStanje=open('TablicaNovoStanje.txt','r')
    TNS=TablicaNovoStanje.readlines();
    
    Sinkronizacijski=open('Sinkronizacijski.txt','r')

    razina='1'
    lista_razina=[]
    STOG=[]
    STOG2=[]
    trenutno_stanje='0'
    STOG.append(trenutno_stanje)
    STOG2.append(trenutno_stanje)
    novostanje={}
    akcije={}
    unif=[]
    stanja=[]
    n=len(ulaz1)
    
    i=0
    #ucitavanje uniformnih znak po znak
    while i<n:
        ulaz2=ulaz1[i].split(' ')
        ulaz2[0]=ulaz2[0]+' '+str(i)
        ulaz2[-1]=ulaz2[-1].rstrip()
        unif.append(ulaz2)
        i=i+1
    print unif

        
    #ucitavanje svih stanja    
    i=0
    n=len(TA)
    
    while i<n:
        TA2=TA[i].split(' ')
        stanja.append(TA2[0].rstrip())
        i=i+1


    #ucitavanje tablice NovoStanje  
    i=0
    n=len(TNS)
    while i<n:
        TNS2=TNS[i].split(' ')
         
        novostanje[TNS2[0].rstrip(),TNS2[1].rstrip()]=TNS2[2].rstrip(),TNS2[3].rstrip()
          
        i=i+1
    

    
    
    #ucitavanje tablice Akcija
    i=0
    n=len(TA)
    while i<n:
        TA2=TA[i].split(' ')
        
            
        akcije[TA2[0].rstrip(),TA2[1].rstrip()]=TA2[2].rstrip(),TA2[3].rstrip()
          
        i=i+1
    
    #citanje uniformnih iz liste
   
    i=0;
    n=len(unif)
    
    while i<3:
        brN=0
        i2=0
        br_nez=0
        el_razine=[]
        razliciti=0
       
        #odvoji broj od znaka
        odvoji=unif[i][0].split(' ')
        
        akcija=akcije[trenutno_stanje,odvoji[0]][0]
        print 'unif je'
        print i
        
        objekt=akcije[trenutno_stanje,odvoji[0]][1]
        tmp1=list(objekt)
        for znak69 in objekt:
            if znak69=='<':
                brN=brN+1;
        print brN
        
        print 'OBJEKT'
        print objekt
        
        print unif
        
        print 'ovo je akcija'
        print akcija
        if akcija=='Pomakni':
            STOG.append(odvoji[0])
            STOG2.append(unif[i][0])
            trenutno_stanje=str(objekt)
            STOG.append(trenutno_stanje)
            STOG2.append(trenutno_stanje)
            print 'ovo zapisuje'
            print unif[i][0]
            
            lista_razina.append(unif[i][0]+' '+razina)          
            
            
           
        print STOG
        print STOG2
        print lista_razina
        print trenutno_stanje
        
        if akcija=='Reduciraj':
            objekt2=objekt.split('->')
            print brN
            n1=len(objekt2[1])-(2*brN)
            print 'OVAJ BROJ TREBA BIT 2'
            print n1
            
            if objekt2[1]=='$':
                STOG.append(objekt2[0])
                STOG2.append(objekt2[0])
                i=i-1;
            #ako akcija ima neke znakova tj nije epsilon npr B->b
            else:
                j=0
                #provjerava svaki drugi element stoga jer su na stogu stanje i znak
                n2=-2*n1
                
                while j<n1:
                    el_razine.append(STOG2[n2])
                    print 'objekt je'
                    print objekt2[1][j]
                    print 'stog je'
                    print STOG2[n2]
                    if objekt2[1][j]!=STOG[n2]:
                        
                        print 'ovo su elementi'
                        print el_razine
                        razliciti=1
                        print 'razliciti su'
                        print objekt2[1][j]
                        print STOG[n2]
                    n2=n2+2
                    
                    
                    j=j+1
                n2=-2*n1
                print 'elementi'
                print el_razine
                if razliciti==0:     
                    
                    #ako su jednaki lijeva stana produkcije i elementi na stogu
                    #obrisi sa stoga elemente
                    del STOG[n2:]
                    del STOG2[n2:]
                    j2=0
                    while j2<n1:
                        tmp_lista=[]
                        tmp_el=lista_razina.pop()
                        print 'temp je'
                        print tmp_el[0]
                        tmp_el=list(tmp_el)
                        if tmp_el[0]=='<':
                            tmp_raz=int(tmp_el[6])
                            tmp_raz=tmp_raz+1
                            tmp_el[6]=str(tmp_raz)
                        else:
                            tmp_raz=int(tmp_el[4])
                            tmp_raz=tmp_raz+1
                            tmp_el[4]=str(tmp_raz)
                        tmp_el=''.join(tmp_el)
                        tmp_lista.append(tmp_el)
                        j2=j2+1
                    
                    #trenutno stanje je zadnje stanje na stogu
                    trenutno_stanje=STOG[-1]
            
                    #dodaj na stog novi nezavrsni znak
                    STOG.append(objekt2[0])
                    STOG2.append(objekt2[0]+' '+str(br_nez))
                    tmp_lista.append(objekt2[0]+' '+str(br_nez)+' '+razina)
                    lista_razina.append(tmp_lista)

                    
                    #idi u tablicu novostanje i nadjii novo trenutno_stanje
                    trenutno_stanje=novostanje[trenutno_stanje,objekt2[0]][1]
                    STOG.append(trenutno_stanje)
                    STOG2.append(trenutno_stanje)




                    

                    i=i-1;                  
                if razliciti==1:
                    u=0
                    #treba napravit funkciju odbaci()
                
        i=i+1                    
    
                








    


if __name__ == '__main__':
  main()
    


