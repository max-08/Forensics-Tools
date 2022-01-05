#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 09:21:00 2021
Lo script cerca ogni singolo file CSV lo apre ed aggiunge tutte le righe nella 
lista dati, successivamente si crea il documento filecsvnuovo ed aggiunge tutto 
il contenuto della lista
 
spostare e rinominare copiare file
@author: max
"""

import os
import csv
dati = []
percorso = "/home/max/.config/spyder-py3"
for cartella, sottocartella, file in os.walk(percorso):
    print(f" Ci troviamo nella cartella corrente : '{ cartella}' ")
    print("")
#    print( f" Le sottocartelle presenti sono : '{ sottocartella}' ")
#    print(f"siamo nell cartella file ") "'{file}' ")    
# se vogliamo solo un tipo di file
    for miofile in file:
        if miofile.endswith(".csv"):
            with open(miofile) as filecsv:
                lettore = csv.reader(filecsv, delimiter =";")
                for parola in lettore:
                    dati.append(parola)
                    print(dati)

#creo un nuvo CSV copleto
outputfile =  open("filecsvNuovo", "w", newline=(''))
scrivofile = csv.writer(outputfile)
for i in dati:
    scrivofile.writerow(i)
print(f"i file inseriti sono: '{dati}'")
outputfile.close()

