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
    contAsig = datosNoNaN.iloc[3,:].count()
    cont10E = 0
    cont10Easig = 0
    exAsig10E = []
    asignatura = []

    while cont10E < contTope:
        if(examenes10Ene[cont10E]=='M'):
            asignatura = datosNoNaN.iloc[cont10E,:]
            while cont10Easig < contAsig:
                if(asignatura[cont10Easig] >= 'A' and asignatura[cont10Easig] <= 'z'):
                    exAsig10E.append(str(asignatura[cont10Easig]))
                cont10Easig+=1
        elif(examenes10Ene[cont10E]=='T'):
            asignatura = datosNoNaN.iloc[cont10E,:]
            cont10Easig = 0;
            while cont10Easig < contAsig:
                if(asignatura[cont10Easig] >= 'A' and asignatura[cont10Easig] <= 'z'):
                    exAsig10E.append(str(asignatura[cont10Easig]))
                cont10Easig+=1
        cont10E+=1
    ################################
    cont11E = 0
    cont11Easig = 0
    exAsig11E = []

    while cont11E < contTope:
        if(examenes11Ene[cont11E]=='M'):
            asignatura = datosNoNaN.iloc[cont11E,:]
            cont11Easig = 0
            while cont11Easig < contAsig:
                if(asignatura[cont11Easig] >= 'A' and asignatura[cont11Easig] <= 'z'):
                    exAsig11E.append(str(asignatura[cont11Easig]))
                cont11Easig+=1
        elif(examenes11Ene[cont11E]=='T'):
            asignatura = datosNoNaN.iloc[cont11E,:]
            cont11Easig = 0
            while cont11Easig < contAsig:
                if(asignatura[cont11Easig] >= 'A' and asignatura[cont11Easig] <= 'z'):
                    exAsig11E.append(str(asignatura[cont11Easig]))
                cont11Easig+=1
        cont11E+=1
    ################################
    cont14E = 0
    cont14Easig = 0
    exAsig14E = []

    while cont14E < contTope:
        if(examenes14Ene[cont14E]=='M'):
            asignatura = datosNoNaN.iloc[cont14E,:]
            cont14Easig = 0
            while cont14Easig < contAsig:
                if(asignatura[cont14Easig] >= 'A' and asignatura[cont14Easig] <= 'z'):
                    exAsig14E.append(str(asignatura[cont14Easig]))
                cont14Easig+=1
        elif(examenes14Ene[cont14E]=='T'):
            asignatura = datosNoNaN.iloc[cont14E,:]
            cont14Easig = 0
            while cont14Easig < contAsig:
                if(asignatura[cont14Easig] >= 'A' and asignatura[cont14Easig] <= 'z'):
                    exAsig14E.append(str(asignatura[cont14Easig]))
                cont14Easig+=1
        cont14E+=1
    ################################
    cont15E = 0
    cont15Easig = 0
    exAsig15E = []

    while cont15E < contTope:
        if(examenes15Ene[cont15E]=='M'):
            asignatura = datosNoNaN.iloc[cont15E,:]
            cont15Easig = 0
            while cont15Easig < contAsig:
                if(asignatura[cont15Easig] >= 'A' and asignatura[cont15Easig] <= 'z'):
                    exAsig15E.append(str(asignatura[cont15Easig]))
                cont15Easig+=1
        elif(examenes15Ene[cont15E]=='T'):
            asignatura = datosNoNaN.iloc[cont15E,:]
            cont15Easig = 0
            while cont15Easig < contAsig:
                if(asignatura[cont15Easig] >= 'A' and asignatura[cont15Easig] <= 'z'):
                    exAsig15E.append(str(asignatura[cont15Easig]))
                cont15Easig+=1
        cont15E+=1
    ################################
    cont16E = 0
    cont16Easig = 0
    exAsig16E = []

    while cont16E < contTope:
        if(examenes16Ene[cont16E]=='M'):
            asignatura = datosNoNaN.iloc[cont16E,:]
            cont16Easig = 0
            while cont16Easig < contAsig:
                if(asignatura[cont16Easig] >= 'A' and asignatura[cont16Easig] <= 'z'):
                    exAsig16E.append(str(asignatura[cont16Easig]))
                cont16Easig+=1
        elif(examenes16Ene[cont16E]=='T'):
            asignatura = datosNoNaN.iloc[cont16E,:]
            cont16Easig = 0
            while cont16Easig < contAsig:
                if(asignatura[cont16Easig] >= 'A' and asignatura[cont16Easig] <= 'z'):
                    exAsig16E.append(str(asignatura[cont16Easig]))
                cont16Easig+=1
        cont16E+=1
    ################################
    cont17E = 0
    cont17Easig = 0
    exAsig17E = []

    while cont17E < contTope:
        if(examenes17Ene[cont17E]=='M'):
            asignatura = datosNoNaN.iloc[cont17E,:]
            cont17Easig = 0
            while cont17Easig < contAsig:
                if(asignatura[cont17Easig] >= 'A' and asignatura[cont17Easig] <= 'z'):
                    exAsig17E.append(str(asignatura[cont17Easig]))
                cont17Easig+=1
        elif(examenes17Ene[cont17E]=='T'):
            asignatura = datosNoNaN.iloc[cont17E,:]
            cont17Easig = 0
            while cont17Easig < contAsig:
                if(asignatura[cont17Easig] >= 'A' and asignatura[cont17Easig] <= 'z'):
                    exAsig17E.append(str(asignatura[cont17Easig]))
                cont17Easig+=1
        cont17E+=1
    ################################
    cont18E = 0
    cont18Easig = 0
    exAsig18E = []

    while cont18E < contTope:
        if(examenes18Ene[cont18E]=='M'):
            asignatura = datosNoNaN.iloc[cont18E,:]
            cont18Easig = 0
            while cont18Easig < contAsig:
                if(asignatura[cont18Easig] >= 'A' and asignatura[cont18Easig] <= 'z'):
                    exAsig18E.append(str(asignatura[cont18Easig]))
                cont18Easig+=1
        elif(examenes18Ene[cont18E]=='T'):
            asignatura = datosNoNaN.iloc[cont18E,:]
            cont18Easig = 0
            while cont18Easig < contAsig:
                if(asignatura[cont18Easig] >= 'A' and asignatura[cont18Easig] <= 'z'):
                    exAsig18E.append(str(asignatura[cont18Easig]))
                cont18Easig+=1
        cont18E+=1
    ################################
    cont21E = 0
    cont21Easig = 0
    exAsig21E = []

    while cont21E < contTope:
        if(examenes21Ene[cont21E]=='M'):
            asignatura = datosNoNaN.iloc[cont21E,:]
            cont21Easig = 0
            while cont21Easig < contAsig:
                if(asignatura[cont21Easig] >= 'A' and asignatura[cont21Easig] <= 'z'):
                    exAsig21E.append(str(asignatura[cont21Easig]))
                cont21Easig+=1
        elif(examenes21Ene[cont21E]=='T'):
            asignatura = datosNoNaN.iloc[cont21E,:]
            cont21Easig = 0
            while cont21Easig < contAsig:
                if(asignatura[cont21Easig] >= 'A' and asignatura[cont21Easig] <= 'z'):
                    exAsig21E.append(str(asignatura[cont21Easig]))
                cont21Easig+=1
        cont21E+=1
    ################################
    cont22E = 0
    cont22Easig = 0
    exAsig22E = []

    while cont22E < contTope:
        if(examenes22Ene[cont22E]=='M'):
            asignatura = datosNoNaN.iloc[cont22E,:]
            cont22Easig = 0
            while cont22Easig < contAsig:
                if(asignatura[cont22Easig] >= 'A' and asignatura[cont22Easig] <= 'z'):
                    exAsig22E.append(str(asignatura[cont22Easig]))
                cont22Easig+=1
        elif(examenes22Ene[cont22E]=='T'):
            asignatura = datosNoNaN.iloc[cont22E,:]
            cont22Easig = 0
            while cont22Easig < contAsig:
                if(asignatura[cont22Easig] >= 'A' and asignatura[cont22Easig] <= 'z'):
                    exAsig22E.append(str(asignatura[cont22Easig]))
                cont22Easig+=1
        cont22E+=1
    ################################
    cont23E = 0
    cont23Easig = 0
    exAsig23E = []

    while cont23E < contTope:
        if(examenes23Ene[cont23E]=='M'):
            asignatura = datosNoNaN.iloc[cont23E,:]
            cont23Easig = 0
            while cont23Easig < contAsig:
                if(asignatura[cont23Easig] >= 'A' and asignatura[cont23Easig] <= 'z'):
                    exAsig23E.append(str(asignatura[cont23Easig]))
                cont23Easig+=1
        elif(examenes23Ene[cont23E]=='T'):
            asignatura = datosNoNaN.iloc[cont23E,:]
            cont23Easig = 0
            while cont23Easig < contAsig:
                if(asignatura[cont23Easig] >= 'A' and asignatura[cont23Easig] <= 'z'):
                    exAsig23E.append(str(asignatura[cont23Easig]))
                cont23Easig+=1
        cont23E+=1
    ################################
    #Comprobación del contenido
    cont=0
    while cont < len(exAsig23E):
        print(str(exAsig23E[cont]))
        cont+=1

    # for num in datosNoNaN:
    #     print (datosNoNaN[num:num+1])