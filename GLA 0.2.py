# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 23:36:19 2013

@author: Matko
"""

import sys

class Automat(object):
    
    def __init__(self):
        pass
    
    br_stanja = 0
    
    def novo_stanje(self):
        self.br_stanja = self.br_stanja + 1
        return self.br_stanja - 1 
        
def je_operator(izraz,i):
    br = 0
    while i-1 >= 0 and izraz[i] == '\\':
        br = br+1
        i = i-1
    return br%2 == 0    
    
def pretvori(izraz,automat):
    izbori = []
    br_zagrada = 0
    
    for i in range(len(izraz)):
        if izraz[i] == '(' and je_operator (izraz,i):
            br_zagrada = br_zagrada + 1
        elif izraz[i] == ')' and je_operator(izraz,i):
            br_zagrada = br_zagrada - 1
        elif br_zagrada == 0 and izraz [i] == '|' and je_operator(izraz,i):
            
    

def main():
    ulaz = open ('ulazna.txt','r')

    izraz = []






if __name__ == '__main__':
  main()