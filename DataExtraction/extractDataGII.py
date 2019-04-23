#!/usr/bin/env python
# -*- coding: utf-8 -*-

import camelot
import csv
import os
import pandas as pd
import sys
import psycopg2

RESOURCE = './resources'
OUTPUT = './outputs'

db = os.environ['NAME_DB']
host_db = os.environ['HOST_DB']
usuario = os.environ['USER_DB']
pw = os.environ['PW_DB']


def extractDataTable1_1SemOrdinaria(asignaturaEX):
    tablas = camelot.read_pdf(os.path.join(
        RESOURCE, 'CalendarioExamenes18-19-GII.pdf'))
    tablas.export(os.path.join(
        OUTPUT, 'CalendarioExamenes18-19-GII.csv'), f='csv', compress=False)

    with open(os.path.join(OUTPUT, 'CalendarioExamenes18-19-GII-page-1-table-1.csv'), 'r') as archivo:
        datos = pd.read_csv(archivo, header=-1)
        datosNoNaN = datos.fillna(value='0')

        examenes10Ene = datosNoNaN.iloc[:, 6]
        examenes11Ene = datosNoNaN.iloc[:, 7]
        examenes14Ene = datosNoNaN.iloc[:, 9]
        examenes15Ene = datosNoNaN.iloc[:, 10]
        examenes16Ene = datosNoNaN.iloc[:, 11]
        examenes17Ene = datosNoNaN.iloc[:, 12]
        examenes18Ene = datosNoNaN.iloc[:, 13]
        examenes21Ene = datosNoNaN.iloc[:, 15]
        examenes22Ene = datosNoNaN.iloc[:, 16]
        examenes23Ene = datosNoNaN.iloc[:, 17]

        contTope = examenes10Ene.count()
        contAsig = datosNoNaN.iloc[3, :].count()
        cont10E = 0
        cont10Easig = 0
        exAsig10E = []
        asignatura = []
        resultado = []

        while cont10E < contTope:
            if(examenes10Ene[cont10E] == 'M'):
                asignatura = datosNoNaN.iloc[cont10E, :]
                while cont10Easig < contAsig:
                    if(asignatura[cont10Easig] >= 'A' and asignatura[cont10Easig] <= 'z'):
                        # if(asignatura[cont10Easig]==asignaturaEX):
                        #     resultado.append("10 de Enero")
                        #     resultado.append(asignatura[cont10Easig])
                        #     resultado.append(asignatura[cont10Easig+1])
                        #     resultado.append(asignatura[cont10Easig+2])
                        exAsig10E.append(str(asignatura[cont10Easig]))
                    cont10Easig += 1
            elif(examenes10Ene[cont10E] == 'T'):
                asignatura = datosNoNaN.iloc[cont10E, :]
                cont10Easig = 0
                while cont10Easig < contAsig:
                    if(asignatura[cont10Easig] >= 'A' and asignatura[cont10Easig] <= 'z'):
                        exAsig10E.append(str(asignatura[cont10Easig]))
                    cont10Easig += 1
            cont10E += 1
        ################################
        cont11E = 0
        cont11Easig = 0
        exAsig11E = []

        while cont11E < contTope:
            if(examenes11Ene[cont11E] == 'M'):
                asignatura = datosNoNaN.iloc[cont11E, :]
                cont11Easig = 0
                while cont11Easig < contAsig:
                    if(asignatura[cont11Easig] >= 'A' and asignatura[cont11Easig] <= 'z'):
                        exAsig11E.append(str(asignatura[cont11Easig]))
                    cont11Easig += 1
            elif(examenes11Ene[cont11E] == 'T'):
                asignatura = datosNoNaN.iloc[cont11E, :]
                cont11Easig = 0
                while cont11Easig < contAsig:
                    if(asignatura[cont11Easig] >= 'A' and asignatura[cont11Easig] <= 'z'):
                        exAsig11E.append(str(asignatura[cont11Easig]))
                    cont11Easig += 1
            cont11E += 1
        ################################
        cont14E = 0
        cont14Easig = 0
        exAsig14E = []

        while cont14E < contTope:
            if(examenes14Ene[cont14E] == 'M'):
                asignatura = datosNoNaN.iloc[cont14E, :]
                cont14Easig = 0
                while cont14Easig < contAsig:
                    if(asignatura[cont14Easig] >= 'A' and asignatura[cont14Easig] <= 'z'):
                        exAsig14E.append(str(asignatura[cont14Easig]))
                    cont14Easig += 1
            elif(examenes14Ene[cont14E] == 'T'):
                asignatura = datosNoNaN.iloc[cont14E, :]
                cont14Easig = 0
                while cont14Easig < contAsig:
                    if(asignatura[cont14Easig] >= 'A' and asignatura[cont14Easig] <= 'z'):
                        exAsig14E.append(str(asignatura[cont14Easig]))
                    cont14Easig += 1
            cont14E += 1
        ################################
        cont15E = 0
        cont15Easig = 0
        exAsig15E = []

        while cont15E < contTope:
            if(examenes15Ene[cont15E] == 'M'):
                asignatura = datosNoNaN.iloc[cont15E, :]
                cont15Easig = 0
                while cont15Easig < contAsig:
                    if(asignatura[cont15Easig] >= 'A' and asignatura[cont15Easig] <= 'z'):
                        exAsig15E.append(str(asignatura[cont15Easig]))
                    cont15Easig += 1
            elif(examenes15Ene[cont15E] == 'T'):
                asignatura = datosNoNaN.iloc[cont15E, :]
                cont15Easig = 0
                while cont15Easig < contAsig:
                    if(asignatura[cont15Easig] >= 'A' and asignatura[cont15Easig] <= 'z'):
                        exAsig15E.append(str(asignatura[cont15Easig]))
                    cont15Easig += 1
            cont15E += 1

        ################################
        cont16E = 0
        cont16Easig = 0
        exAsig16E = []

        while cont16E < contTope:
            if(examenes16Ene[cont16E] == 'M'):
                asignatura = datosNoNaN.iloc[cont16E, :]
                cont16Easig = 0
                while cont16Easig < contAsig:
                    if(asignatura[cont16Easig] >= 'A' and asignatura[cont16Easig] <= 'z'):
                        exAsig16E.append(str(asignatura[cont16Easig]))
                    cont16Easig += 1
            elif(examenes16Ene[cont16E] == 'T'):
                asignatura = datosNoNaN.iloc[cont16E, :]
                cont16Easig = 0
                while cont16Easig < contAsig:
                    if(asignatura[cont16Easig] >= 'A' and asignatura[cont16Easig] <= 'z'):
                        exAsig16E.append(str(asignatura[cont16Easig]))
                    cont16Easig += 1
            cont16E += 1
        ################################
        cont17E = 0
        cont17Easig = 0
        exAsig17E = []

        while cont17E < contTope:
            if(examenes17Ene[cont17E] == 'M'):
                asignatura = datosNoNaN.iloc[cont17E, :]
                cont17Easig = 0
                while cont17Easig < contAsig:
                    if(asignatura[cont17Easig] >= 'A' and asignatura[cont17Easig] <= 'z'):
                        exAsig17E.append(str(asignatura[cont17Easig]))
                    cont17Easig += 1
            elif(examenes17Ene[cont17E] == 'T'):
                asignatura = datosNoNaN.iloc[cont17E, :]
                cont17Easig = 0
                while cont17Easig < contAsig:
                    if(asignatura[cont17Easig] >= 'A' and asignatura[cont17Easig] <= 'z'):
                        exAsig17E.append(str(asignatura[cont17Easig]))
                    cont17Easig += 1
            cont17E += 1
        ################################
        cont18E = 0
        cont18Easig = 0
        exAsig18E = []

        while cont18E < contTope:
            if(examenes18Ene[cont18E] == 'M'):
                asignatura = datosNoNaN.iloc[cont18E, :]
                cont18Easig = 0
                while cont18Easig < contAsig:
                    if(asignatura[cont18Easig] >= 'A' and asignatura[cont18Easig] <= 'z'):
                        exAsig18E.append(str(asignatura[cont18Easig]))
                    cont18Easig += 1
            elif(examenes18Ene[cont18E] == 'T'):
                asignatura = datosNoNaN.iloc[cont18E, :]
                cont18Easig = 0
                while cont18Easig < contAsig:
                    if(asignatura[cont18Easig] >= 'A' and asignatura[cont18Easig] <= 'z'):
                        exAsig18E.append(str(asignatura[cont18Easig]))
                    cont18Easig += 1
            cont18E += 1
        ################################
        cont21E = 0
        cont21Easig = 0
        exAsig21E = []

        while cont21E < contTope:
            if(examenes21Ene[cont21E] == 'M'):
                asignatura = datosNoNaN.iloc[cont21E, :]
                cont21Easig = 0
                while cont21Easig < contAsig:
                    if(asignatura[cont21Easig] >= 'A' and asignatura[cont21Easig] <= 'z'):
                        exAsig21E.append(str(asignatura[cont21Easig]))
                    cont21Easig += 1
            elif(examenes21Ene[cont21E] == 'T'):
                asignatura = datosNoNaN.iloc[cont21E, :]
                cont21Easig = 0
                while cont21Easig < contAsig:
                    if(asignatura[cont21Easig] >= 'A' and asignatura[cont21Easig] <= 'z'):
                        exAsig21E.append(str(asignatura[cont21Easig]))
                    cont21Easig += 1
            cont21E += 1
        ################################
        cont22E = 0
        cont22Easig = 0
        exAsig22E = []

        while cont22E < contTope:
            if(examenes22Ene[cont22E] == 'M'):
                asignatura = datosNoNaN.iloc[cont22E, :]
                cont22Easig = 0
                while cont22Easig < contAsig:
                    if(asignatura[cont22Easig] >= 'A' and asignatura[cont22Easig] <= 'É'):
                        exAsig22E.append(str(asignatura[cont22Easig]))
                    cont22Easig += 1
            elif(examenes22Ene[cont22E] == 'T'):
                asignatura = datosNoNaN.iloc[cont22E, :]
                cont22Easig = 0
                while cont22Easig < contAsig:
                    if(asignatura[cont22Easig] >= 'A' and asignatura[cont22Easig] <= 'z'):
                        exAsig22E.append(str(asignatura[cont22Easig]))
                    cont22Easig += 1
            cont22E += 1
        ################################
        cont23E = 0
        cont23Easig = 0
        exAsig23E = []

        while cont23E < contTope:
            if(examenes23Ene[cont23E] == 'M'):
                asignatura = datosNoNaN.iloc[cont23E, :]
                cont23Easig = 0
                while cont23Easig < contAsig:
                    if(asignatura[cont23Easig] >= 'A' and asignatura[cont23Easig] <= 'z'):
                        exAsig23E.append(str(asignatura[cont23Easig]))
                    cont23Easig += 1
            elif(examenes23Ene[cont23E] == 'T'):
                asignatura = datosNoNaN.iloc[cont23E, :]
                cont23Easig = 0
                while cont23Easig < contAsig:
                    if(asignatura[cont23Easig] >= 'A' and asignatura[cont23Easig] <= 'z'):
                        exAsig23E.append(str(asignatura[cont23Easig]))
                    cont23Easig += 1
            cont23E += 1
        ################################
        # Comprobación del contenido
        cont = 0
        resultado = []
        encontrado  = False

        while(cont < len(exAsig10E) and (encontrado == False)):
            if(exAsig10E[cont] == asignaturaEX):
                resultado.append("10 de Enero")
                resultado.append(exAsig10E[cont])
                resultado.append(exAsig10E[cont+1])
                resultado.append(exAsig10E[cont+2])
                encontrado = True
            cont += 1
        
        cont = 0
        while(cont < len(exAsig11E) and (encontrado == False)):
            if(exAsig11E[cont] == asignaturaEX):
                resultado.append("11 de Enero")
                resultado.append(exAsig11E[cont])
                resultado.append(exAsig11E[cont+1])
                resultado.append(exAsig11E[cont+2])
                encontrado = True
            cont += 1

        cont = 0
        while(cont < len(exAsig14E) and (encontrado == False)):
            if(exAsig14E[cont] == asignaturaEX):
                resultado.append("14 de Enero")
                resultado.append(exAsig14E[cont])
                resultado.append(exAsig14E[cont+1])
                resultado.append(exAsig14E[cont+2])
                encontrado = True
            cont += 1

        cont = 0
        while(cont < len(exAsig15E) and (encontrado == False)):
            if(exAsig15E[cont] == asignaturaEX):
                resultado.append("15 de Enero")
                resultado.append(exAsig15E[cont])
                resultado.append(exAsig15E[cont+1])
                resultado.append(exAsig15E[cont+2])
                encontrado = True
            cont += 1

        cont = 0
        while(cont < len(exAsig16E) and (encontrado == False)):
            if(exAsig16E[cont] == asignaturaEX):
                resultado.append("16 de Enero")
                resultado.append(exAsig16E[cont])
                resultado.append(exAsig16E[cont+1])
                resultado.append(exAsig16E[cont+2])
                encontrado = True
            cont += 1
    
        cont = 0
        while(cont < len(exAsig17E) and (encontrado == False)):
            if(exAsig17E[cont] == asignaturaEX):
                resultado.append("17 de Enero")
                resultado.append(exAsig17E[cont])
                resultado.append(exAsig17E[cont+1])
                resultado.append(exAsig17E[cont+2])
                encontrado = True
            cont += 1

        cont = 0
        while(cont < len(exAsig18E) and (encontrado == False)):
            if(exAsig18E[cont] == asignaturaEX):
                resultado.append("18 de Enero")
                resultado.append(exAsig18E[cont])
                resultado.append(exAsig18E[cont+1])
                resultado.append(exAsig18E[cont+2])
                encontrado = True
            cont += 1

        cont = 0
        while(cont < len(exAsig21E) and (encontrado == False)):
            if(exAsig21E[cont] == asignaturaEX):
                resultado.append("21 de Enero")
                resultado.append(exAsig21E[cont])
                resultado.append(exAsig21E[cont+1])
                resultado.append(exAsig21E[cont+2])
                encontrado = True
            cont += 1

        cont = 0
        while(cont < len(exAsig22E) and (encontrado == False)):
            if(exAsig22E[cont] == asignaturaEX):
                resultado.append("22 de Enero")
                resultado.append(exAsig22E[cont])
                resultado.append(exAsig22E[cont+1])
                resultado.append(exAsig22E[cont+2])
                encontrado = True
            cont += 1
        
        cont = 0
        while(cont < len(exAsig23E) and (encontrado == False)):
            if(exAsig23E[cont] == asignaturaEX):
                resultado.append("23 de Enero")
                resultado.append(exAsig23E[cont])
                resultado.append(exAsig23E[cont+1])
                resultado.append(exAsig23E[cont+2])
                encontrado = True
            cont += 1

        return resultado


def extractDataTable2_1SemOrdinaria(asignaturaEX):
    tablas = camelot.read_pdf(os.path.join(
        RESOURCE, 'CalendarioExamenes18-19-GII.pdf'), pages='2')
    tablas.export(os.path.join(
        OUTPUT, 'CalendarioExamenes18-19-GII.csv'), f='csv', compress=False)

    with open(os.path.join(OUTPUT, 'CalendarioExamenes18-19-GII-page-2-table-1.csv'), 'r') as archivo:
        datos = pd.read_csv(archivo, header=-1)
        datosNoNaN = datos.fillna(value='0')

        examenes10Ene = datosNoNaN.iloc[:, 6]
        examenes11Ene = datosNoNaN.iloc[:, 7]
        examenes14Ene = datosNoNaN.iloc[:, 9]
        examenes15Ene = datosNoNaN.iloc[:, 10]
        examenes16Ene = datosNoNaN.iloc[:, 11]
        examenes17Ene = datosNoNaN.iloc[:, 12]
        examenes18Ene = datosNoNaN.iloc[:, 13]
        examenes21Ene = datosNoNaN.iloc[:, 15]
        examenes22Ene = datosNoNaN.iloc[:, 16]
        examenes23Ene = datosNoNaN.iloc[:, 17]

        # print(examenes10Ene.value_counts())
        # print(examenes10Ene.count())
        # print(examenes18Ene)
        # print(datosNoNaN.iloc[3,:])

        contTope = examenes10Ene.count()
        contAsig = datosNoNaN.iloc[3, :].count()
        cont10E = 0
        cont10Easig = 0
        exAsig10E = []
        asignatura = []

        while cont10E < contTope:
            if(examenes10Ene[cont10E] == 'M'):
                asignatura = datosNoNaN.iloc[cont10E, :]
                while cont10Easig < contAsig:
                    if(asignatura[cont10Easig] >= 'A' and asignatura[cont10Easig] <= 'z'):
                        exAsig10E.append(str(asignatura[cont10Easig]))
                    cont10Easig += 1
            elif(examenes10Ene[cont10E] == 'T'):
                asignatura = datosNoNaN.iloc[cont10E, :]
                cont10Easig = 0
                while cont10Easig < contAsig:
                    if(asignatura[cont10Easig] >= 'A' and asignatura[cont10Easig] <= 'z'):
                        exAsig10E.append(str(asignatura[cont10Easig]))
                    cont10Easig += 1
            cont10E += 1
        ################################
        cont11E = 0
        cont11Easig = 0
        exAsig11E = []

        while cont11E < contTope:
            if(examenes11Ene[cont11E] == 'M'):
                asignatura = datosNoNaN.iloc[cont11E, :]
                cont11Easig = 0
                while cont11Easig < contAsig:
                    if(asignatura[cont11Easig] >= 'A' and asignatura[cont11Easig] <= 'z'):
                        exAsig11E.append(str(asignatura[cont11Easig]))
                    cont11Easig += 1
            elif(examenes11Ene[cont11E] == 'T'):
                asignatura = datosNoNaN.iloc[cont11E, :]
                cont11Easig = 0
                while cont11Easig < contAsig:
                    if(asignatura[cont11Easig] >= 'A' and asignatura[cont11Easig] <= 'z'):
                        exAsig11E.append(str(asignatura[cont11Easig]))
                    cont11Easig += 1
            cont11E += 1
        ################################
        cont14E = 0
        cont14Easig = 0
        exAsig14E = []

        while cont14E < contTope:
            if(examenes14Ene[cont14E] == 'M'):
                asignatura = datosNoNaN.iloc[cont14E, :]
                cont14Easig = 0
                while cont14Easig < contAsig:
                    if(asignatura[cont14Easig] >= 'A' and asignatura[cont14Easig] <= 'z'):
                        exAsig14E.append(str(asignatura[cont14Easig]))
                    cont14Easig += 1
            elif(examenes14Ene[cont14E] == 'T'):
                asignatura = datosNoNaN.iloc[cont14E, :]
                cont14Easig = 0
                while cont14Easig < contAsig:
                    if(asignatura[cont14Easig] >= 'A' and asignatura[cont14Easig] <= 'z'):
                        exAsig14E.append(str(asignatura[cont14Easig]))
                    cont14Easig += 1
            cont14E += 1
        ################################
        cont15E = 0
        cont15Easig = 0
        exAsig15E = []

        while cont15E < contTope:
            if(examenes15Ene[cont15E] == 'M'):
                asignatura = datosNoNaN.iloc[cont15E, :]
                cont15Easig = 0
                while cont15Easig < contAsig:
                    if(asignatura[cont15Easig] >= 'A' and asignatura[cont15Easig] <= 'z'):
                        exAsig15E.append(str(asignatura[cont15Easig]))
                    cont15Easig += 1
            elif(examenes15Ene[cont15E] == 'T'):
                asignatura = datosNoNaN.iloc[cont15E, :]
                cont15Easig = 0
                while cont15Easig < contAsig:
                    if(asignatura[cont15Easig] >= 'A' and asignatura[cont15Easig] <= 'z'):
                        exAsig15E.append(str(asignatura[cont15Easig]))
                    cont15Easig += 1
            cont15E += 1
        ################################
        cont16E = 0
        cont16Easig = 0
        exAsig16E = []

        while cont16E < contTope:
            if(examenes16Ene[cont16E] == 'M'):
                asignatura = datosNoNaN.iloc[cont16E, :]
                cont16Easig = 0
                while cont16Easig < contAsig:
                    if(asignatura[cont16Easig] >= 'A' and asignatura[cont16Easig] <= 'z'):
                        exAsig16E.append(str(asignatura[cont16Easig]))
                    cont16Easig += 1
            elif(examenes16Ene[cont16E] == 'T'):
                asignatura = datosNoNaN.iloc[cont16E, :]
                cont16Easig = 0
                while cont16Easig < contAsig:
                    if(asignatura[cont16Easig] >= 'A' and asignatura[cont16Easig] <= 'z'):
                        exAsig16E.append(str(asignatura[cont16Easig]))
                    cont16Easig += 1
            cont16E += 1
        ################################
        cont17E = 0
        cont17Easig = 0
        exAsig17E = []

        while cont17E < contTope:
            if(examenes17Ene[cont17E] == 'M'):
                asignatura = datosNoNaN.iloc[cont17E, :]
                cont17Easig = 0
                while cont17Easig < contAsig:
                    if(asignatura[cont17Easig] >= 'A' and asignatura[cont17Easig] <= 'z'):
                        exAsig17E.append(str(asignatura[cont17Easig]))
                    cont17Easig += 1
            elif(examenes17Ene[cont17E] == 'T'):
                asignatura = datosNoNaN.iloc[cont17E, :]
                cont17Easig = 0
                while cont17Easig < contAsig:
                    if(asignatura[cont17Easig] >= 'A' and asignatura[cont17Easig] <= 'z'):
                        exAsig17E.append(str(asignatura[cont17Easig]))
                    cont17Easig += 1
            cont17E += 1
        ################################
        cont18E = 0
        cont18Easig = 0
        exAsig18E = []

        while cont18E < contTope:
            if(examenes18Ene[cont18E] == 'M'):
                asignatura = datosNoNaN.iloc[cont18E, :]
                cont18Easig = 0
                while cont18Easig < contAsig:
                    if(asignatura[cont18Easig] >= 'A' and asignatura[cont18Easig] <= 'z'):
                        exAsig18E.append(str(asignatura[cont18Easig]))
                    cont18Easig += 1
            elif(examenes18Ene[cont18E] == 'T'):
                asignatura = datosNoNaN.iloc[cont18E, :]
                cont18Easig = 0
                while cont18Easig < contAsig:
                    if(asignatura[cont18Easig] >= 'A' and asignatura[cont18Easig] <= 'z'):
                        exAsig18E.append(str(asignatura[cont18Easig]))
                    cont18Easig += 1
            cont18E += 1
        ################################
        cont21E = 0
        cont21Easig = 0
        exAsig21E = []

        while cont21E < contTope:
            if(examenes21Ene[cont21E] == 'M'):
                asignatura = datosNoNaN.iloc[cont21E, :]
                cont21Easig = 0
                while cont21Easig < contAsig:
                    if(asignatura[cont21Easig] >= 'A' and asignatura[cont21Easig] <= 'z'):
                        exAsig21E.append(str(asignatura[cont21Easig]))
                    cont21Easig += 1
            elif(examenes21Ene[cont21E] == 'T'):
                asignatura = datosNoNaN.iloc[cont21E, :]
                cont21Easig = 0
                while cont21Easig < contAsig:
                    if(asignatura[cont21Easig] >= 'A' and asignatura[cont21Easig] <= 'z'):
                        exAsig21E.append(str(asignatura[cont21Easig]))
                    cont21Easig += 1
            cont21E += 1
        ################################
        cont22E = 0
        cont22Easig = 0
        exAsig22E = []

        while cont22E < contTope:
            if(examenes22Ene[cont22E] == 'M'):
                asignatura = datosNoNaN.iloc[cont22E, :]
                cont22Easig = 0
                while cont22Easig < contAsig:
                    if(asignatura[cont22Easig] >= 'A' and asignatura[cont22Easig] <= 'z'):
                        exAsig22E.append(str(asignatura[cont22Easig]))
                    cont22Easig += 1
            elif(examenes22Ene[cont22E] == 'T'):
                asignatura = datosNoNaN.iloc[cont22E, :]
                cont22Easig = 0
                while cont22Easig < contAsig:
                    if(asignatura[cont22Easig] >= 'A' and asignatura[cont22Easig] <= 'z'):
                        exAsig22E.append(str(asignatura[cont22Easig]))
                    cont22Easig += 1
            cont22E += 1
        ################################
        cont23E = 0
        cont23Easig = 0
        exAsig23E = []

        while cont23E < contTope:
            if(examenes23Ene[cont23E] == 'M'):
                asignatura = datosNoNaN.iloc[cont23E, :]
                cont23Easig = 0
                while cont23Easig < contAsig:
                    if(asignatura[cont23Easig] >= 'A' and asignatura[cont23Easig] <= 'z'):
                        exAsig23E.append(str(asignatura[cont23Easig]))
                    cont23Easig += 1
            elif(examenes23Ene[cont23E] == 'T'):
                asignatura = datosNoNaN.iloc[cont23E, :]
                cont23Easig = 0
                while cont23Easig < contAsig:
                    if(asignatura[cont23Easig] >= 'A' and asignatura[cont23Easig] <= 'z'):
                        exAsig23E.append(str(asignatura[cont23Easig]))
                    cont23Easig += 1
            cont23E += 1
        ################################
        # Comprobación del contenido
        cont = 0
        resultado = []
        encontrado  = False

        while(cont < len(exAsig10E) and (encontrado == False)):
            if(exAsig10E[cont] == asignaturaEX):
                resultado.append("10 de Enero")
                resultado.append(exAsig10E[cont])
                resultado.append(exAsig10E[cont+1])
                resultado.append(exAsig10E[cont+2])
                encontrado = True
            cont += 1
        
        cont = 0
        while(cont < len(exAsig11E) and (encontrado == False)):
            if(exAsig11E[cont] == asignaturaEX):
                resultado.append("11 de Enero")
                resultado.append(exAsig11E[cont])
                resultado.append(exAsig11E[cont+1])
                resultado.append(exAsig11E[cont+2])
                encontrado = True
            cont += 1

        cont = 0
        while(cont < len(exAsig14E) and (encontrado == False)):
            if(exAsig14E[cont] == asignaturaEX):
                resultado.append("14 de Enero")
                resultado.append(exAsig14E[cont])
                resultado.append(exAsig14E[cont+1])
                resultado.append(exAsig14E[cont+2])
                encontrado = True
            cont += 1

        cont = 0
        while(cont < len(exAsig15E) and (encontrado == False)):
            if(exAsig15E[cont] == asignaturaEX):
                resultado.append("15 de Enero")
                resultado.append(exAsig15E[cont])
                resultado.append(exAsig15E[cont+1])
                resultado.append(exAsig15E[cont+2])
                encontrado = True
            cont += 1

        cont = 0
        while(cont < len(exAsig16E) and (encontrado == False)):
            if(exAsig16E[cont] == asignaturaEX):
                resultado.append("16 de Enero")
                resultado.append(exAsig16E[cont])
                resultado.append(exAsig16E[cont+1])
                resultado.append(exAsig16E[cont+2])
                encontrado = True
            cont += 1
    
        cont = 0
        while(cont < len(exAsig17E) and (encontrado == False)):
            if(exAsig17E[cont] == asignaturaEX):
                resultado.append("17 de Enero")
                resultado.append(exAsig17E[cont])
                resultado.append(exAsig17E[cont+1])
                resultado.append(exAsig17E[cont+2])
                encontrado = True
            cont += 1

        cont = 0
        while(cont < len(exAsig18E) and (encontrado == False)):
            if(exAsig18E[cont] == asignaturaEX):
                resultado.append("18 de Enero")
                resultado.append(exAsig18E[cont])
                resultado.append(exAsig18E[cont+1])
                resultado.append(exAsig18E[cont+2])
                encontrado = True
            cont += 1

        cont = 0
        while(cont < len(exAsig21E) and (encontrado == False)):
            if(exAsig21E[cont] == asignaturaEX):
                resultado.append("21 de Enero")
                resultado.append(exAsig21E[cont])
                resultado.append(exAsig21E[cont+1])
                resultado.append(exAsig21E[cont+2])
                encontrado = True
            cont += 1

        cont = 0
        while(cont < len(exAsig22E) and (encontrado == False)):
            if(exAsig22E[cont] == asignaturaEX):
                resultado.append("22 de Enero")
                resultado.append(exAsig22E[cont])
                resultado.append(exAsig22E[cont+1])
                resultado.append(exAsig22E[cont+2])
                encontrado = True
            cont += 1
        
        cont = 0
        while(cont < len(exAsig23E) and (encontrado == False)):
            if(exAsig23E[cont] == asignaturaEX):
                resultado.append("23 de Enero")
                resultado.append(exAsig23E[cont])
                resultado.append(exAsig23E[cont+1])
                resultado.append(exAsig23E[cont+2])
                encontrado = True
            cont += 1

        return resultado


def extractDataTable1_1SemExtraordinaria(asignaturaEX):
    tablas = camelot.read_pdf(os.path.join(RESOURCE, 'CalendarioExamenes18-19-GII.pdf'), pages='3')
    tablas.export(os.path.join(OUTPUT, 'CalendarioExamenes18-19-GII.csv'), f='csv', compress=False)

    with open(os.path.join(OUTPUT, 'CalendarioExamenes18-19-GII-page-3-table-1.csv'), 'r') as archivo:
        datos = pd.read_csv(archivo, header=-1)
        datosNoNaN = datos.fillna(value='0')

        examenes31Ene = datosNoNaN.iloc[:,6]
        examenes1Feb = datosNoNaN.iloc[:,7]
        examenes4Feb = datosNoNaN.iloc[:,9]
        examenes5Feb = datosNoNaN.iloc[:,10]
        examenes6Feb = datosNoNaN.iloc[:,11]
        examenes7Feb = datosNoNaN.iloc[:,12]
        examenes8Feb = datosNoNaN.iloc[:,13]
        examenes11Feb = datosNoNaN.iloc[:,15]
        examenes12Feb = datosNoNaN.iloc[:,16]
        examenes13Feb = datosNoNaN.iloc[:,17]

        # print(examenes10Ene.value_counts())
        # print(examenes10Ene.count())
        # print(examenes31Ene)
        # print(datosNoNaN.iloc[3,:])

        contTope = examenes31Ene.count()
        contAsig = datosNoNaN.iloc[3,:].count()
        cont31E = 0
        cont31Easig = 0
        exAsig31E = []

        while cont31E < contTope:
            if(examenes31Ene[cont31E]=='M'):
                asignatura = datosNoNaN.iloc[cont31E,:]
                cont31Easig = 0
                while cont31Easig < contAsig:
                    if(asignatura[cont31Easig] >= 'A' and asignatura[cont31Easig] <= 'z'):
                        exAsig31E.append(str(asignatura[cont31Easig]))
                    cont31Easig+=1
            elif(examenes31Ene[cont31E]=='T'):
                asignatura = datosNoNaN.iloc[cont31E,:]
                cont31Easig = 0
                while cont31Easig < contAsig:
                    if(asignatura[cont31Easig] >= 'A' and asignatura[cont31Easig] <= 'z'):
                        exAsig31E.append(str(asignatura[cont31Easig]))
                    cont31Easig+=1
            cont31E+=1
        # ################################
        cont1F = 0
        cont1Fasig = 0
        exAsig1F = []

        while cont1F < contTope:
            if(examenes1Feb[cont1F]=='M'):
                asignatura = datosNoNaN.iloc[cont1F,:]
                cont1Fasig = 0
                while cont1Fasig < contAsig:
                    if(asignatura[cont1Fasig] >= 'A' and asignatura[cont1Fasig] <= 'z'):
                        exAsig1F.append(str(asignatura[cont1Fasig]))
                    cont1Fasig+=1
            elif(examenes1Feb[cont1F]=='T'):
                asignatura = datosNoNaN.iloc[cont1F,:]
                cont1Fasig = 0
                while cont1Fasig < contAsig:
                    if(asignatura[cont1Fasig] >= 'A' and asignatura[cont1Fasig] <= 'z'):
                        exAsig1F.append(str(asignatura[cont1Fasig]))
                    cont1Fasig+=1
            cont1F+=1
        ################################
        cont4F = 0
        cont4Fasig = 0
        exAsig4F = []

        while cont4F < contTope:
            if(examenes4Feb[cont4F]=='M'):
                asignatura = datosNoNaN.iloc[cont4F,:]
                cont4Fasig = 0
                while cont4Fasig < contAsig:
                    if(asignatura[cont4Fasig] >= 'A' and asignatura[cont4Fasig] <= 'z'):
                        exAsig4F.append(str(asignatura[cont4Fasig]))
                    cont4Fasig+=1
            elif(examenes4Feb[cont4F]=='T'):
                asignatura = datosNoNaN.iloc[cont4F,:]
                cont4Fasig = 0
                while cont4Fasig < contAsig:
                    if(asignatura[cont4Fasig] >= 'A' and asignatura[cont4Fasig] <= 'z'):
                        exAsig4F.append(str(asignatura[cont4Fasig]))
                    cont4Fasig+=1
            cont4F+=1
        ################################
        cont5F = 0
        cont5Fasig = 0
        exAsig5F = []

        while cont5F < contTope:
            if(examenes5Feb[cont5F]=='M'):
                asignatura = datosNoNaN.iloc[cont5F,:]
                cont5Fasig = 0
                while cont5Fasig < contAsig:
                    if(asignatura[cont5Fasig] >= 'A' and asignatura[cont5Fasig] <= 'z'):
                        exAsig5F.append(str(asignatura[cont5Fasig]))
                    cont5Fasig+=1
            elif(examenes5Feb[cont5F]=='T'):
                asignatura = datosNoNaN.iloc[cont5F,:]
                cont5Fasig = 0
                while cont5Fasig < contAsig:
                    if(asignatura[cont5Fasig] >= 'A' and asignatura[cont5Fasig] <= 'z'):
                        exAsig5F.append(str(asignatura[cont5Fasig]))
                    cont5Fasig+=1
            cont5F+=1
        ################################
        cont6F = 0
        cont6Fasig = 0
        exAsig6F = []

        while cont6F < contTope:
            if(examenes6Feb[cont6F]=='M'):
                asignatura = datosNoNaN.iloc[cont6F,:]
                cont6Fasig = 0
                while cont6Fasig < contAsig:
                    if(asignatura[cont6Fasig] >= 'A' and asignatura[cont6Fasig] <= 'z'):
                        exAsig6F.append(str(asignatura[cont6Fasig]))
                    cont6Fasig+=1
            elif(examenes6Feb[cont6F]=='T'):
                asignatura = datosNoNaN.iloc[cont6F,:]
                cont6Fasig = 0
                while cont6Fasig < contAsig:
                    if(asignatura[cont6Fasig] >= 'A' and asignatura[cont6Fasig] <= 'z'):
                        exAsig6F.append(str(asignatura[cont6Fasig]))
                    cont6Fasig+=1
            cont6F+=1
        ################################
        cont7F = 0
        cont7Fasig = 0
        exAsig7F = []

        while cont7F < contTope:
            if(examenes7Feb[cont7F]=='M'):
                asignatura = datosNoNaN.iloc[cont7F,:]
                cont7Fasig = 0
                while cont7Fasig < contAsig:
                    if(asignatura[cont7Fasig] >= 'A' and asignatura[cont7Fasig] <= 'z'):
                        exAsig7F.append(str(asignatura[cont7Fasig]))
                    cont7Fasig+=1
            elif(examenes7Feb[cont7F]=='T'):
                asignatura = datosNoNaN.iloc[cont7F,:]
                cont7Fasig = 0
                while cont7Fasig < contAsig:
                    if(asignatura[cont7Fasig] >= 'A' and asignatura[cont7Fasig] <= 'z'):
                        exAsig7F.append(str(asignatura[cont7Fasig]))
                    cont7Fasig+=1
            cont7F+=1
        ################################
        cont8F = 0
        cont8Fasig = 0
        exAsig8F = []

        while cont8F < contTope:
            if(examenes8Feb[cont8F]=='M'):
                asignatura = datosNoNaN.iloc[cont8F,:]
                cont8Fasig = 0
                while cont8Fasig < contAsig:
                    if(asignatura[cont8Fasig] >= 'A' and asignatura[cont8Fasig] <= 'z'):
                        exAsig8F.append(str(asignatura[cont8Fasig]))
                    cont8Fasig+=1
            elif(examenes8Feb[cont8F]=='T'):
                asignatura = datosNoNaN.iloc[cont8F,:]
                cont8Fasig = 0
                while cont8Fasig < contAsig:
                    if(asignatura[cont8Fasig] >= 'A' and asignatura[cont8Fasig] <= 'z'):
                        exAsig8F.append(str(asignatura[cont8Fasig]))
                    cont8Fasig+=1
            cont8F+=1
        ################################
        cont11F = 0
        cont11Fasig = 0
        exAsig11F = []

        while cont11F < contTope:
            if(examenes11Feb[cont11F]=='M'):
                asignatura = datosNoNaN.iloc[cont11F,:]
                cont11Fasig = 0
                while cont11Fasig < contAsig:
                    if(asignatura[cont11Fasig] >= 'A' and asignatura[cont11Fasig] <= 'z'):
                        exAsig11F.append(str(asignatura[cont11Fasig]))
                    cont11Fasig+=1
            elif(examenes11Feb[cont11F]=='T'):
                asignatura = datosNoNaN.iloc[cont11F,:]
                cont11Fasig = 0
                while cont11Fasig < contAsig:
                    if(asignatura[cont11Fasig] >= 'A' and asignatura[cont11Fasig] <= 'z'):
                        exAsig11F.append(str(asignatura[cont11Fasig]))
                    cont11Fasig+=1
            cont11F+=1
        ################################
        cont12F = 0
        cont12Fasig = 0
        exAsig12F = []

        while cont12F < contTope:
            if(examenes12Feb[cont12F]=='M'):
                asignatura = datosNoNaN.iloc[cont12F,:]
                cont12Fasig = 0
                while cont12Fasig < contAsig:
                    if(asignatura[cont12Fasig] >= 'A' and asignatura[cont12Fasig] <= 'É'):
                        exAsig12F.append(str(asignatura[cont12Fasig]))
                    cont12Fasig+=1
            elif(examenes12Feb[cont12F]=='T'):
                asignatura = datosNoNaN.iloc[cont12F,:]
                cont12Fasig = 0
                while cont12Fasig < contAsig:
                    if(asignatura[cont12Fasig] >= 'A' and asignatura[cont12Fasig] <= 'z'):
                        exAsig12F.append(str(asignatura[cont12Fasig]))
                    cont12Fasig+=1
            cont12F+=1
        ################################
        cont13F = 0
        cont13Fasig = 0
        exAsig13F = []

        while cont13F < contTope:
            if(examenes13Feb[cont13F]=='M'):
                asignatura = datosNoNaN.iloc[cont13F,:]
                cont13Fasig = 0
                while cont13Fasig < contAsig:
                    if(asignatura[cont13Fasig] >= 'A' and asignatura[cont13Fasig] <= 'z'):
                        exAsig13F.append(str(asignatura[cont13Fasig]))
                    cont13Fasig+=1
            elif(examenes13Feb[cont13F]=='T'):
                asignatura = datosNoNaN.iloc[cont13F,:]
                cont13Fasig = 0
                while cont13Fasig < contAsig:
                    if(asignatura[cont13Fasig] >= 'A' and asignatura[cont13Fasig] <= 'z'):
                        exAsig13F.append(str(asignatura[cont13Fasig]))
                    cont13Fasig+=1
            cont13F+=1
        ################################
        #Comprobación del contenido
        cont = 0
        resultado = []
        encontrado  = False

        while(cont < len(exAsig31E) and (encontrado == False)):
            if(exAsig31E[cont] == asignaturaEX):
                resultado.append("31 de Enero")
                resultado.append(exAsig31E[cont])
                resultado.append(exAsig31E[cont+1])
                resultado.append(exAsig31E[cont+2])
                encontrado = True
            cont += 1
        
        cont = 0
        while(cont < len(exAsig1F) and (encontrado == False)):
            if(exAsig1F[cont] == asignaturaEX):
                resultado.append("1 de Febrero")
                resultado.append(exAsig1F[cont])
                resultado.append(exAsig1F[cont+1])
                resultado.append(exAsig1F[cont+2])
                encontrado = True
            cont += 1

        cont = 0
        while(cont < len(exAsig4F) and (encontrado == False)):
            if(exAsig4F[cont] == asignaturaEX):
                resultado.append("4 de Febrero")
                resultado.append(exAsig4F[cont])
                resultado.append(exAsig4F[cont+1])
                resultado.append(exAsig4F[cont+2])
                encontrado = True
            cont += 1

        cont = 0
        while(cont < len(exAsig5F) and (encontrado == False)):
            if(exAsig5F[cont] == asignaturaEX):
                resultado.append("5 de Febrero")
                resultado.append(exAsig5F[cont])
                resultado.append(exAsig5F[cont+1])
                resultado.append(exAsig5F[cont+2])
                encontrado = True
            cont += 1

        cont = 0
        while(cont < len(exAsig6F) and (encontrado == False)):
            if(exAsig6F[cont] == asignaturaEX):
                resultado.append("6 de Febrero")
                resultado.append(exAsig6F[cont])
                resultado.append(exAsig6F[cont+1])
                resultado.append(exAsig6F[cont+2])
                encontrado = True
            cont += 1

        cont = 0
        while(cont < len(exAsig7F) and (encontrado == False)):
            if(exAsig7F[cont] == asignaturaEX):
                resultado.append("7 de Febrero")
                resultado.append(exAsig7F[cont])
                resultado.append(exAsig7F[cont+1])
                resultado.append(exAsig7F[cont+2])
                encontrado = True
            cont += 1

        cont = 0
        while(cont < len(exAsig8F) and (encontrado == False)):
            if(exAsig8F[cont] == asignaturaEX):
                resultado.append("8 de Febrero")
                resultado.append(exAsig8F[cont])
                resultado.append(exAsig8F[cont+1])
                resultado.append(exAsig8F[cont+2])
                encontrado = True
            cont += 1
    
        cont = 0
        while(cont < len(exAsig11F) and (encontrado == False)):
            if(exAsig11F[cont] == asignaturaEX):
                resultado.append("11 de Febrero")
                resultado.append(exAsig11F[cont])
                resultado.append(exAsig11F[cont+1])
                resultado.append(exAsig11F[cont+2])
                encontrado = True
            cont += 1

        cont = 0
        while(cont < len(exAsig12F) and (encontrado == False)):
            if(exAsig12F[cont] == asignaturaEX):
                resultado.append("12 de Febrero")
                resultado.append(exAsig12F[cont])
                resultado.append(exAsig12F[cont+1])
                resultado.append(exAsig12F[cont+2])
                encontrado = True
            cont += 1

        cont = 0
        while(cont < len(exAsig13F) and (encontrado == False)):
            if(exAsig13F[cont] == asignaturaEX):
                resultado.append("13 de Febrero")
                resultado.append(exAsig13F[cont])
                resultado.append(exAsig13F[cont+1])
                resultado.append(exAsig13F[cont+2])
                encontrado = True
            cont += 1

        return resultado


def extractDataTable2_1SemExtraordinaria(asignaturaEX):
    tablas = camelot.read_pdf(os.path.join(RESOURCE, 'CalendarioExamenes18-19-GII.pdf'), pages='4')
    tablas.export(os.path.join(OUTPUT, 'CalendarioExamenes18-19-GII.csv'), f='csv', compress=False)

    with open(os.path.join(OUTPUT, 'CalendarioExamenes18-19-GII-page-4-table-1.csv'), 'r') as archivo:
        datos = pd.read_csv(archivo, header=-1)
        datosNoNaN = datos.fillna(value='0')

        examenes31Ene = datosNoNaN.iloc[:,6]
        examenes1Feb = datosNoNaN.iloc[:,7]
        examenes4Feb = datosNoNaN.iloc[:,9]
        examenes5Feb = datosNoNaN.iloc[:,10]
        examenes6Feb = datosNoNaN.iloc[:,11]
        examenes7Feb = datosNoNaN.iloc[:,12]
        examenes8Feb = datosNoNaN.iloc[:,13]
        examenes11Feb = datosNoNaN.iloc[:,15]
        examenes12Feb = datosNoNaN.iloc[:,16]
        examenes13Feb = datosNoNaN.iloc[:,17]

        # print(examenes10Ene.value_counts())
        # print(examenes10Ene.count())
        # print(examenes10Ene)
        # print(datosNoNaN.iloc[3,:])

        contTope = examenes31Ene.count()
        contAsig = datosNoNaN.iloc[3,:].count()
        cont31E = 0
        cont31Easig = 0
        exAsig31E = []

        while cont31E < contTope:
            if(examenes31Ene[cont31E]=='M'):
                asignatura = datosNoNaN.iloc[cont31E,:]
                cont31Easig = 0
                while cont31Easig < contAsig:
                    if(asignatura[cont31Easig] >= 'A' and asignatura[cont31Easig] <= 'z'):
                        exAsig31E.append(str(asignatura[cont31Easig]))
                    cont31Easig+=1
            elif(examenes31Ene[cont31E]=='T'):
                asignatura = datosNoNaN.iloc[cont31E,:]
                cont31Easig = 0
                while cont31Easig < contAsig:
                    if(asignatura[cont31Easig] >= 'A' and asignatura[cont31Easig] <= 'z'):
                        exAsig31E.append(str(asignatura[cont31Easig]))
                    cont31Easig+=1
            cont31E+=1
        # ################################
        cont1F = 0
        cont1Fasig = 0
        exAsig1F = []

        while cont1F < contTope:
            if(examenes1Feb[cont1F]=='M'):
                asignatura = datosNoNaN.iloc[cont1F,:]
                cont1Fasig = 0
                while cont1Fasig < contAsig:
                    if(asignatura[cont1Fasig] >= 'A' and asignatura[cont1Fasig] <= 'z'):
                        exAsig1F.append(str(asignatura[cont1Fasig]))
                    cont1Fasig+=1
            elif(examenes1Feb[cont1F]=='T'):
                asignatura = datosNoNaN.iloc[cont1F,:]
                cont1Fasig = 0
                while cont1Fasig < contAsig:
                    if(asignatura[cont1Fasig] >= 'A' and asignatura[cont1Fasig] <= 'z'):
                        exAsig1F.append(str(asignatura[cont1Fasig]))
                    cont1Fasig+=1
            cont1F+=1
        ################################
        cont4F = 0
        cont4Fasig = 0
        exAsig4F = []

        while cont4F < contTope:
            if(examenes4Feb[cont4F]=='M'):
                asignatura = datosNoNaN.iloc[cont4F,:]
                cont4Fasig = 0
                while cont4Fasig < contAsig:
                    if(asignatura[cont4Fasig] >= 'A' and asignatura[cont4Fasig] <= 'z'):
                        exAsig4F.append(str(asignatura[cont4Fasig]))
                    cont4Fasig+=1
            elif(examenes4Feb[cont4F]=='T'):
                asignatura = datosNoNaN.iloc[cont4F,:]
                cont4Fasig = 0
                while cont4Fasig < contAsig:
                    if(asignatura[cont4Fasig] >= 'A' and asignatura[cont4Fasig] <= 'z'):
                        exAsig4F.append(str(asignatura[cont4Fasig]))
                    cont4Fasig+=1
            cont4F+=1

        ################################
        cont5F = 0
        cont5Fasig = 0
        exAsig5F = []

        while cont5F < contTope:
            if(examenes5Feb[cont5F]=='M'):
                asignatura = datosNoNaN.iloc[cont5F,:]
                cont5Fasig = 0
                while cont5Fasig < contAsig:
                    if(asignatura[cont5Fasig] >= 'A' and asignatura[cont5Fasig] <= 'z'):
                        exAsig5F.append(str(asignatura[cont5Fasig]))
                    cont5Fasig+=1
            elif(examenes5Feb[cont5F]=='T'):
                asignatura = datosNoNaN.iloc[cont5F,:]
                cont5Fasig = 0
                while cont5Fasig < contAsig:
                    if(asignatura[cont5Fasig] >= 'A' and asignatura[cont5Fasig] <= 'z'):
                        exAsig5F.append(str(asignatura[cont5Fasig]))
                    cont5Fasig+=1
            cont5F+=1
        ################################
        cont6F = 0
        cont6Fasig = 0
        exAsig6F = []

        while cont6F < contTope:
            if(examenes6Feb[cont6F]=='M'):
                asignatura = datosNoNaN.iloc[cont6F,:]
                cont6Fasig = 0
                while cont6Fasig < contAsig:
                    if(asignatura[cont6Fasig] >= 'A' and asignatura[cont6Fasig] <= 'z'):
                        exAsig6F.append(str(asignatura[cont6Fasig]))
                    cont6Fasig+=1
            elif(examenes6Feb[cont6F]=='T'):
                asignatura = datosNoNaN.iloc[cont6F,:]
                cont6Fasig = 0
                while cont6Fasig < contAsig:
                    if(asignatura[cont6Fasig] >= 'A' and asignatura[cont6Fasig] <= 'z'):
                        exAsig6F.append(str(asignatura[cont6Fasig]))
                    cont6Fasig+=1
            cont6F+=1
        ################################
        cont7F = 0
        cont7Fasig = 0
        exAsig7F = []

        while cont7F < contTope:
            if(examenes7Feb[cont7F]=='M'):
                asignatura = datosNoNaN.iloc[cont7F,:]
                cont7Fasig = 0
                while cont7Fasig < contAsig:
                    if(asignatura[cont7Fasig] >= 'A' and asignatura[cont7Fasig] <= 'z'):
                        exAsig7F.append(str(asignatura[cont7Fasig]))
                    cont7Fasig+=1
            elif(examenes7Feb[cont7F]=='T'):
                asignatura = datosNoNaN.iloc[cont7F,:]
                cont7Fasig = 0
                while cont7Fasig < contAsig:
                    if(asignatura[cont7Fasig] >= 'A' and asignatura[cont7Fasig] <= 'z'):
                        exAsig7F.append(str(asignatura[cont7Fasig]))
                    cont7Fasig+=1
            cont7F+=1
        ################################
        cont8F = 0
        cont8Fasig = 0
        exAsig8F = []

        while cont8F < contTope:
            if(examenes8Feb[cont8F]=='M'):
                asignatura = datosNoNaN.iloc[cont8F,:]
                cont8Fasig = 0
                while cont8Fasig < contAsig:
                    if(asignatura[cont8Fasig] >= 'A' and asignatura[cont8Fasig] <= 'z'):
                        exAsig8F.append(str(asignatura[cont8Fasig]))
                    cont8Fasig+=1
            elif(examenes8Feb[cont8F]=='T'):
                asignatura = datosNoNaN.iloc[cont8F,:]
                cont8Fasig = 0
                while cont8Fasig < contAsig:
                    if(asignatura[cont8Fasig] >= 'A' and asignatura[cont8Fasig] <= 'z'):
                        exAsig8F.append(str(asignatura[cont8Fasig]))
                    cont8Fasig+=1
            cont8F+=1
        ################################
        cont11F = 0
        cont11Fasig = 0
        exAsig11F = []

        while cont11F < contTope:
            if(examenes11Feb[cont11F]=='M'):
                asignatura = datosNoNaN.iloc[cont11F,:]
                cont11Fasig = 0
                while cont11Fasig < contAsig:
                    if(asignatura[cont11Fasig] >= 'A' and asignatura[cont11Fasig] <= 'z'):
                        exAsig11F.append(str(asignatura[cont11Fasig]))
                    cont11Fasig+=1
            elif(examenes11Feb[cont11F]=='T'):
                asignatura = datosNoNaN.iloc[cont11F,:]
                cont11Fasig = 0
                while cont11Fasig < contAsig:
                    if(asignatura[cont11Fasig] >= 'A' and asignatura[cont11Fasig] <= 'z'):
                        if(asignatura[cont11Fasig] != 'Int' and asignatura[cont11Fasig] != 'Tit'
                            and asignatura[cont11Fasig] != 'Cur' and asignatura[cont11Fasig] != 'Cuat'
                                and asignatura[cont11Fasig] != 'Acr'):
                            exAsig11F.append(str(asignatura[cont11Fasig]))
                    cont11Fasig+=1
            cont11F+=1
        ################################
        cont12F = 0
        cont12Fasig = 0
        exAsig12F = []

        while cont12F < contTope:
            if(examenes12Feb[cont12F]=='M'):
                asignatura = datosNoNaN.iloc[cont12F,:]
                cont12Fasig = 0
                while cont12Fasig < contAsig:
                    if(asignatura[cont12Fasig] >= 'A' and asignatura[cont12Fasig] <= 'É'):
                        exAsig12F.append(str(asignatura[cont12Fasig]))
                    cont12Fasig+=1
            elif(examenes12Feb[cont12F]=='T'):
                asignatura = datosNoNaN.iloc[cont12F,:]
                cont12Fasig = 0
                while cont12Fasig < contAsig:
                    if(asignatura[cont12Fasig] >= 'A' and asignatura[cont12Fasig] <= 'z'):
                        exAsig12F.append(str(asignatura[cont12Fasig]))
                    cont12Fasig+=1
            cont12F+=1
        ################################
        cont13F = 0
        cont13Fasig = 0
        exAsig13F = []

        while cont13F < contTope:
            if(examenes13Feb[cont13F]=='M'):
                asignatura = datosNoNaN.iloc[cont13F,:]
                cont13Fasig = 0
                while cont13Fasig < contAsig:
                    if(asignatura[cont13Fasig] >= 'A' and asignatura[cont13Fasig] <= 'z'):
                        exAsig13F.append(str(asignatura[cont13Fasig]))
                    cont13Fasig+=1
            elif(examenes13Feb[cont13F]=='T'):
                asignatura = datosNoNaN.iloc[cont13F,:]
                cont13Fasig = 0
                while cont13Fasig < contAsig:
                    if(asignatura[cont13Fasig] >= 'A' and asignatura[cont13Fasig] <= 'z'):
                        exAsig13F.append(str(asignatura[cont13Fasig]))
                    cont13Fasig+=1
            cont13F+=1
        ################################
        #Comprobación del contenido
        cont = 0
        resultado = []
        encontrado  = False

        while(cont < len(exAsig31E) and (encontrado == False)):
            if(exAsig31E[cont] == asignaturaEX):
                resultado.append("31 de Enero")
                resultado.append(exAsig31E[cont])
                resultado.append(exAsig31E[cont+1])
                resultado.append(exAsig31E[cont+2])
                encontrado = True
            cont += 1
        
        cont = 0
        while(cont < len(exAsig1F) and (encontrado == False)):
            if(exAsig1F[cont] == asignaturaEX):
                resultado.append("1 de Febrero")
                resultado.append(exAsig1F[cont])
                resultado.append(exAsig1F[cont+1])
                resultado.append(exAsig1F[cont+2])
                encontrado = True
            cont += 1

        cont = 0
        while(cont < len(exAsig4F) and (encontrado == False)):
            if(exAsig4F[cont] == asignaturaEX):
                resultado.append("4 de Febrero")
                resultado.append(exAsig4F[cont])
                resultado.append(exAsig4F[cont+1])
                resultado.append(exAsig4F[cont+2])
                encontrado = True
            cont += 1

        cont = 0
        while(cont < len(exAsig5F) and (encontrado == False)):
            if(exAsig5F[cont] == asignaturaEX):
                resultado.append("5 de Febrero")
                resultado.append(exAsig5F[cont])
                resultado.append(exAsig5F[cont+1])
                resultado.append(exAsig5F[cont+2])
                encontrado = True
            cont += 1

        cont = 0
        while(cont < len(exAsig6F) and (encontrado == False)):
            if(exAsig6F[cont] == asignaturaEX):
                resultado.append("6 de Febrero")
                resultado.append(exAsig6F[cont])
                resultado.append(exAsig6F[cont+1])
                resultado.append(exAsig6F[cont+2])
                encontrado = True
            cont += 1

        cont = 0
        while(cont < len(exAsig7F) and (encontrado == False)):
            if(exAsig7F[cont] == asignaturaEX):
                resultado.append("7 de Febrero")
                resultado.append(exAsig7F[cont])
                resultado.append(exAsig7F[cont+1])
                resultado.append(exAsig7F[cont+2])
                encontrado = True
            cont += 1

        cont = 0
        while(cont < len(exAsig8F) and (encontrado == False)):
            if(exAsig8F[cont] == asignaturaEX):
                resultado.append("8 de Febrero")
                resultado.append(exAsig8F[cont])
                resultado.append(exAsig8F[cont+1])
                resultado.append(exAsig8F[cont+2])
                encontrado = True
            cont += 1
    
        cont = 0
        while(cont < len(exAsig11F) and (encontrado == False)):
            if(exAsig11F[cont] == asignaturaEX):
                resultado.append("11 de Febrero")
                resultado.append(exAsig11F[cont])
                resultado.append(exAsig11F[cont+1])
                resultado.append(exAsig11F[cont+2])
                encontrado = True
            cont += 1

        cont = 0
        while(cont < len(exAsig12F) and (encontrado == False)):
            if(exAsig12F[cont] == asignaturaEX):
                resultado.append("12 de Febrero")
                resultado.append(exAsig12F[cont])
                resultado.append(exAsig12F[cont+1])
                resultado.append(exAsig12F[cont+2])
                encontrado = True
            cont += 1

        cont = 0
        while(cont < len(exAsig13F) and (encontrado == False)):
            if(exAsig13F[cont] == asignaturaEX):
                resultado.append("13 de Febrero")
                resultado.append(exAsig13F[cont])
                resultado.append(exAsig13F[cont+1])
                resultado.append(exAsig13F[cont+2])
                encontrado = True
            cont += 1

        return resultado


def extractDataTable1_2SemOrdinaria():
    tablas = camelot.read_pdf(os.path.join(
        RESOURCE, 'CalendarioExamenes18-19-GII.pdf'), pages='5')
    tablas.export(os.path.join(
        OUTPUT, 'CalendarioExamenes18-19-GII.csv'), f='csv', compress=False)

    with open(os.path.join(OUTPUT, 'CalendarioExamenes18-19-GII-page-5-table-1.csv'), 'r') as archivo:
        datos = pd.read_csv(archivo, header=-1)
        datosNoNaN = datos.fillna(value='0')

        examenes5Jun = datosNoNaN.iloc[:, 6]
        examenes6Jun = datosNoNaN.iloc[:, 7]
        examenes7Jun = datosNoNaN.iloc[:, 8]
        examenes10Jun = datosNoNaN.iloc[:, 10]
        examenes11Jun = datosNoNaN.iloc[:, 11]
        examenes12Jun = datosNoNaN.iloc[:, 12]
        examenes13Jun = datosNoNaN.iloc[:, 13]
        examenes14Jun = datosNoNaN.iloc[:, 14]
        examenes17Jun = datosNoNaN.iloc[:, 16]
        examenes18Jun = datosNoNaN.iloc[:, 17]
        examenes19Jun = datosNoNaN.iloc[:, 18]

        # print(examenes10Ene.value_counts())
        # print(examenes22Ene.count())
        # print(examenes19Jun)

        contTope = examenes5Jun.count()
        contAsig = datosNoNaN.iloc[3, :].count()
        cont5J = 0
        cont5Jasig = 0
        exAsig5J = []
        asignatura = []

        while cont5J < contTope:
            if(examenes5Jun[cont5J] == 'M'):
                asignatura = datosNoNaN.iloc[cont5J, :]
                while cont5Jasig < contAsig:
                    if(asignatura[cont5Jasig] >= 'A' and asignatura[cont5Jasig] <= 'z'):
                        exAsig5J.append(str(asignatura[cont5Jasig]))
                    cont5Jasig += 1
            elif(examenes5Jun[cont5J] == 'T'):
                asignatura = datosNoNaN.iloc[cont5J, :]
                cont5Jasig = 0
                while cont5Jasig < contAsig:
                    if(asignatura[cont5Jasig] >= 'A' and asignatura[cont5Jasig] <= 'z'):
                        exAsig5J.append(str(asignatura[cont5Jasig]))
                    cont5Jasig += 1
            cont5J += 1
        ################################
        cont6J = 0
        cont6Jasig = 0
        exAsig6J = []

        while cont6J < contTope:
            if(examenes6Jun[cont6J] == 'M'):
                asignatura = datosNoNaN.iloc[cont6J, :]
                cont6Jasig = 0
                while cont6Jasig < contAsig:
                    if(asignatura[cont6Jasig] >= 'A' and asignatura[cont6Jasig] <= 'z'):
                        exAsig6J.append(str(asignatura[cont6Jasig]))
                    cont6Jasig += 1
            elif(examenes6Jun[cont6J] == 'T'):
                asignatura = datosNoNaN.iloc[cont6J, :]
                cont6Jasig = 0
                while cont6Jasig < contAsig:
                    if(asignatura[cont6Jasig] >= 'A' and asignatura[cont6Jasig] <= 'z'):
                        exAsig6J.append(str(asignatura[cont6Jasig]))
                    cont6Jasig += 1
            cont6J += 1
        # ################################
        cont7J = 0
        cont7Jasig = 0
        exAsig7J = []

        while cont7J < contTope:
            if(examenes7Jun[cont7J] == 'M'):
                asignatura = datosNoNaN.iloc[cont7J, :]
                cont7Jasig = 0
                while cont7Jasig < contAsig:
                    if(asignatura[cont7Jasig] >= 'A' and asignatura[cont7Jasig] <= 'z'):
                        exAsig7J.append(str(asignatura[cont7Jasig]))
                    cont7Jasig += 1
            elif(examenes7Jun[cont7J] == 'T'):
                asignatura = datosNoNaN.iloc[cont7J, :]
                cont7Jasig = 0
                while cont7Jasig < contAsig:
                    if(asignatura[cont7Jasig] >= 'A' and asignatura[cont7Jasig] <= 'z'):
                        exAsig7J.append(str(asignatura[cont7Jasig]))
                    cont7Jasig += 1
            cont7J += 1
        # ################################
        cont10J = 0
        cont10Jasig = 0
        exAsig10J = []

        while cont10J < contTope:
            if(examenes10Jun[cont10J] == 'M'):
                asignatura = datosNoNaN.iloc[cont10J, :]
                cont10Jasig = 0
                while cont10Jasig < contAsig:
                    if(asignatura[cont10Jasig] >= 'A' and asignatura[cont10Jasig] <= 'z'):
                        exAsig10J.append(str(asignatura[cont10Jasig]))
                    cont10Jasig += 1
            elif(examenes10Jun[cont10J] == 'T'):
                asignatura = datosNoNaN.iloc[cont10J, :]
                cont10Jasig = 0
                while cont10Jasig < contAsig:
                    if(asignatura[cont10Jasig] >= 'A' and asignatura[cont10Jasig] <= 'z'):
                        exAsig10J.append(str(asignatura[cont10Jasig]))
                    cont10Jasig += 1
            cont10J += 1
        # ################################
        cont11J = 0
        cont11Jasig = 0
        exAsig11J = []

        while cont11J < contTope:
            if(examenes11Jun[cont11J] == 'M'):
                asignatura = datosNoNaN.iloc[cont11J, :]
                cont11Jasig = 0
                while cont11Jasig < contAsig:
                    if(asignatura[cont11Jasig] >= 'A' and asignatura[cont11Jasig] <= 'z'):
                        exAsig11J.append(str(asignatura[cont11Jasig]))
                    cont11Jasig += 1
            elif(examenes11Jun[cont11J] == 'T'):
                asignatura = datosNoNaN.iloc[cont11J, :]
                cont11Jasig = 0
                while cont11Jasig < contAsig:
                    if(asignatura[cont11Jasig] >= 'A' and asignatura[cont11Jasig] <= 'z'):
                        exAsig11J.append(str(asignatura[cont11Jasig]))
                    cont11Jasig += 1
            cont11J += 1
        # ################################
        cont12J = 0
        cont12Jasig = 0
        exAsig12J = []

        while cont12J < contTope:
            if(examenes12Jun[cont12J] == 'M'):
                asignatura = datosNoNaN.iloc[cont12J, :]
                cont12Jasig = 0
                while cont12Jasig < contAsig:
                    if(asignatura[cont12Jasig] >= 'A' and asignatura[cont12Jasig] <= 'z'):
                        exAsig12J.append(str(asignatura[cont12Jasig]))
                    cont12Jasig += 1
            elif(examenes12Jun[cont12J] == 'T'):
                asignatura = datosNoNaN.iloc[cont12J, :]
                cont12Jasig = 0
                while cont12Jasig < contAsig:
                    if(asignatura[cont12Jasig] >= 'A' and asignatura[cont12Jasig] <= 'z'):
                        exAsig12J.append(str(asignatura[cont12Jasig]))
                    cont12Jasig += 1
            cont12J += 1
        ################################
        cont13J = 0
        cont13Jasig = 0
        exAsig13J = []

        while cont13J < contTope:
            if(examenes13Jun[cont13J] == 'M'):
                asignatura = datosNoNaN.iloc[cont13J, :]
                cont13Jasig = 0
                while cont13Jasig < contAsig:
                    if(asignatura[cont13Jasig] >= 'A' and asignatura[cont13Jasig] <= 'z'):
                        exAsig13J.append(str(asignatura[cont13Jasig]))
                    cont13Jasig += 1
            elif(examenes13Jun[cont13J] == 'T'):
                asignatura = datosNoNaN.iloc[cont13J, :]
                cont13Jasig = 0
                while cont13Jasig < contAsig:
                    if(asignatura[cont13Jasig] >= 'A' and asignatura[cont13Jasig] <= 'z'):
                        exAsig13J.append(str(asignatura[cont13Jasig]))
                    cont13Jasig += 1
            cont13J += 1
        ################################
        cont14J = 0
        cont14Jasig = 0
        exAsig14J = []

        while cont14J < contTope:
            if(examenes14Jun[cont14J] == 'M'):
                asignatura = datosNoNaN.iloc[cont14J, :]
                cont14Jasig = 0
                while cont14Jasig < contAsig:
                    if(asignatura[cont14Jasig] >= 'A' and asignatura[cont14Jasig] <= 'z'):
                        exAsig14J.append(str(asignatura[cont14Jasig]))
                    cont14Jasig += 1
            elif(examenes14Jun[cont14J] == 'T'):
                asignatura = datosNoNaN.iloc[cont14J, :]
                cont14Jasig = 0
                while cont14Jasig < contAsig:
                    if(asignatura[cont14Jasig] >= 'A' and asignatura[cont14Jasig] <= 'z'):
                        exAsig14J.append(str(asignatura[cont14Jasig]))
                    cont14Jasig += 1
            cont14J += 1
        ################################
        cont17J = 0
        cont17Jasig = 0
        exAsig17J = []

        while cont17J < contTope:
            if(examenes17Jun[cont17J] == 'M'):
                asignatura = datosNoNaN.iloc[cont17J, :]
                cont17Jasig = 0
                while cont17Jasig < contAsig:
                    if(asignatura[cont17Jasig] >= 'A' and asignatura[cont17Jasig] <= 'z'):
                        exAsig17J.append(str(asignatura[cont17Jasig]))
                    cont17Jasig += 1
            elif(examenes17Jun[cont17J] == 'T'):
                asignatura = datosNoNaN.iloc[cont17J, :]
                cont17Jasig = 0
                while cont17Jasig < contAsig:
                    if(asignatura[cont17Jasig] >= 'A' and asignatura[cont17Jasig] <= 'z'):
                        exAsig17J.append(str(asignatura[cont17Jasig]))
                    cont17Jasig += 1
            cont17J += 1
        ################################
        cont18J = 0
        cont18Jasig = 0
        exAsig18J = []

        while cont18J < contTope:
            if(examenes18Jun[cont18J] == 'M'):
                asignatura = datosNoNaN.iloc[cont18J, :]
                cont18Jasig = 0
                while cont18Jasig < contAsig:
                    if(asignatura[cont18Jasig] >= 'A' and asignatura[cont18Jasig] <= 'z'):
                        exAsig18J.append(str(asignatura[cont18Jasig]))
                    cont18Jasig += 1
            elif(examenes18Jun[cont18J] == 'T'):
                asignatura = datosNoNaN.iloc[cont18J, :]
                cont18Jasig = 0
                while cont18Jasig < contAsig:
                    if(asignatura[cont18Jasig] >= 'A' and asignatura[cont18Jasig] <= 'z'):
                        exAsig18J.append(str(asignatura[cont18Jasig]))
                    cont18Jasig += 1
            cont18J += 1
        ################################
        cont19J = 0
        cont19Jasig = 0
        exAsig19J = []

        while cont19J < contTope:
            if(examenes19Jun[cont19J] == 'M'):
                asignatura = datosNoNaN.iloc[cont19J, :]
                cont19Jasig = 0
                while cont19Jasig < contAsig:
                    if(asignatura[cont19Jasig] >= 'A' and asignatura[cont19Jasig] <= 'z'):
                        exAsig19J.append(str(asignatura[cont19Jasig]))
                    cont19Jasig += 1
            elif(examenes19Jun[cont19J] == 'T'):
                asignatura = datosNoNaN.iloc[cont19J, :]
                cont19Jasig = 0
                while cont19Jasig < contAsig:
                    if(asignatura[cont19Jasig] >= 'A' and asignatura[cont19Jasig] <= 'z'):
                        exAsig19J.append(str(asignatura[cont19Jasig]))
                    cont19Jasig += 1
            cont19J += 1
        ################################
        # Comprobación del contenido
        cont = 0
        print("------------------------------------")
        print("2do Semestre - Ordinaria")
        print("------------------------------------")
        while cont < len(exAsig19J):
            print(str(exAsig19J[cont]))
            cont += 1

        # for num in datosNoNaN:
        #     print (datosNoNaN[num:num+1])


def extractDataTable2_2SemOrdinaria():
    tablas = camelot.read_pdf(os.path.join(
        RESOURCE, 'CalendarioExamenes18-19-GII.pdf'), pages='6')
    tablas.export(os.path.join(
        OUTPUT, 'CalendarioExamenes18-19-GII.csv'), f='csv', compress=False)

    with open(os.path.join(OUTPUT, 'CalendarioExamenes18-19-GII-page-6-table-1.csv'), 'r') as archivo:
        datos = pd.read_csv(archivo, header=-1)
        datosNoNaN = datos.fillna(value='0')

        examenes5Jun = datosNoNaN.iloc[:, 6]
        examenes6Jun = datosNoNaN.iloc[:, 7]
        examenes7Jun = datosNoNaN.iloc[:, 8]
        examenes10Jun = datosNoNaN.iloc[:, 10]
        examenes11Jun = datosNoNaN.iloc[:, 11]
        examenes12Jun = datosNoNaN.iloc[:, 12]
        examenes13Jun = datosNoNaN.iloc[:, 13]
        examenes14Jun = datosNoNaN.iloc[:, 14]
        examenes17Jun = datosNoNaN.iloc[:, 16]
        examenes18Jun = datosNoNaN.iloc[:, 17]
        examenes19Jun = datosNoNaN.iloc[:, 18]

        # print(examenes10Ene.value_counts())
        # print(examenes22Ene.count())
        # print(examenes19Jun)

        contTope = examenes5Jun.count()
        contAsig = datosNoNaN.iloc[3, :].count()
        cont5J = 0
        cont5Jasig = 0
        exAsig5J = []
        asignatura = []

        while cont5J < contTope:
            if(examenes5Jun[cont5J] == 'M'):
                asignatura = datosNoNaN.iloc[cont5J, :]
                while cont5Jasig < contAsig:
                    if(asignatura[cont5Jasig] >= 'A' and asignatura[cont5Jasig] <= 'z'):
                        exAsig5J.append(str(asignatura[cont5Jasig]))
                    cont5Jasig += 1
            elif(examenes5Jun[cont5J] == 'T'):
                asignatura = datosNoNaN.iloc[cont5J, :]
                cont5Jasig = 0
                while cont5Jasig < contAsig:
                    if(asignatura[cont5Jasig] >= 'A' and asignatura[cont5Jasig] <= 'z'):
                        exAsig5J.append(str(asignatura[cont5Jasig]))
                    cont5Jasig += 1
            cont5J += 1
        ################################
        cont6J = 0
        cont6Jasig = 0
        exAsig6J = []

        while cont6J < contTope:
            if(examenes6Jun[cont6J] == 'M'):
                asignatura = datosNoNaN.iloc[cont6J, :]
                cont6Jasig = 0
                while cont6Jasig < contAsig:
                    if(asignatura[cont6Jasig] >= 'A' and asignatura[cont6Jasig] <= 'z'):
                        exAsig6J.append(str(asignatura[cont6Jasig]))
                    cont6Jasig += 1
            elif(examenes6Jun[cont6J] == 'T'):
                asignatura = datosNoNaN.iloc[cont6J, :]
                cont6Jasig = 0
                while cont6Jasig < contAsig:
                    if(asignatura[cont6Jasig] >= 'A' and asignatura[cont6Jasig] <= 'z'):
                        exAsig6J.append(str(asignatura[cont6Jasig]))
                    cont6Jasig += 1
            cont6J += 1
        # ################################
        cont7J = 0
        cont7Jasig = 0
        exAsig7J = []

        while cont7J < contTope:
            if(examenes7Jun[cont7J] == 'M'):
                asignatura = datosNoNaN.iloc[cont7J, :]
                cont7Jasig = 0
                while cont7Jasig < contAsig:
                    if(asignatura[cont7Jasig] >= 'A' and asignatura[cont7Jasig] <= 'z'):
                        exAsig7J.append(str(asignatura[cont7Jasig]))
                    cont7Jasig += 1
            elif(examenes7Jun[cont7J] == 'T'):
                asignatura = datosNoNaN.iloc[cont7J, :]
                cont7Jasig = 0
                while cont7Jasig < contAsig:
                    if(asignatura[cont7Jasig] >= 'A' and asignatura[cont7Jasig] <= 'z'):
                        exAsig7J.append(str(asignatura[cont7Jasig]))
                    cont7Jasig += 1
            cont7J += 1
        # ################################
        cont10J = 0
        cont10Jasig = 0
        exAsig10J = []

        while cont10J < contTope:
            if(examenes10Jun[cont10J] == 'M'):
                asignatura = datosNoNaN.iloc[cont10J, :]
                cont10Jasig = 0
                while cont10Jasig < contAsig:
                    if(asignatura[cont10Jasig] >= 'A' and asignatura[cont10Jasig] <= 'z'):
                        exAsig10J.append(str(asignatura[cont10Jasig]))
                    cont10Jasig += 1
            elif(examenes10Jun[cont10J] == 'T'):
                asignatura = datosNoNaN.iloc[cont10J, :]
                cont10Jasig = 0
                while cont10Jasig < contAsig:
                    if(asignatura[cont10Jasig] >= 'A' and asignatura[cont10Jasig] <= 'z'):
                        exAsig10J.append(str(asignatura[cont10Jasig]))
                    cont10Jasig += 1
            cont10J += 1
        # ################################
        cont11J = 0
        cont11Jasig = 0
        exAsig11J = []

        while cont11J < contTope:
            if(examenes11Jun[cont11J] == 'M'):
                asignatura = datosNoNaN.iloc[cont11J, :]
                cont11Jasig = 0
                while cont11Jasig < contAsig:
                    if(asignatura[cont11Jasig] >= 'A' and asignatura[cont11Jasig] <= 'z'):
                        exAsig11J.append(str(asignatura[cont11Jasig]))
                    cont11Jasig += 1
            elif(examenes11Jun[cont11J] == 'T'):
                asignatura = datosNoNaN.iloc[cont11J, :]
                cont11Jasig = 0
                while cont11Jasig < contAsig:
                    if(asignatura[cont11Jasig] >= 'A' and asignatura[cont11Jasig] <= 'z'):
                        exAsig11J.append(str(asignatura[cont11Jasig]))
                    cont11Jasig += 1
            cont11J += 1
        # ################################
        cont12J = 0
        cont12Jasig = 0
        exAsig12J = []

        while cont12J < contTope:
            if(examenes12Jun[cont12J] == 'M'):
                asignatura = datosNoNaN.iloc[cont12J, :]
                cont12Jasig = 0
                while cont12Jasig < contAsig:
                    if(asignatura[cont12Jasig] >= 'A' and asignatura[cont12Jasig] <= 'z'):
                        exAsig12J.append(str(asignatura[cont12Jasig]))
                    cont12Jasig += 1
            elif(examenes12Jun[cont12J] == 'T'):
                asignatura = datosNoNaN.iloc[cont12J, :]
                cont12Jasig = 0
                while cont12Jasig < contAsig:
                    if(asignatura[cont12Jasig] >= 'A' and asignatura[cont12Jasig] <= 'z'):
                        exAsig12J.append(str(asignatura[cont12Jasig]))
                    cont12Jasig += 1
            cont12J += 1
        ################################
        cont13J = 0
        cont13Jasig = 0
        exAsig13J = []

        while cont13J < contTope:
            if(examenes13Jun[cont13J] == 'M'):
                asignatura = datosNoNaN.iloc[cont13J, :]
                cont13Jasig = 0
                while cont13Jasig < contAsig:
                    if(asignatura[cont13Jasig] >= 'A' and asignatura[cont13Jasig] <= 'z'):
                        exAsig13J.append(str(asignatura[cont13Jasig]))
                    cont13Jasig += 1
            elif(examenes13Jun[cont13J] == 'T'):
                asignatura = datosNoNaN.iloc[cont13J, :]
                cont13Jasig = 0
                while cont13Jasig < contAsig:
                    if(asignatura[cont13Jasig] >= 'A' and asignatura[cont13Jasig] <= 'z'):
                        exAsig13J.append(str(asignatura[cont13Jasig]))
                    cont13Jasig += 1
            cont13J += 1
        ################################
        cont14J = 0
        cont14Jasig = 0
        exAsig14J = []

        while cont14J < contTope:
            if(examenes14Jun[cont14J] == 'M'):
                asignatura = datosNoNaN.iloc[cont14J, :]
                cont14Jasig = 0
                while cont14Jasig < contAsig:
                    if(asignatura[cont14Jasig] >= 'A' and asignatura[cont14Jasig] <= 'z'):
                        exAsig14J.append(str(asignatura[cont14Jasig]))
                    cont14Jasig += 1
            elif(examenes14Jun[cont14J] == 'T'):
                asignatura = datosNoNaN.iloc[cont14J, :]
                cont14Jasig = 0
                while cont14Jasig < contAsig:
                    if(asignatura[cont14Jasig] >= 'A' and asignatura[cont14Jasig] <= 'z'):
                        exAsig14J.append(str(asignatura[cont14Jasig]))
                    cont14Jasig += 1
            cont14J += 1
        ################################
        cont17J = 0
        cont17Jasig = 0
        exAsig17J = []

        while cont17J < contTope:
            if(examenes17Jun[cont17J] == 'M'):
                asignatura = datosNoNaN.iloc[cont17J, :]
                cont17Jasig = 0
                while cont17Jasig < contAsig:
                    if(asignatura[cont17Jasig] >= 'A' and asignatura[cont17Jasig] <= 'z'):
                        exAsig17J.append(str(asignatura[cont17Jasig]))
                    cont17Jasig += 1
            elif(examenes17Jun[cont17J] == 'T'):
                asignatura = datosNoNaN.iloc[cont17J, :]
                cont17Jasig = 0
                while cont17Jasig < contAsig:
                    if(asignatura[cont17Jasig] >= 'A' and asignatura[cont17Jasig] <= 'z'):
                        exAsig17J.append(str(asignatura[cont17Jasig]))
                    cont17Jasig += 1
            cont17J += 1
        ################################
        cont18J = 0
        cont18Jasig = 0
        exAsig18J = []

        while cont18J < contTope:
            if(examenes18Jun[cont18J] == 'M'):
                asignatura = datosNoNaN.iloc[cont18J, :]
                cont18Jasig = 0
                while cont18Jasig < contAsig:
                    if(asignatura[cont18Jasig] >= 'A' and asignatura[cont18Jasig] <= 'z'):
                        exAsig18J.append(str(asignatura[cont18Jasig]))
                    cont18Jasig += 1
            elif(examenes18Jun[cont18J] == 'T'):
                asignatura = datosNoNaN.iloc[cont18J, :]
                cont18Jasig = 0
                while cont18Jasig < contAsig:
                    if(asignatura[cont18Jasig] >= 'A' and asignatura[cont18Jasig] <= 'z'):
                        exAsig18J.append(str(asignatura[cont18Jasig]))
                    cont18Jasig += 1
            cont18J += 1
        ################################
        cont19J = 0
        cont19Jasig = 0
        exAsig19J = []

        while cont19J < contTope:
            if(examenes19Jun[cont19J] == 'M'):
                asignatura = datosNoNaN.iloc[cont19J, :]
                cont19Jasig = 0
                while cont19Jasig < contAsig:
                    if(asignatura[cont19Jasig] >= 'A' and asignatura[cont19Jasig] <= 'z'):
                        exAsig19J.append(str(asignatura[cont19Jasig]))
                    cont19Jasig += 1
            elif(examenes19Jun[cont19J] == 'T'):
                asignatura = datosNoNaN.iloc[cont19J, :]
                cont19Jasig = 0
                while cont19Jasig < contAsig:
                    if(asignatura[cont19Jasig] >= 'A' and asignatura[cont19Jasig] <= 'z'):
                        exAsig19J.append(str(asignatura[cont19Jasig]))
                    cont19Jasig += 1
            cont19J += 1
        ################################
        # Comprobación del contenido
        cont = 0
        print("------------------------------------")
        print("2do Semestre - Ordinaria cont")
        print("------------------------------------")
        while cont < len(exAsig19J):
            print(str(exAsig19J[cont]))
            cont += 1


def extractDataTable3_2SemOrdinaria():
    tablas = camelot.read_pdf(os.path.join(
        RESOURCE, 'CalendarioExamenes18-19-GII.pdf'), pages='7')
    tablas.export(os.path.join(
        OUTPUT, 'CalendarioExamenes18-19-GII.csv'), f='csv', compress=False)

    with open(os.path.join(OUTPUT, 'CalendarioExamenes18-19-GII-page-7-table-1.csv'), 'r') as archivo:
        datos = pd.read_csv(archivo, header=-1)
        datosNoNaN = datos.fillna(value='0')

        examenes5Jun = datosNoNaN.iloc[:, 1]
        examenes6Jun = datosNoNaN.iloc[:, 2]
        examenes7Jun = datosNoNaN.iloc[:, 3]
        examenes10Jun = datosNoNaN.iloc[:, 5]
        examenes11Jun = datosNoNaN.iloc[:, 6]
        examenes12Jun = datosNoNaN.iloc[:, 7]
        examenes13Jun = datosNoNaN.iloc[:, 8]
        examenes14Jun = datosNoNaN.iloc[:, 9]
        examenes17Jun = datosNoNaN.iloc[:, 11]
        examenes18Jun = datosNoNaN.iloc[:, 12]
        examenes19Jun = datosNoNaN.iloc[:, 13]

        # print(examenes18Jun.value_counts())
        # print(examenes22Ene.count())
        # print(examenes18Jun)

        contTope = examenes5Jun.count()
        contAsig = datosNoNaN.iloc[3, :].count()
        cont5J = 0
        cont5Jasig = 0
        exAsig5J = []
        asignatura = []

        while cont5J < contTope:
            if(examenes5Jun[cont5J] == 'M'):
                asignatura = datosNoNaN.iloc[cont5J, :]
                while cont5Jasig < contAsig:
                    if(asignatura[cont5Jasig] >= 'A' and asignatura[cont5Jasig] <= 'z'):
                        exAsig5J.append(str(asignatura[cont5Jasig]))
                    cont5Jasig += 1
            elif(examenes5Jun[cont5J] == 'T'):
                asignatura = datosNoNaN.iloc[cont5J, :]
                cont5Jasig = 0
                while cont5Jasig < contAsig:
                    if(asignatura[cont5Jasig] >= 'A' and asignatura[cont5Jasig] <= 'z'):
                        exAsig5J.append(str(asignatura[cont5Jasig]))
                    cont5Jasig += 1
            cont5J += 1
        ################################
        cont6J = 0
        cont6Jasig = 0
        exAsig6J = []

        while cont6J < contTope:
            if(examenes6Jun[cont6J] == 'M'):
                asignatura = datosNoNaN.iloc[cont6J, :]
                cont6Jasig = 0
                while cont6Jasig < contAsig:
                    if(asignatura[cont6Jasig] >= 'A' and asignatura[cont6Jasig] <= 'z'):
                        exAsig6J.append(str(asignatura[cont6Jasig]))
                    cont6Jasig += 1
            elif(examenes6Jun[cont6J] == 'T'):
                asignatura = datosNoNaN.iloc[cont6J, :]
                cont6Jasig = 0
                while cont6Jasig < contAsig:
                    if(asignatura[cont6Jasig] >= 'A' and asignatura[cont6Jasig] <= 'z'):
                        exAsig6J.append(str(asignatura[cont6Jasig]))
                    cont6Jasig += 1
            cont6J += 1
        ################################
        cont7J = 0
        cont7Jasig = 0
        exAsig7J = []

        while cont7J < contTope:
            if(examenes7Jun[cont7J] == 'M'):
                asignatura = datosNoNaN.iloc[cont7J, :]
                cont7Jasig = 0
                while cont7Jasig < contAsig:
                    if(asignatura[cont7Jasig] >= 'A' and asignatura[cont7Jasig] <= 'z'):
                        exAsig7J.append(str(asignatura[cont7Jasig]))
                    cont7Jasig += 1
            elif(examenes7Jun[cont7J] == 'T'):
                asignatura = datosNoNaN.iloc[cont7J, :]
                cont7Jasig = 0
                while cont7Jasig < contAsig:
                    if(asignatura[cont7Jasig] >= 'A' and asignatura[cont7Jasig] <= 'z'):
                        exAsig7J.append(str(asignatura[cont7Jasig]))
                    cont7Jasig += 1
            cont7J += 1
        ################################
        cont10J = 0
        cont10Jasig = 0
        exAsig10J = []

        while cont10J < contTope:
            if(examenes10Jun[cont10J] == 'M'):
                asignatura = datosNoNaN.iloc[cont10J, :]
                cont10Jasig = 0
                while cont10Jasig < contAsig:
                    if(asignatura[cont10Jasig] >= 'A' and asignatura[cont10Jasig] <= 'z'):
                        exAsig10J.append(str(asignatura[cont10Jasig]))
                    cont10Jasig += 1
            elif(examenes10Jun[cont10J] == 'T'):
                asignatura = datosNoNaN.iloc[cont10J, :]
                cont10Jasig = 0
                while cont10Jasig < contAsig:
                    if(asignatura[cont10Jasig] >= 'A' and asignatura[cont10Jasig] <= 'z'):
                        exAsig10J.append(str(asignatura[cont10Jasig]))
                    cont10Jasig += 1
            cont10J += 1
        ################################
        cont11J = 0
        cont11Jasig = 0
        exAsig11J = []

        while cont11J < contTope:
            if(examenes11Jun[cont11J] == 'M'):
                asignatura = datosNoNaN.iloc[cont11J, :]
                cont11Jasig = 0
                while cont11Jasig < contAsig:
                    if(asignatura[cont11Jasig] >= 'A' and asignatura[cont11Jasig] <= 'z'):
                        exAsig11J.append(str(asignatura[cont11Jasig]))
                    cont11Jasig += 1
            elif(examenes11Jun[cont11J] == 'T'):
                asignatura = datosNoNaN.iloc[cont11J, :]
                cont11Jasig = 0
                while cont11Jasig < contAsig:
                    if(asignatura[cont11Jasig] >= 'A' and asignatura[cont11Jasig] <= 'z'):
                        exAsig11J.append(str(asignatura[cont11Jasig]))
                    cont11Jasig += 1
            cont11J += 1
        ################################
        cont12J = 0
        cont12Jasig = 0
        exAsig12J = []

        while cont12J < contTope:
            if(examenes12Jun[cont12J] == 'M'):
                asignatura = datosNoNaN.iloc[cont12J, :]
                cont12Jasig = 0
                while cont12Jasig < contAsig:
                    if(asignatura[cont12Jasig] >= 'A' and asignatura[cont12Jasig] <= 'z'):
                        exAsig12J.append(str(asignatura[cont12Jasig]))
                    cont12Jasig += 1
            elif(examenes12Jun[cont12J] == 'T'):
                asignatura = datosNoNaN.iloc[cont12J, :]
                cont12Jasig = 0
                while cont12Jasig < contAsig:
                    if(asignatura[cont12Jasig] >= 'A' and asignatura[cont12Jasig] <= 'z'):
                        exAsig12J.append(str(asignatura[cont12Jasig]))
                    cont12Jasig += 1
            cont12J += 1
        ################################
        cont13J = 0
        cont13Jasig = 0
        exAsig13J = []

        while cont13J < contTope:
            if(examenes13Jun[cont13J] == 'M'):
                asignatura = datosNoNaN.iloc[cont13J, :]
                cont13Jasig = 0
                while cont13Jasig < contAsig:
                    if(asignatura[cont13Jasig] >= 'A' and asignatura[cont13Jasig] <= 'z'):
                        exAsig13J.append(str(asignatura[cont13Jasig]))
                    cont13Jasig += 1
            elif(examenes13Jun[cont13J] == 'T'):
                asignatura = datosNoNaN.iloc[cont13J, :]
                cont13Jasig = 0
                while cont13Jasig < contAsig:
                    if(asignatura[cont13Jasig] >= 'A' and asignatura[cont13Jasig] <= 'z'):
                        exAsig13J.append(str(asignatura[cont13Jasig]))
                    cont13Jasig += 1
            cont13J += 1
        ################################
        cont14J = 0
        cont14Jasig = 0
        exAsig14J = []

        while cont14J < contTope:
            if(examenes14Jun[cont14J] == 'M'):
                asignatura = datosNoNaN.iloc[cont14J, :]
                cont14Jasig = 0
                while cont14Jasig < contAsig:
                    if(asignatura[cont14Jasig] >= 'A' and asignatura[cont14Jasig] <= 'z'):
                        exAsig14J.append(str(asignatura[cont14Jasig]))
                    cont14Jasig += 1
            elif(examenes14Jun[cont14J] == 'T'):
                asignatura = datosNoNaN.iloc[cont14J, :]
                cont14Jasig = 0
                while cont14Jasig < contAsig:
                    if(asignatura[cont14Jasig] >= 'A' and asignatura[cont14Jasig] <= 'z'):
                        exAsig14J.append(str(asignatura[cont14Jasig]))
                    cont14Jasig += 1
            cont14J += 1
        ################################
        cont17J = 0
        cont17Jasig = 0
        exAsig17J = []

        while cont17J < contTope:
            if(examenes17Jun[cont17J] == 'M'):
                asignatura = datosNoNaN.iloc[cont17J, :]
                cont17Jasig = 0
                while cont17Jasig < contAsig:
                    if(asignatura[cont17Jasig] >= 'A' and asignatura[cont17Jasig] <= 'z'):
                        exAsig17J.append(str(asignatura[cont17Jasig]))
                    cont17Jasig += 1
            elif(examenes17Jun[cont17J] == 'T'):
                asignatura = datosNoNaN.iloc[cont17J, :]
                cont17Jasig = 0
                while cont17Jasig < contAsig:
                    if(asignatura[cont17Jasig] >= 'A' and asignatura[cont17Jasig] <= 'z'):
                        exAsig17J.append(str(asignatura[cont17Jasig]))
                    cont17Jasig += 1
            cont17J += 1
        ################################
        cont18J = 0
        cont18Jasig = 0
        exAsig18J = []

        while cont18J < contTope:
            if(examenes18Jun[cont18J] == 'M'):
                asignatura = datosNoNaN.iloc[cont18J, :]
                cont18Jasig = 0
                while cont18Jasig < contAsig:
                    if(asignatura[cont18Jasig] >= 'A' and asignatura[cont18Jasig] <= 'z'):
                        exAsig18J.append(str(asignatura[cont18Jasig]))
                    cont18Jasig += 1
            elif(examenes18Jun[cont18J] == 'T'):
                asignatura = datosNoNaN.iloc[cont18J, :]
                cont18Jasig = 0
                while cont18Jasig < contAsig:
                    if(asignatura[cont18Jasig] >= 'A' and asignatura[cont18Jasig] <= 'z'):
                        exAsig18J.append(str(asignatura[cont18Jasig]))
                    cont18Jasig += 1
            cont18J += 1
        ################################
        cont19J = 0
        cont19Jasig = 0
        exAsig19J = []

        while cont19J < contTope:
            if(examenes19Jun[cont19J] == 'M'):
                asignatura = datosNoNaN.iloc[cont19J, :]
                cont19Jasig = 0
                while cont19Jasig < contAsig:
                    if(asignatura[cont19Jasig] >= 'A' and asignatura[cont19Jasig] <= 'z'):
                        exAsig19J.append(str(asignatura[cont19Jasig]))
                    cont19Jasig += 1
            elif(examenes19Jun[cont19J] == 'T'):
                asignatura = datosNoNaN.iloc[cont19J, :]
                cont19Jasig = 0
                while cont19Jasig < contAsig:
                    if(asignatura[cont19Jasig] >= 'A' and asignatura[cont19Jasig] <= 'z'):
                        exAsig19J.append(str(asignatura[cont19Jasig]))
                    cont19Jasig += 1
            cont19J += 1
        ################################
        # Comprobación del contenido
        cont = 0
        print("------------------------------------")
        print("2do Semestre - Ordinaria cont 2")
        print("------------------------------------")
        while cont < len(exAsig19J):
            print(str(exAsig19J[cont]))
            cont += 1


def extractDataTable1_2SemExtraordinaria():
    tablas = camelot.read_pdf(os.path.join(RESOURCE, 'CalendarioExamenes18-19-GII.pdf'), pages='8')
    tablas.export(os.path.join(OUTPUT, 'CalendarioExamenes18-19-GII.csv'), f='csv', compress=False)

    with open(os.path.join(OUTPUT, 'CalendarioExamenes18-19-GII-page-8-table-1.csv'), 'r') as archivo:
        datos = pd.read_csv(archivo, header=-1)
        datosNoNaN = datos.fillna(value='0')

    examenes27Jun = datosNoNaN.iloc[:,6]
    examenes28Jun = datosNoNaN.iloc[:,7]
    examenes1Jul = datosNoNaN.iloc[:,9]
    examenes2Jul = datosNoNaN.iloc[:,10]
    examenes3Jul = datosNoNaN.iloc[:,11]
    examenes4Jul = datosNoNaN.iloc[:,12]
    examenes5Jul = datosNoNaN.iloc[:,13]
    examenes8Jul = datosNoNaN.iloc[:,15]
    examenes9Jul = datosNoNaN.iloc[:,16]
    examenes10Jul = datosNoNaN.iloc[:,17]
    examenes11Jul = datosNoNaN.iloc[:,18]

    # print(examenes10Ene.value_counts())
    # print(examenes10Ene.count())
    # print(examenes10Ene)
    # print(datosNoNaN.iloc[3,:])

    contTope = examenes27Jun.count()
    contAsig = datosNoNaN.iloc[3,:].count()
    cont27J = 0
    cont27Jasig = 0
    exAsig27J = []

    while cont27J < contTope:
        if(examenes27Jun[cont27J]=='M'):
            asignatura = datosNoNaN.iloc[cont27J,:]
            cont27Jasig = 0
            while cont27Jasig < contAsig:
                if(asignatura[cont27Jasig] >= 'A' and asignatura[cont27Jasig] <= 'z'):
                    exAsig27J.append(str(asignatura[cont27Jasig]))
                cont27Jasig+=1
        elif(examenes27Jun[cont27J]=='T'):
            asignatura = datosNoNaN.iloc[cont27J,:]
            cont27Jasig = 0
            while cont27Jasig < contAsig:
                if(asignatura[cont27Jasig] >= 'A' and asignatura[cont27Jasig] <= 'z'):
                    exAsig27J.append(str(asignatura[cont27Jasig]))
                cont27Jasig+=1
        cont27J+=1
    ################################
    cont28J = 0
    cont28Jasig = 0
    exAsig28J = []

    while cont28J < contTope:
        if(examenes28Jun[cont28J]=='M'):
            asignatura = datosNoNaN.iloc[cont28J,:]
            cont28Jasig = 0
            while cont28Jasig < contAsig:
                if(asignatura[cont28Jasig] >= 'A' and asignatura[cont28Jasig] <= 'z'):
                    exAsig28J.append(str(asignatura[cont28Jasig]))
                cont28Jasig+=1
        elif(examenes28Jun[cont28J]=='T'):
            asignatura = datosNoNaN.iloc[cont28J,:]
            cont28Jasig = 0
            while cont28Jasig < contAsig:
                if(asignatura[cont28Jasig] >= 'A' and asignatura[cont28Jasig] <= 'z'):
                    exAsig28J.append(str(asignatura[cont28Jasig]))
                cont28Jasig+=1
        cont28J+=1
    ################################
    cont1J = 0
    cont1Jasig = 0
    exAsig1J = []

    while cont1J < contTope:
        if(examenes1Jul[cont1J]=='M'):
            asignatura = datosNoNaN.iloc[cont1J,:]
            cont1Jasig = 0
            while cont1Jasig < contAsig:
                if(asignatura[cont1Jasig] >= 'A' and asignatura[cont1Jasig] <= 'z'):
                    exAsig1J.append(str(asignatura[cont1Jasig]))
                cont1Jasig+=1
        elif(examenes1Jul[cont1J]=='T'):
            asignatura = datosNoNaN.iloc[cont1J,:]
            cont1Jasig = 0
            while cont1Jasig < contAsig:
                if(asignatura[cont1Jasig] >= 'A' and asignatura[cont1Jasig] <= 'z'):
                    exAsig1J.append(str(asignatura[cont1Jasig]))
                cont1Jasig+=1
        cont1J+=1
    ################################
    cont2J = 0
    cont2Jasig = 0
    exAsig2J = []

    while cont2J < contTope:
        if(examenes2Jul[cont2J]=='M'):
            asignatura = datosNoNaN.iloc[cont2J,:]
            cont2Jasig = 0
            while cont2Jasig < contAsig:
                if(asignatura[cont2Jasig] >= 'A' and asignatura[cont2Jasig] <= 'z'):
                    exAsig2J.append(str(asignatura[cont2Jasig]))
                cont2Jasig+=1
        elif(examenes2Jul[cont2J]=='T'):
            asignatura = datosNoNaN.iloc[cont2J,:]
            cont2Jasig = 0
            while cont2Jasig < contAsig:
                if(asignatura[cont2Jasig] >= 'A' and asignatura[cont2Jasig] <= 'z'):
                    exAsig2J.append(str(asignatura[cont2Jasig]))
                cont2Jasig+=1
        cont2J+=1
    ################################
    cont3J = 0
    cont3Jasig = 0
    exAsig3J = []

    while cont3J < contTope:
        if(examenes3Jul[cont3J]=='M'):
            asignatura = datosNoNaN.iloc[cont3J,:]
            cont3Jasig = 0
            while cont3Jasig < contAsig:
                if(asignatura[cont3Jasig] >= 'A' and asignatura[cont3Jasig] <= 'z'):
                    exAsig3J.append(str(asignatura[cont3Jasig]))
                cont3Jasig+=1
        elif(examenes3Jul[cont3J]=='T'):
            asignatura = datosNoNaN.iloc[cont3J,:]
            cont3Jasig = 0
            while cont3Jasig < contAsig:
                if(asignatura[cont3Jasig] >= 'A' and asignatura[cont3Jasig] <= 'z'):
                    exAsig3J.append(str(asignatura[cont3Jasig]))
                cont3Jasig+=1
        cont3J+=1
    ################################
    cont4J = 0
    cont4Jasig = 0
    exAsig4J = []

    while cont4J < contTope:
        if(examenes4Jul[cont4J]=='M'):
            asignatura = datosNoNaN.iloc[cont4J,:]
            cont4Jasig = 0
            while cont4Jasig < contAsig:
                if(asignatura[cont4Jasig] >= 'A' and asignatura[cont4Jasig] <= 'z'):
                    exAsig4J.append(str(asignatura[cont4Jasig]))
                cont4Jasig+=1
        elif(examenes4Jul[cont4J]=='T'):
            asignatura = datosNoNaN.iloc[cont4J,:]
            cont4Jasig = 0
            while cont4Jasig < contAsig:
                if(asignatura[cont4Jasig] >= 'A' and asignatura[cont4Jasig] <= 'z'):
                    exAsig4J.append(str(asignatura[cont4Jasig]))
                cont4Jasig+=1
        cont4J+=1
    ################################
    cont5J = 0
    cont5Jasig = 0
    exAsig5J = []

    while cont5J < contTope:
        if(examenes5Jul[cont5J]=='M'):
            asignatura = datosNoNaN.iloc[cont5J,:]
            cont5Jasig = 0
            while cont5Jasig < contAsig:
                if(asignatura[cont5Jasig] >= 'A' and asignatura[cont5Jasig] <= 'z'):
                    exAsig5J.append(str(asignatura[cont5Jasig]))
                cont5Jasig+=1
        elif(examenes5Jul[cont5J]=='T'):
            asignatura = datosNoNaN.iloc[cont5J,:]
            cont5Jasig = 0
            while cont5Jasig < contAsig:
                if(asignatura[cont5Jasig] >= 'A' and asignatura[cont5Jasig] <= 'z'):
                    exAsig5J.append(str(asignatura[cont5Jasig]))
                cont5Jasig+=1
        cont5J+=1
    ################################
    cont8J = 0
    cont8Jasig = 0
    exAsig8J = []

    while cont8J < contTope:
        if(examenes8Jul[cont8J]=='M'):
            asignatura = datosNoNaN.iloc[cont8J,:]
            cont8Jasig = 0
            while cont8Jasig < contAsig:
                if(asignatura[cont8Jasig] >= 'A' and asignatura[cont8Jasig] <= 'z'):
                    exAsig8J.append(str(asignatura[cont8Jasig]))
                cont8Jasig+=1
        elif(examenes8Jul[cont8J]=='T'):
            asignatura = datosNoNaN.iloc[cont8J,:]
            cont8Jasig = 0
            while cont8Jasig < contAsig:
                if(asignatura[cont8Jasig] >= 'A' and asignatura[cont8Jasig] <= 'z'):
                    exAsig8J.append(str(asignatura[cont8Jasig]))
                cont8Jasig+=1
        cont8J+=1
    ################################
    cont9J = 0
    cont9Jasig = 0
    exAsig9J = []

    while cont9J < contTope:
        if(examenes9Jul[cont9J]=='M'):
            asignatura = datosNoNaN.iloc[cont9J,:]
            cont9Jasig = 0
            while cont9Jasig < contAsig:
                if(asignatura[cont9Jasig] >= 'A' and asignatura[cont9Jasig] <= 'z'):
                    exAsig9J.append(str(asignatura[cont9Jasig]))
                cont9Jasig+=1
        elif(examenes9Jul[cont9J]=='T'):
            asignatura = datosNoNaN.iloc[cont9J,:]
            cont9Jasig = 0
            while cont9Jasig < contAsig:
                if(asignatura[cont9Jasig] >= 'A' and asignatura[cont9Jasig] <= 'z'):
                    exAsig9J.append(str(asignatura[cont9Jasig]))
                cont9Jasig+=1
        cont9J+=1
    ################################
    cont10J = 0
    cont10Jasig = 0
    exAsig10J = []

    while cont10J < contTope:
        if(examenes10Jul[cont10J]=='M'):
            asignatura = datosNoNaN.iloc[cont10J,:]
            cont10Jasig = 0
            while cont10Jasig < contAsig:
                if(asignatura[cont10Jasig] >= 'A' and asignatura[cont10Jasig] <= 'z'):
                    exAsig10J.append(str(asignatura[cont10Jasig]))
                cont10Jasig+=1
        elif(examenes10Jul[cont10J]=='T'):
            asignatura = datosNoNaN.iloc[cont10J,:]
            cont10Jasig = 0
            while cont10Jasig < contAsig:
                if(asignatura[cont10Jasig] >= 'A' and asignatura[cont10Jasig] <= 'z'):
                    exAsig10J.append(str(asignatura[cont10Jasig]))
                cont10Jasig+=1
        cont10J+=1
    ################################
    cont11J = 0
    cont11Jasig = 0
    exAsig11J = []

    while cont11J < contTope:
        if(examenes11Jul[cont11J]=='M'):
            asignatura = datosNoNaN.iloc[cont11J,:]
            cont11Jasig = 0
            while cont11Jasig < contAsig:
                if(asignatura[cont11Jasig] >= 'A' and asignatura[cont11Jasig] <= 'z'):
                    exAsig11J.append(str(asignatura[cont11Jasig]))
                cont11Jasig+=1
        elif(examenes11Jul[cont11J]=='T'):
            asignatura = datosNoNaN.iloc[cont11J,:]
            cont11Jasig = 0
            while cont11Jasig < contAsig:
                if(asignatura[cont11Jasig] >= 'A' and asignatura[cont11Jasig] <= 'z'):
                    exAsig11J.append(str(asignatura[cont11Jasig]))
                cont11Jasig+=1
        cont11J+=1
    ################################
    #Comprobación del contenido
    cont=0
    print("------------------------------------")
    print("2do Semestre - Extraordinaria")
    print("------------------------------------")
    while cont < len(exAsig11J):
        print(str(exAsig11J[cont]))
        cont+=1


def extractDataTable2_2SemExtraordinaria():
    tablas = camelot.read_pdf(os.path.join(RESOURCE, 'CalendarioExamenes18-19-GII.pdf'), pages='9')
    tablas.export(os.path.join(OUTPUT, 'CalendarioExamenes18-19-GII.csv'), f='csv', compress=False)

    with open(os.path.join(OUTPUT, 'CalendarioExamenes18-19-GII-page-9-table-1.csv'), 'r') as archivo:
        datos = pd.read_csv(archivo, header=-1)
        datosNoNaN = datos.fillna(value='0')

        examenes27Jun = datosNoNaN.iloc[:,6]
        examenes28Jun = datosNoNaN.iloc[:,7]
        examenes1Jul = datosNoNaN.iloc[:,9]
        examenes2Jul = datosNoNaN.iloc[:,10]
        examenes3Jul = datosNoNaN.iloc[:,11]
        examenes4Jul = datosNoNaN.iloc[:,12]
        examenes5Jul = datosNoNaN.iloc[:,13]
        examenes8Jul = datosNoNaN.iloc[:,15]
        examenes9Jul = datosNoNaN.iloc[:,16]
        examenes10Jul = datosNoNaN.iloc[:,17]
        examenes11Jul = datosNoNaN.iloc[:,18]

        # print(examenes10Ene.value_counts())
        # print(examenes10Ene.count())
        # print(examenes10Ene)
        # print(datosNoNaN.iloc[3,:])

        contTope = examenes27Jun.count()
        contAsig = datosNoNaN.iloc[3,:].count()
        cont27J = 0
        cont27Jasig = 0
        exAsig27J = []

        while cont27J < contTope:
            if(examenes27Jun[cont27J]=='M'):
                asignatura = datosNoNaN.iloc[cont27J,:]
                cont27Jasig = 0
                while cont27Jasig < contAsig:
                    if(asignatura[cont27Jasig] >= 'A' and asignatura[cont27Jasig] <= 'z'):
                        exAsig27J.append(str(asignatura[cont27Jasig]))
                    cont27Jasig+=1
            elif(examenes27Jun[cont27J]=='T'):
                asignatura = datosNoNaN.iloc[cont27J,:]
                cont27Jasig = 0
                while cont27Jasig < contAsig:
                    if(asignatura[cont27Jasig] >= 'A' and asignatura[cont27Jasig] <= 'z'):
                        exAsig27J.append(str(asignatura[cont27Jasig]))
                    cont27Jasig+=1
            cont27J+=1
        ################################
        cont28J = 0
        cont28Jasig = 0
        exAsig28J = []

        while cont28J < contTope:
            if(examenes28Jun[cont28J]=='M'):
                asignatura = datosNoNaN.iloc[cont28J,:]
                cont28Jasig = 0
                while cont28Jasig < contAsig:
                    if(asignatura[cont28Jasig] >= 'A' and asignatura[cont28Jasig] <= 'z'):
                        exAsig28J.append(str(asignatura[cont28Jasig]))
                    cont28Jasig+=1
            elif(examenes28Jun[cont28J]=='T'):
                asignatura = datosNoNaN.iloc[cont28J,:]
                cont28Jasig = 0
                while cont28Jasig < contAsig:
                    if(asignatura[cont28Jasig] >= 'A' and asignatura[cont28Jasig] <= 'z'):
                        exAsig28J.append(str(asignatura[cont28Jasig]))
                    cont28Jasig+=1
            cont28J+=1
        ################################
        cont1J = 0
        cont1Jasig = 0
        exAsig1J = []

        while cont1J < contTope:
            if(examenes1Jul[cont1J]=='M'):
                asignatura = datosNoNaN.iloc[cont1J,:]
                cont1Jasig = 0
                while cont1Jasig < contAsig:
                    if(asignatura[cont1Jasig] >= 'A' and asignatura[cont1Jasig] <= 'z'):
                        exAsig1J.append(str(asignatura[cont1Jasig]))
                    cont1Jasig+=1
            elif(examenes1Jul[cont1J]=='T'):
                asignatura = datosNoNaN.iloc[cont1J,:]
                cont1Jasig = 0
                while cont1Jasig < contAsig:
                    if(asignatura[cont1Jasig] >= 'A' and asignatura[cont1Jasig] <= 'z'):
                        exAsig1J.append(str(asignatura[cont1Jasig]))
                    cont1Jasig+=1
            cont1J+=1
        ################################
        cont2J = 0
        cont2Jasig = 0
        exAsig2J = []

        while cont2J < contTope:
            if(examenes2Jul[cont2J]=='M'):
                asignatura = datosNoNaN.iloc[cont2J,:]
                cont2Jasig = 0
                while cont2Jasig < contAsig:
                    if(asignatura[cont2Jasig] >= 'A' and asignatura[cont2Jasig] <= 'z'):
                        exAsig2J.append(str(asignatura[cont2Jasig]))
                    cont2Jasig+=1
            elif(examenes2Jul[cont2J]=='T'):
                asignatura = datosNoNaN.iloc[cont2J,:]
                cont2Jasig = 0
                while cont2Jasig < contAsig:
                    if(asignatura[cont2Jasig] >= 'A' and asignatura[cont2Jasig] <= 'z'):
                        exAsig2J.append(str(asignatura[cont2Jasig]))
                    cont2Jasig+=1
            cont2J+=1
        ################################
        cont3J = 0
        cont3Jasig = 0
        exAsig3J = []

        while cont3J < contTope:
            if(examenes3Jul[cont3J]=='M'):
                asignatura = datosNoNaN.iloc[cont3J,:]
                cont3Jasig = 0
                while cont3Jasig < contAsig:
                    if(asignatura[cont3Jasig] >= 'A' and asignatura[cont3Jasig] <= 'z'):
                        exAsig3J.append(str(asignatura[cont3Jasig]))
                    cont3Jasig+=1
            elif(examenes3Jul[cont3J]=='T'):
                asignatura = datosNoNaN.iloc[cont3J,:]
                cont3Jasig = 0
                while cont3Jasig < contAsig:
                    if(asignatura[cont3Jasig] >= 'A' and asignatura[cont3Jasig] <= 'z'):
                        exAsig3J.append(str(asignatura[cont3Jasig]))
                    cont3Jasig+=1
            cont3J+=1
        ################################
        cont4J = 0
        cont4Jasig = 0
        exAsig4J = []

        while cont4J < contTope:
            if(examenes4Jul[cont4J]=='M'):
                asignatura = datosNoNaN.iloc[cont4J,:]
                cont4Jasig = 0
                while cont4Jasig < contAsig:
                    if(asignatura[cont4Jasig] >= 'A' and asignatura[cont4Jasig] <= 'z'):
                        exAsig4J.append(str(asignatura[cont4Jasig]))
                    cont4Jasig+=1
            elif(examenes4Jul[cont4J]=='T'):
                asignatura = datosNoNaN.iloc[cont4J,:]
                cont4Jasig = 0
                while cont4Jasig < contAsig:
                    if(asignatura[cont4Jasig] >= 'A' and asignatura[cont4Jasig] <= 'z'):
                        exAsig4J.append(str(asignatura[cont4Jasig]))
                    cont4Jasig+=1
            cont4J+=1
        ################################
        cont5J = 0
        cont5Jasig = 0
        exAsig5J = []

        while cont5J < contTope:
            if(examenes5Jul[cont5J]=='M'):
                asignatura = datosNoNaN.iloc[cont5J,:]
                cont5Jasig = 0
                while cont5Jasig < contAsig:
                    if(asignatura[cont5Jasig] >= 'A' and asignatura[cont5Jasig] <= 'z'):
                        exAsig5J.append(str(asignatura[cont5Jasig]))
                    cont5Jasig+=1
            elif(examenes5Jul[cont5J]=='T'):
                asignatura = datosNoNaN.iloc[cont5J,:]
                cont5Jasig = 0
                while cont5Jasig < contAsig:
                    if(asignatura[cont5Jasig] >= 'A' and asignatura[cont5Jasig] <= 'z'):
                        exAsig5J.append(str(asignatura[cont5Jasig]))
                    cont5Jasig+=1
            cont5J+=1
        ################################
        cont8J = 0
        cont8Jasig = 0
        exAsig8J = []

        while cont8J < contTope:
            if(examenes8Jul[cont8J]=='M'):
                asignatura = datosNoNaN.iloc[cont8J,:]
                cont8Jasig = 0
                while cont8Jasig < contAsig:
                    if(asignatura[cont8Jasig] >= 'A' and asignatura[cont8Jasig] <= 'z'):
                        exAsig8J.append(str(asignatura[cont8Jasig]))
                    cont8Jasig+=1
            elif(examenes8Jul[cont8J]=='T'):
                asignatura = datosNoNaN.iloc[cont8J,:]
                cont8Jasig = 0
                while cont8Jasig < contAsig:
                    if(asignatura[cont8Jasig] >= 'A' and asignatura[cont8Jasig] <= 'z'):
                        exAsig8J.append(str(asignatura[cont8Jasig]))
                    cont8Jasig+=1
            cont8J+=1
        ################################
        cont9J = 0
        cont9Jasig = 0
        exAsig9J = []

        while cont9J < contTope:
            if(examenes9Jul[cont9J]=='M'):
                asignatura = datosNoNaN.iloc[cont9J,:]
                cont9Jasig = 0
                while cont9Jasig < contAsig:
                    if(asignatura[cont9Jasig] >= 'A' and asignatura[cont9Jasig] <= 'z'):
                        exAsig9J.append(str(asignatura[cont9Jasig]))
                    cont9Jasig+=1
            elif(examenes9Jul[cont9J]=='T'):
                asignatura = datosNoNaN.iloc[cont9J,:]
                cont9Jasig = 0
                while cont9Jasig < contAsig:
                    if(asignatura[cont9Jasig] >= 'A' and asignatura[cont9Jasig] <= 'z'):
                        exAsig9J.append(str(asignatura[cont9Jasig]))
                    cont9Jasig+=1
            cont9J+=1
        ################################
        cont10J = 0
        cont10Jasig = 0
        exAsig10J = []

        while cont10J < contTope:
            if(examenes10Jul[cont10J]=='M'):
                asignatura = datosNoNaN.iloc[cont10J,:]
                cont10Jasig = 0
                while cont10Jasig < contAsig:
                    if(asignatura[cont10Jasig] >= 'A' and asignatura[cont10Jasig] <= 'z'):
                        exAsig10J.append(str(asignatura[cont10Jasig]))
                    cont10Jasig+=1
            elif(examenes10Jul[cont10J]=='T'):
                asignatura = datosNoNaN.iloc[cont10J,:]
                cont10Jasig = 0
                while cont10Jasig < contAsig:
                    if(asignatura[cont10Jasig] >= 'A' and asignatura[cont10Jasig] <= 'z'):
                        exAsig10J.append(str(asignatura[cont10Jasig]))
                    cont10Jasig+=1
            cont10J+=1
        ################################
        cont11J = 0
        cont11Jasig = 0
        exAsig11J = []

        while cont11J < contTope:
            if(examenes11Jul[cont11J]=='M'):
                asignatura = datosNoNaN.iloc[cont11J,:]
                cont11Jasig = 0
                while cont11Jasig < contAsig:
                    if(asignatura[cont11Jasig] >= 'A' and asignatura[cont11Jasig] <= 'z'):
                        exAsig11J.append(str(asignatura[cont11Jasig]))
                    cont11Jasig+=1
            elif(examenes11Jul[cont11J]=='T'):
                asignatura = datosNoNaN.iloc[cont11J,:]
                cont11Jasig = 0
                while cont11Jasig < contAsig:
                    if(asignatura[cont11Jasig] >= 'A' and asignatura[cont11Jasig] <= 'z'):
                            exAsig11J.append(str(asignatura[cont11Jasig]))
                    cont11Jasig+=1
            cont11J+=1
        ################################
        #Comprobación del contenido
        cont=0
        print("------------------------------------")
        print("2do Semestre - Extraordinaria cont")
        print("------------------------------------")
        while cont < len(exAsig11J):
            print(str(exAsig11J[cont]))
            cont+=1


def extractDataTable3_2SemExtraordinaria():
    tablas = camelot.read_pdf(os.path.join(RESOURCE, 'CalendarioExamenes18-19-GII.pdf'), pages='10')
    tablas.export(os.path.join(OUTPUT, 'CalendarioExamenes18-19-GII.csv'), f='csv', compress=False)

    with open(os.path.join(OUTPUT, 'CalendarioExamenes18-19-GII-page-10-table-1.csv'), 'r') as archivo:
        datos = pd.read_csv(archivo, header=-1)
        datosNoNaN = datos.fillna(value='0')

        examenes27Jun = datosNoNaN.iloc[:,6]
        examenes28Jun = datosNoNaN.iloc[:,7]
        examenes1Jul = datosNoNaN.iloc[:,9]
        examenes2Jul = datosNoNaN.iloc[:,10]
        examenes3Jul = datosNoNaN.iloc[:,11]
        examenes4Jul = datosNoNaN.iloc[:,12]
        examenes5Jul = datosNoNaN.iloc[:,13]
        examenes8Jul = datosNoNaN.iloc[:,15]
        examenes9Jul = datosNoNaN.iloc[:,16]
        examenes10Jul = datosNoNaN.iloc[:,17]
        examenes11Jul = datosNoNaN.iloc[:,18]

        # print(examenes10Ene.value_counts())
        # print(examenes10Ene.count())
        # print(examenes10Ene)
        # print(datosNoNaN.iloc[3,:])

        contTope = examenes27Jun.count()
        contAsig = datosNoNaN.iloc[3,:].count()
        cont27J = 0
        cont27Jasig = 0
        exAsig27J = []

        while cont27J < contTope:
            if(examenes27Jun[cont27J]=='M'):
                asignatura = datosNoNaN.iloc[cont27J,:]
                cont27Jasig = 0
                while cont27Jasig < contAsig:
                    if(asignatura[cont27Jasig] >= 'A' and asignatura[cont27Jasig] <= 'z'):
                        exAsig27J.append(str(asignatura[cont27Jasig]))
                    cont27Jasig+=1
            elif(examenes27Jun[cont27J]=='T'):
                asignatura = datosNoNaN.iloc[cont27J,:]
                cont27Jasig = 0
                while cont27Jasig < contAsig:
                    if(asignatura[cont27Jasig] >= 'A' and asignatura[cont27Jasig] <= 'z'):
                        exAsig27J.append(str(asignatura[cont27Jasig]))
                    cont27Jasig+=1
            cont27J+=1
        ################################
        cont28J = 0
        cont28Jasig = 0
        exAsig28J = []

        while cont28J < contTope:
            if(examenes28Jun[cont28J]=='M'):
                asignatura = datosNoNaN.iloc[cont28J,:]
                cont28Jasig = 0
                while cont28Jasig < contAsig:
                    if(asignatura[cont28Jasig] >= 'A' and asignatura[cont28Jasig] <= 'z'):
                        exAsig28J.append(str(asignatura[cont28Jasig]))
                    cont28Jasig+=1
            elif(examenes28Jun[cont28J]=='T'):
                asignatura = datosNoNaN.iloc[cont28J,:]
                cont28Jasig = 0
                while cont28Jasig < contAsig:
                    if(asignatura[cont28Jasig] >= 'A' and asignatura[cont28Jasig] <= 'z'):
                        exAsig28J.append(str(asignatura[cont28Jasig]))
                    cont28Jasig+=1
            cont28J+=1
        ################################
        cont1J = 0
        cont1Jasig = 0
        exAsig1J = []

        while cont1J < contTope:
            if(examenes1Jul[cont1J]=='M'):
                asignatura = datosNoNaN.iloc[cont1J,:]
                cont1Jasig = 0
                while cont1Jasig < contAsig:
                    if(asignatura[cont1Jasig] >= 'A' and asignatura[cont1Jasig] <= 'z'):
                        exAsig1J.append(str(asignatura[cont1Jasig]))
                    cont1Jasig+=1
            elif(examenes1Jul[cont1J]=='T'):
                asignatura = datosNoNaN.iloc[cont1J,:]
                cont1Jasig = 0
                while cont1Jasig < contAsig:
                    if(asignatura[cont1Jasig] >= 'A' and asignatura[cont1Jasig] <= 'z'):
                        exAsig1J.append(str(asignatura[cont1Jasig]))
                    cont1Jasig+=1
            cont1J+=1
        ################################
        cont2J = 0
        cont2Jasig = 0
        exAsig2J = []

        while cont2J < contTope:
            if(examenes2Jul[cont2J]=='M'):
                asignatura = datosNoNaN.iloc[cont2J,:]
                cont2Jasig = 0
                while cont2Jasig < contAsig:
                    if(asignatura[cont2Jasig] >= 'A' and asignatura[cont2Jasig] <= 'z'):
                        exAsig2J.append(str(asignatura[cont2Jasig]))
                    cont2Jasig+=1
            elif(examenes2Jul[cont2J]=='T'):
                asignatura = datosNoNaN.iloc[cont2J,:]
                cont2Jasig = 0
                while cont2Jasig < contAsig:
                    if(asignatura[cont2Jasig] >= 'A' and asignatura[cont2Jasig] <= 'z'):
                        exAsig2J.append(str(asignatura[cont2Jasig]))
                    cont2Jasig+=1
            cont2J+=1
        ################################
        cont3J = 0
        cont3Jasig = 0
        exAsig3J = []

        while cont3J < contTope:
            if(examenes3Jul[cont3J]=='M'):
                asignatura = datosNoNaN.iloc[cont3J,:]
                cont3Jasig = 0
                while cont3Jasig < contAsig:
                    if(asignatura[cont3Jasig] >= 'A' and asignatura[cont3Jasig] <= 'z'):
                        exAsig3J.append(str(asignatura[cont3Jasig]))
                    cont3Jasig+=1
            elif(examenes3Jul[cont3J]=='T'):
                asignatura = datosNoNaN.iloc[cont3J,:]
                cont3Jasig = 0
                while cont3Jasig < contAsig:
                    if(asignatura[cont3Jasig] >= 'A' and asignatura[cont3Jasig] <= 'z'):
                        exAsig3J.append(str(asignatura[cont3Jasig]))
                    cont3Jasig+=1
            cont3J+=1
        ################################
        cont4J = 0
        cont4Jasig = 0
        exAsig4J = []

        while cont4J < contTope:
            if(examenes4Jul[cont4J]=='M'):
                asignatura = datosNoNaN.iloc[cont4J,:]
                cont4Jasig = 0
                while cont4Jasig < contAsig:
                    if(asignatura[cont4Jasig] >= 'A' and asignatura[cont4Jasig] <= 'z'):
                        exAsig4J.append(str(asignatura[cont4Jasig]))
                    cont4Jasig+=1
            elif(examenes4Jul[cont4J]=='T'):
                asignatura = datosNoNaN.iloc[cont4J,:]
                cont4Jasig = 0
                while cont4Jasig < contAsig:
                    if(asignatura[cont4Jasig] >= 'A' and asignatura[cont4Jasig] <= 'z'):
                        exAsig4J.append(str(asignatura[cont4Jasig]))
                    cont4Jasig+=1
            cont4J+=1
        ################################
        cont5J = 0
        cont5Jasig = 0
        exAsig5J = []

        while cont5J < contTope:
            if(examenes5Jul[cont5J]=='M'):
                asignatura = datosNoNaN.iloc[cont5J,:]
                cont5Jasig = 0
                while cont5Jasig < contAsig:
                    if(asignatura[cont5Jasig] >= 'A' and asignatura[cont5Jasig] <= 'z'):
                        exAsig5J.append(str(asignatura[cont5Jasig]))
                    cont5Jasig+=1
            elif(examenes5Jul[cont5J]=='T'):
                asignatura = datosNoNaN.iloc[cont5J,:]
                cont5Jasig = 0
                while cont5Jasig < contAsig:
                    if(asignatura[cont5Jasig] >= 'A' and asignatura[cont5Jasig] <= 'z'):
                        exAsig5J.append(str(asignatura[cont5Jasig]))
                    cont5Jasig+=1
            cont5J+=1
        ################################
        cont8J = 0
        cont8Jasig = 0
        exAsig8J = []

        while cont8J < contTope:
            if(examenes8Jul[cont8J]=='M'):
                asignatura = datosNoNaN.iloc[cont8J,:]
                cont8Jasig = 0
                while cont8Jasig < contAsig:
                    if(asignatura[cont8Jasig] >= 'A' and asignatura[cont8Jasig] <= 'z'):
                        exAsig8J.append(str(asignatura[cont8Jasig]))
                    cont8Jasig+=1
            elif(examenes8Jul[cont8J]=='T'):
                asignatura = datosNoNaN.iloc[cont8J,:]
                cont8Jasig = 0
                while cont8Jasig < contAsig:
                    if(asignatura[cont8Jasig] >= 'A' and asignatura[cont8Jasig] <= 'z'):
                        exAsig8J.append(str(asignatura[cont8Jasig]))
                    cont8Jasig+=1
            cont8J+=1
        ################################
        cont9J = 0
        cont9Jasig = 0
        exAsig9J = []

        while cont9J < contTope:
            if(examenes9Jul[cont9J]=='M'):
                asignatura = datosNoNaN.iloc[cont9J,:]
                cont9Jasig = 0
                while cont9Jasig < contAsig:
                    if(asignatura[cont9Jasig] >= 'A' and asignatura[cont9Jasig] <= 'z'):
                        exAsig9J.append(str(asignatura[cont9Jasig]))
                    cont9Jasig+=1
            elif(examenes9Jul[cont9J]=='T'):
                asignatura = datosNoNaN.iloc[cont9J,:]
                cont9Jasig = 0
                while cont9Jasig < contAsig:
                    if(asignatura[cont9Jasig] >= 'A' and asignatura[cont9Jasig] <= 'z'):
                        exAsig9J.append(str(asignatura[cont9Jasig]))
                    cont9Jasig+=1
            cont9J+=1
        ################################
        cont10J = 0
        cont10Jasig = 0
        exAsig10J = []

        while cont10J < contTope:
            if(examenes10Jul[cont10J]=='M'):
                asignatura = datosNoNaN.iloc[cont10J,:]
                cont10Jasig = 0
                while cont10Jasig < contAsig:
                    if(asignatura[cont10Jasig] >= 'A' and asignatura[cont10Jasig] <= 'z'):
                        exAsig10J.append(str(asignatura[cont10Jasig]))
                    cont10Jasig+=1
            elif(examenes10Jul[cont10J]=='T'):
                asignatura = datosNoNaN.iloc[cont10J,:]
                cont10Jasig = 0
                while cont10Jasig < contAsig:
                    if(asignatura[cont10Jasig] >= 'A' and asignatura[cont10Jasig] <= 'z'):
                        exAsig10J.append(str(asignatura[cont10Jasig]))
                    cont10Jasig+=1
            cont10J+=1
        ################################
        cont11J = 0
        cont11Jasig = 0
        exAsig11J = []

        while cont11J < contTope:
            if(examenes11Jul[cont11J]=='M'):
                asignatura = datosNoNaN.iloc[cont11J,:]
                cont11Jasig = 0
                while cont11Jasig < contAsig:
                    if(asignatura[cont11Jasig] >= 'A' and asignatura[cont11Jasig] <= 'z'):
                        exAsig11J.append(str(asignatura[cont11Jasig]))
                    cont11Jasig+=1
            elif(examenes11Jul[cont11J]=='T'):
                asignatura = datosNoNaN.iloc[cont11J,:]
                cont11Jasig = 0
                while cont11Jasig < contAsig:
                    if(asignatura[cont11Jasig] >= 'A' and asignatura[cont11Jasig] <= 'z'):
                            exAsig11J.append(str(asignatura[cont11Jasig]))
                    cont11Jasig+=1
            cont11J+=1
        ################################
        #Comprobación del contenido
        cont=0
        print("------------------------------------")
        print("2do Semestre - Extraordinaria cont")
        print("------------------------------------")
        while cont < len(exAsig10J):
            print(str(exAsig10J[cont]))
            cont+=1

if __name__ == '__main__':
    if(sys.argv[3:]):
        connect_db = psycopg2.connect(database=db, user=usuario, password=pw, host=host_db)
        cursor = connect_db.cursor()

        asignaturaEX = sys.argv[1]

        if(sys.argv[2] == '1' or sys.argv[2] == 'primero'):
            if(sys.argv[3] == 'ordinaria'):
                res = extractDataTable1_1SemOrdinaria(asignaturaEX)
                if len(res) == 0:
                    res = extractDataTable2_1SemOrdinaria(asignaturaEX)

                sql_insert_query = """INSERT INTO "FechasExamenes" VALUES(%s, %s, %s, %s)"""
                insert_tuple = (asignaturaEX, 1, 'ordinaria', res)
                result = cursor.execute(sql_insert_query, insert_tuple)

                connect_db.commit()
                print("Fila insertada correctamente")

            if(sys.argv[3] == 'extraordinaria'):
                res = extractDataTable1_1SemExtraordinaria(asignaturaEX)
                if len(res) == 0:
                    res = extractDataTable2_1SemExtraordinaria(asignaturaEX)

                sql_insert_query = """INSERT INTO "FechasExamenes" VALUES(%s, %s, %s, %s)"""
                insert_tuple = (asignaturaEX, 1, 'extraordinaria', res)
                result = cursor.execute(sql_insert_query, insert_tuple)

                connect_db.commit()
                print("Fila insertada correctamente")                

        # extractDataTable1_2SemOrdinaria()
        # extractDataTable2_2SemOrdinaria()
        # extractDataTable3_2SemOrdinaria()
        # extractDataTable1_2SemExtraordinaria()
        # extractDataTable2_2SemExtraordinaria()
        # extractDataTable3_2SemExtraordinaria()
