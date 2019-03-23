#!/usr/bin/env python
# -*- coding: utf-8 -*-

import camelot
import csv
import os
import pandas as pd

RESOURCE = './resources'
OUTPUT = './outputs'

tablas = camelot.read_pdf(os.path.join(RESOURCE, 'CalendarioExamenes18-19-GII.pdf'))
tablas.export(os.path.join(OUTPUT, 'CalendarioExamenes18-19-GII.csv'), f='csv', compress=False)

with open(os.path.join(OUTPUT, 'CalendarioExamenes18-19-GII-page-1-table-1.csv'), 'r') as archivo:  
    datos = pd.read_csv(archivo, header=-1)
    datosNoNaN = datos.fillna(value='0')

    examenes10Ene = datosNoNaN.iloc[:,6]
    examenes11Ene = datosNoNaN.iloc[:,7]
    examenes14Ene = datosNoNaN.iloc[:,9]
    examenes15Ene = datosNoNaN.iloc[:,10]
    examenes16Ene = datosNoNaN.iloc[:,11]
    examenes17Ene = datosNoNaN.iloc[:,12]
    examenes18Ene = datosNoNaN.iloc[:,13]
    examenes21Ene = datosNoNaN.iloc[:,15]
    examenes22Ene = datosNoNaN.iloc[:,16]
    examenes23Ene = datosNoNaN.iloc[:,17]

    # print(examenes10Ene.value_counts())
    # print(examenes10Ene.count())
    # print(examenes10Ene)
    
    contTope = examenes10Ene.count()
    cont10E = 0;
    exAsig10E = []

    while cont10E < contTope:
        if(examenes10Ene[cont10E]=='M'):
            # print('El 10 de enero hay un examen por la maniana en la posicion ' + str(cont10E-2))
            exAsig10E.append('M')
            exAsig10E.append(str(cont10E-2))
        elif(examenes10Ene[cont10E]=='T'):
            # print('El 10 de enero hay un examen por la tarde en la posicion ' + str(cont10E-2))
            exAsig10E.append('T')
            exAsig10E.append(str(cont10E-2))
        cont10E+=1
    ################################
    cont11E = 0;
    exAsig11E = []

    while cont11E < contTope:
        if(examenes11Ene[cont11E]=='M'):
            exAsig11E.append('M')
            exAsig11E.append(str(cont11E-2))
        elif(examenes11Ene[cont11E]=='T'):
            exAsig11E.append('T')
            exAsig11E.append(str(cont11E-2))            
        cont11E+=1
    ################################
    cont14E = 0;
    exAsig14E = []

    while cont14E < contTope:
        if(examenes14Ene[cont14E]=='M'):
            exAsig14E.append('M')
            exAsig14E.append(str(cont14E-2))
        elif(examenes14Ene[cont14E]=='T'):
            exAsig14E.append('T')
            exAsig14E.append(str(cont14E-2))            
        cont14E+=1
    ################################
    cont15E = 0;
    exAsig15E = []

    while cont15E < contTope:
        if(examenes15Ene[cont15E]=='M'):
            exAsig15E.append('M')
            exAsig15E.append(str(cont15E-2))
        elif(examenes15Ene[cont15E]=='T'):
            exAsig15E.append('T')
            exAsig15E.append(str(cont15E-2))            
        cont15E+=1
    ################################
    cont16E = 0;
    exAsig16E = []

    while cont16E < contTope:
        if(examenes16Ene[cont16E]=='M'):
            exAsig16E.append('M')
            exAsig16E.append(str(cont16E-2))
        elif(examenes16Ene[cont16E]=='T'):
            exAsig16E.append('T')
            exAsig16E.append(str(cont16E-2))            
        cont16E+=1
    ################################
    cont17E = 0;
    exAsig17E = []

    while cont17E < contTope:
        if(examenes17Ene[cont17E]=='M'):
            exAsig17E.append('M')
            exAsig17E.append(str(cont17E-2))
        elif(examenes17Ene[cont17E]=='T'):
            exAsig17E.append('T')
            exAsig17E.append(str(cont17E-2))            
        cont17E+=1
    ################################
    cont18E = 0;
    exAsig18E = []

    while cont18E < contTope:
        if(examenes18Ene[cont18E]=='M'):
            exAsig18E.append('M')
            exAsig18E.append(str(cont18E-2))
        elif(examenes18Ene[cont18E]=='T'):
            exAsig18E.append('T')
            exAsig18E.append(str(cont18E-2))            
        cont18E+=1
    ################################
    cont21E = 0;
    exAsig21E = []

    while cont21E < contTope:
        if(examenes21Ene[cont21E]=='M'):
            exAsig21E.append('M')
            exAsig21E.append(str(cont21E-2))
        elif(examenes21Ene[cont21E]=='T'):
            exAsig21E.append('T')
            exAsig21E.append(str(cont21E-2))            
        cont21E+=1
    ################################
    cont22E = 0;
    exAsig22E = []

    while cont22E < contTope:
        if(examenes22Ene[cont22E]=='M'):
            exAsig22E.append('M')
            exAsig22E.append(str(cont22E-2))
        elif(examenes22Ene[cont22E]=='T'):
            exAsig22E.append('T')
            exAsig22E.append(str(cont22E-2))            
        cont22E+=1
    ################################
    cont23E = 0;
    exAsig23E = []

    while cont23E < contTope:
        if(examenes23Ene[cont23E]=='M'):
            exAsig23E.append('M')
            exAsig23E.append(str(cont23E-2))
        elif(examenes23Ene[cont23E]=='T'):
            exAsig23E.append('T')
            exAsig23E.append(str(cont23E-2))            
        cont23E+=1
    ################################
    #Comprobación del contenido
    cont=0
    while cont < len(exAsig23E):
        print(str(exAsig23E[cont]))
        cont+=1

    # for num in datosNoNaN:
    #     print (datosNoNaN[num:num+1])
        # print (datosNoNaN[4:5])
