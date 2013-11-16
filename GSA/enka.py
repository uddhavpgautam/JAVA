# -*- coding: utf-8 -*-
"""
@author: Matko
"""

from dka import Dka

class Enka(object):


    def __init__(self,mapa,listaPraznih,dictZapocinje,zavrsni,nezavrsni):
        self.mapa = mapa
        self.listaPraznih = listaPraznih
        self.dictZapocinje = dictZapocinje
        self.zavrsni = zavrsni
        self.nezavrsni = nezavrsni

    def stvoriStanje(self,ime,lista):
        stanje = ''
        lista = list(lista)
        stanje += ''.join(ime)
        stanje += '{'
        stanje += ''.join(lista)
        stanje += '}'
        return stanje

    def jeLipotpuna(self,stanje):
        tmp = stanje.split('{')

        ime = tmp[0]

        #prvo vidi di je točka
        ind = ime.find('#')

        #je li na kraju,
        if ind+1 == len(ime):
            return 1
        else:
            return 0

    def nadiEpsPoc(self,stanje,prijelazi):
        #dobiva jedno stanje
        #nalazi sva stanja u koje se prelazi eps prijalzima iz tog stanja (samo prvu razinu)
        tmp = stanje.split('{')
        listaStara = list(tmp[1])
        del listaStara[-1]

        ime = tmp[0]

        #prvo vidi di je točka
        ind = ime.find('#')

        #je li na kraju,
        falseRet = []
        if ind+1 == len(ime):
            falseRet.append('{')
            return falseRet

        #ili je poslije nje zavrsni znak
        elif ime[ind+1] != '<':
            falseRet.append('#')
            return falseRet

        #ako smo tu u kodu znaci da slijedi nezavrsni znak => bit ce eps prijelaza
        #pogledaj koji je to znak

        znak1 = list(ime)
        del znak1 [:ind+1]
        znak1 = ''.join(znak1)
        ind1 = znak1.find('>')

        #ako je tocka nakon pomaka na kraju lista ce ostati ista (lista = listaStara)
        #jer je eps...
        lista = []
        if ind1+1 == len(znak1):
            lista.extend(listaStara)

        #ako je nakon točke zavrsni znak dodaj ga u listu
        #jer je on sam svoj skup započinje
        elif znak1[ind1+1] in self.zavrsni:
            lista.append(znak1[ind1+1])

        #na kraju ako nije ovo od prije znaci da je nezavrsni znak na redu
        else:
            #nadi koji je to nezavrsni znak i u listu ubaci zapocinje skup
            znak1 = list(znak1)

            znak2 = znak1[ind1+1:]
            znak2 = ''.join(znak2)
            ind2 = znak2.find('>')
            #sad pogledaj je li taj preostali niz ide u epsilon
            #jedino ako na 3. mjestu nema nista mozda moze ici u epsilon

            if ind2+1 == len(znak2):
                ide = 1

            #nema 3. znaka provjerit ces ide li u epsilon
            else:
                ide = 0


            znak2 = list(znak2)
            del znak2[ind2+1:]
            znak2 = ''.join(znak2)
            #u znak2 je sada znak koji je 2; poslije točke trenutno(ako je to nezavrsni)
            if znak2 in self.nezavrsni:
                lista.extend(self.dictZapocinje[znak2])
            else:
                #inače pronađi koji je to zavrsni
                ind6 = znak2.find('<')
                znak2 = list(znak2)
                del znak2[ind6:]
                znak2 = ''.join(znak2)
                lista.extend(znak2)

            #ako ima mogucnost da ode u epsilon provjeri, i ako je prazan
            #dodaj staru listu u novu
            if ide and znak2 in self.listaPraznih:
                lista.extend(listaStara)

        znak1 = list(znak1)
        del znak1 [ind1+1:]
        znak1 = ''.join(znak1)
        #u znak1 je sada znak koji moramo obraditi

        #dakle znak koji ce bit s lijeve strane imamo, sad pogledaj kakvu ces
        #listu poslati da se nadoda u novo stanje

        #pobrisi duplikate
        lista = list(set(lista))

        #u znak1 je sada znak za koji moramo stvoriti nova stanja, a u listi je ono što im pridružujemo

        lsTrenutnihStanja = []
        stanja = []

        for i in range(len(self.mapa[znak1])):
            lsTrenutnihStanja.append(self.mapa[znak1][i])

        lsZnak1 = [znak1, '->', '#']

        for i in range(len(lsTrenutnihStanja)):
            lsTrenutnihStanja[i] = lsZnak1 + lsTrenutnihStanja[i]
            stanja.append(self.stvoriStanje(lsTrenutnihStanja[i], lista))

        #rješava se #$
        for i in range(len(stanja)):
            pom = stanja[i]
            broj = pom.find('#$')
            if broj != -1:
                pom = pom.replace("#$","#")
                stanja[i] = pom

        #sređuje da liste budu ažurirane kako treba

        for j in range(len(stanja)):
            tmp = stanja[j].split('{')
            ime = tmp[0]+'{'
            for i in range(len(prijelazi)):
                if ime in prijelazi[i]:
                    stanja[j] = prijelazi[i]
                    break
        return stanja

    def nadiPrijelaz(self,stanje):
        #funkcija dobiva jedno stanje i vraca jedno stanje u koje je presla zbog procitanog znaka
        #pomaknute tocke, pritom ne mijenja listu
        #dodatno vraca i znak (bilo zavrsni ili nezavrsni) koji je procitala kao drugi clan liste
        ind = stanje.find('#')
        falseRet = []

        #ako nema prijelaza
        if stanje[ind+1] == '{':
            falseRet.append('{')
            return falseRet

        #inače generiraj novo stanje
        staro = ''
        staro += stanje

        staro = list(staro)
        prviDio = staro[:ind]
        prviDio = ''.join(prviDio)
        del staro[:ind+1]
        staro = ''.join(staro)

        znak = ''

        if stanje[ind+1] == '<':
            ind2 = staro.find('>')
            staro = list(staro)
            staro.insert(ind2+1,'#')
            staro = ''.join(staro)
            znak = staro[:ind2+1]
        else:
            ind3 = staro.find('<')
            ind4 = staro.find('{')
            if ind3 != -1:
                staro = list(staro)
                staro.insert(ind3,'#')
                staro = ''.join(staro)
                znak = staro[:ind3]
            elif ind4 != -1:
                staro = list(staro)
                staro.insert(ind4,'#')
                staro = ''.join(staro)
                znak = staro[:ind4]

        novo = prviDio+staro

        ret =[]
        ret.append(novo)
        ret.append(znak)
        return ret



















