#!/usr/bin/python
# -*- coding: utf-8 -*-

# This is a wrapper script to run tests using the unittest
# framework. It setups the environment properly and defines some
# commandline options for running tests.
#
# Copyright 2008 Jaap Karssenberg <jaap.karssenberg@gmail.com>

import os
import json
import getopt
import random
import time

filename="listaDocs.yml"

verbose       = True
debug         = False
checkreserved = True
refusereserved= True

#nomes = { "reservados":reservados, "em uso":usados, "duplicados": duplicados}
nomes={}
usados = []
duplicados = []
reservados = []

def newName():
    pass
    
def nameIsGood(name):
    if (name in usados):
        return False
    if (refusereserved and name in reservados):
        return False
    return True

def main(argv=None):
    '''Apresenta um nome que não esteja sendo usado.'''
    seed=time.clock()
    random.seed(seed)
    anumber=random.randrange(1000,9999)
    
    with open("./"+filename, "r") as f:
        nomes = json.load(f)
        
    if (debug):
        print nomes.keys()
        
    reservados = nomes["reservados"]
    reservados.append('0000')

    usados = nomes["em uso"]
    duplicados = nomes["duplicados"]
    
    aStrNumber = str(anumber)
    if (verbose):
        print("Número aleatório: " + aStrNumber)
        #for i in usados:
        #    print(i)
    #while (aStrNumber in usados):
    while (not nameIsGood(aStrNumber)):
        if (verbose):
            print (aStrNumber + " está em uso ou reservado")
    if (checkreserved):
        if (aStrNumber in reservados):
            print("Aviso: " + aStrNumber + " é um nome reservado.")

    print("Novo nome: " + aStrNumber)
        
        
    #print(json.dumps(nomes))
    #with open("./"+filename, "w") as f:
    #    json.dump(nomes, f, indent=4)
    
if __name__ == '__main__':
	main()



