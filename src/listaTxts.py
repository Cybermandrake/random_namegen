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

filename="listaDocs.yml"

verbose = False
debug   = False

reservados = []
reservados.append('0000')

usados = []
duplicados = []

nomes = { "reservados":reservados, "em uso":usados, "duplicados": duplicados}

def listaTxts(path):
    '''Visita todos os subdiretórios em busca de arquivos \.txt e atualiza lista de nomes usados.
    '''
    for dirname, dirnames, filenames in os.walk('.'):
    # editing the 'dirnames' list will stop os.walk() from recursing into there.
        #if '.git' in dirnames:
        #    # don't go into any .git directories.
        #    dirnames.remove('.git')    


        # print path to all filenames.
        if (verbose or debug):
            print("filenames>>")
        for filename in filenames:
            if (filename.endswith('txt')):
                basename=filename[0:len(filename)-4]
                if (basename in usados):
                    duplicados.append(os.path.join(dirname,filename))
                usados.append(basename)
            if (verbose):
                print(os.path.join(dirname, filename))

        # print path to all subdirectories first.
        #print("dirnames>>")
        #for subdirname in dirnames:
        #    #listaTxts(subdirname)
        #    print(os.path.join(dirname, subdirname))
        
def main(argv=None):
    '''Procura no diretório corrente (e seus subdiretórios) arquivos terminados em "txt" e registra seus nomes.'''
    listaTxts('.')
    for nn in reservados:
        if nn in usados:
            reservados.remove(nn)
    
    if (verbose):
        print("Lista de usados:")
        for i in usados:
            print(i)
    print(json.dumps(nomes))
    with open("./"+filename, "w") as f:
        json.dump(nomes, f, indent=4)
    
if __name__ == '__main__':
	main()
