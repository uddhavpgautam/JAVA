# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 00:26:36 2013

@author: Matko
"""


def main():
    ls = ['NIZ_ZNAKOVA', '|', 'UDJI_U_STANJE', '|', 'S_pocetno', '|']
    print ls
    string = ''.join(ls)
    print string
    ls2 = string.split('|')
    print ls2
    #dio koda koji slijedi primijeniti samo okoliko string završava znakom '|'
    #odnosno ako je zadnji član novonastale liste nastao nepotrebno
    #u konkretnom slučaju ovdje navedenom to je doista potrebno napraviti
    del ls2[-1]
    print ls2
    
    #da je lista izgledala ovako:
    #ls = ['NIZ_ZNAKOVA', '|', 'UDJI_U_STANJE', '|', 'S_pocetno'] to ne bi bilo potrebno raditi

if __name__ == '__main__':
  main()