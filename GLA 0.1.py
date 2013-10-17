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

def main():
    ulaz = open ('ulazna.txt','r')








if __name__ == '__main__':
  main()