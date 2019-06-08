#!/usr/bin/env python
# -*- coding: utf-8 -*-

import PyPDF2
import sys
import os

def text_extractor(path):

    print ("Abriendo " + sys.argv[1])

    pdf_file = sys.argv[1]
    read_pdf = PyPDF2.PdfFileReader(pdf_file)

    number_of_pages = read_pdf.getNumPages()
    print (str(number_of_pages) + " páginas leídas")

    out_page_content = 'out_page_csv.csv'
    os.system(("ps2ascii %s %s") %( pdf_file , out_page_content))

    convocatoria = "Ordinaria"
    asignatura = input("Asignatura a buscar: ")
    repetidas = 0
    f = open("out_page1_csv.csv", "r")
    lines = f.readlines()

    # Extraemos línea de los días de exámenes
    dias = []
    for line in lines:
        diasEx = line.split()
        for p in diasEx:
            if p==convocatoria:
                dias = diasEx
    cont = 0
    while cont < 4:
        dias.pop(0)
        cont+=1

    print(dias)

    # Extraemos línea de la asignatura en concreto
    for line in lines:
        palabras = line.split()
        for p in palabras:
            if p == asignatura:
                repetidas = repetidas+1
                print(palabras)
                if palabras[len(palabras)-1] == 'M':
                    print ("Exámen a las 9:00")
                elif palabras[len(palabras)-1] == 'T':
                    print ("Exámen a las 16:00") 

    if(repetidas>0):
        print ("La asignatura \"{0}\" se repite {1} veces en el archivo {2}".format(asignatura, repetidas, pdf_file))
    else:
        print ("No se ha encontrado")

if __name__ == '__main__':
    if sys.argv[1:]:
        path = sys.argv[1]
        text_extractor(path)
    else:
        print("Error: falta de parámetros")

