#!/usr/bin/env python
# -*- coding: utf-8 -*-

import camelot
import csv
import os
import pandas as pd

RESOURCE = './resources'
OUTPUT = './outputs'

def extractDataTeable1_1A1C_1A2C():
    tablas = camelot.read_pdf(os.path.join(
        RESOURCE, 'CalendarioExamenes18-19-GII.pdf'), pages='2')
    tablas.export(os.path.join(
        OUTPUT, 'CalendarioExamenes18-19-GII.csv'), f='csv', compress=False)

    with open(os.path.join(OUTPUT, './HORARIOS/HORARIOS1819-page-1-table-1.csv'), 'r') as archivo:
        datos = pd.read_csv(archivo, header=0)
        datosNoNaN = datos.fillna(value='0')

        contDias = datosNoNaN.iloc[0, :].count()-1;
        contHoras = datosNoNaN.iloc[1:, 0].count()
        hora = datosNoNaN.iloc[1:, 0][1]
        contFilL = 1
        contColL = 1
        lunes = []

        # De esta forma me saca lo siguiente: (Por horas)

        #['9:30-10:30', 'FFT(A1)\nFP (A2)\nCA (A3)\n3.6\n2.1\n3.5', 
        # '9:30-10:30', 'FP (A1)\nFS (A2)\nFFT (A3)\n3.1\n2.1\n3.6', 
        # '9:30-10:30', 'FFT\n0.2', 
        # '9:30-10:30', 'FS (A1)\nALEM(A2)\nFP(A3)\n2.1\n2.2\n3.1', 
        # '9:30-10:30', 'ALEM(A1)\nFFT (A2)\nFS (A3)\n2.3\n3.6\n3.1']


        # while contFilL <= contHoras:
        #     if(datosNoNaN.iloc[1:, 0][contFilL] != '0'):
        #         contFilL+=1
        #         while contColL <= contDias:
        #             if(datosNoNaN.iloc[:, contColL][contFilL] != '0'):
        #                 resultado.append(datosNoNaN.iloc[1:, 0][contFilL])
        #                 resultado.append(datosNoNaN.iloc[:, contColL][contFilL])
        #                 # print(resultado)
        #                 contColL+=1
        #             else:
        #                 contColL+=1
        #     else:
        #         contFilL+=1;
        
        # print(resultado)

        # De esta forma me saca lo siguiente: (Por días)
        # ['9:30-10:30', 'FP (A1)\nFS (A2)\nFFT (A3)\n3.1\n2.1\n3.6', 
        # '10:30-11:30', 'FP (A1)\nFS (A2)\nFFT (A3)\n3.1\n2.1\n3.6', 
        # '11:30-12:30', 'CA\n0.2', 
        # '12:30-13:30', 'FP\n0.2']

        while contColL <= contDias:
            if(datosNoNaN.iloc[1:, 0][contColL] != '0'):
                contColL+=1
                while contFilL <= contHoras:
                    if(datosNoNaN.iloc[:, contColL-1][contFilL] != '0'):
                        lunes.append(datosNoNaN.iloc[1:, 0][contFilL])
                        lunes.append(datosNoNaN.iloc[:, contColL-1][contFilL])
                        contFilL+=1
                    else:
                        contFilL+=1
            else:
                contColL+=1;

        ##################################################################
            
        contFilM = 1
        contColM = 1
        martes = []

        while contColM <= contDias:
            if(datosNoNaN.iloc[1:, 0][contColM] != '0'):
                contColM+=1
                while contFilM <= contHoras:
                    if(datosNoNaN.iloc[:, contColM][contFilM] != '0'):
                        martes.append(datosNoNaN.iloc[1:, 0][contFilM])
                        martes.append(datosNoNaN.iloc[:, contColM][contFilM])
                        contFilM+=1
                    else:
                        contFilM+=1
            else:
                contColM+=1;

        ##################################################################

        contFilX = 1
        contColX = 1
        miercoles = []

        while contColX <= contDias:
            if(datosNoNaN.iloc[1:, 0][contColX] != '0'):
                contColX+=1
                while contFilX <= contHoras:
                    if(datosNoNaN.iloc[:, contColX+1][contFilX] != '0'):
                        miercoles.append(datosNoNaN.iloc[1:, 0][contFilX])
                        miercoles.append(datosNoNaN.iloc[:, contColX+1][contFilX])
                        contFilX+=1
                    else:
                        contFilX+=1
            else:
                contColX+=1;

        ##################################################################

        contFilJ = 1
        contColJ = 1
        jueves = []

        while contColJ <= contDias:
            if(datosNoNaN.iloc[1:, 0][contColJ] != '0'):
                contColJ+=1
                while contFilJ <= contHoras:
                    if(datosNoNaN.iloc[:, contColJ+2][contFilJ] != '0'):
                        jueves.append(datosNoNaN.iloc[1:, 0][contFilJ])
                        jueves.append(datosNoNaN.iloc[:, contColJ+2][contFilJ])
                        contFilJ+=1
                    else:
                        contFilJ+=1
            else:
                contColJ+=1;

        ##################################################################

        contFilV = 1
        contColV = 1
        viernes = []

        while contColV <= contDias:
            if(datosNoNaN.iloc[1:, 0][contColV] != '0'):
                contColV+=1
                while contFilV <= contHoras:
                    if(datosNoNaN.iloc[:, contColV+3][contFilV] != '0'):
                        viernes.append(datosNoNaN.iloc[1:, 0][contFilV])
                        viernes.append(datosNoNaN.iloc[:, contColV+3][contFilV])
                        contFilV+=1
                    else:
                        contFilV+=1
            else:
                contColV+=1;
        
    with open(os.path.join(OUTPUT, './HORARIOS/HORARIOS1819-page-1-table-2.csv'), 'r') as archivo:
        datos = pd.read_csv(archivo, header=0)
        datosNoNaN = datos.fillna(value='0')

        contDias = datosNoNaN.iloc[0, :].count()-1;
        contHoras = datosNoNaN.iloc[1:, 0].count()
        hora = datosNoNaN.iloc[1:, 0][1]
        contFilL = 1
        contColL = 1
        lunes = []

        while contColL <= contDias:
            if(datosNoNaN.iloc[1:, 0][contColL] != '0'):
                contColL+=1
                while contFilL <= contHoras:
                    if(datosNoNaN.iloc[:, contColL-1][contFilL] != '0'):
                        lunes.append(datosNoNaN.iloc[1:, 0][contFilL])
                        lunes.append(datosNoNaN.iloc[:, contColL-1][contFilL])
                        contFilL+=1
                    else:
                        contFilL+=1
            else:
                contColL+=1;

        ##################################################################
            
        contFilM = 1
        contColM = 1
        martes = []

        while contColM <= contDias:
            if(datosNoNaN.iloc[1:, 0][contColM] != '0'):
                contColM+=1
                while contFilM <= contHoras:
                    if(datosNoNaN.iloc[:, contColM][contFilM] != '0'):
                        martes.append(datosNoNaN.iloc[1:, 0][contFilM])
                        martes.append(datosNoNaN.iloc[:, contColM][contFilM])
                        contFilM+=1
                    else:
                        contFilM+=1
            else:
                contColM+=1;

        ##################################################################

        contFilX = 1
        contColX = 1
        miercoles = []

        while contColX <= contDias:
            if(datosNoNaN.iloc[1:, 0][contColX] != '0'):
                contColX+=1
                while contFilX <= contHoras:
                    if(datosNoNaN.iloc[:, contColX+1][contFilX] != '0'):
                        miercoles.append(datosNoNaN.iloc[1:, 0][contFilX])
                        miercoles.append(datosNoNaN.iloc[:, contColX+1][contFilX])
                        contFilX+=1
                    else:
                        contFilX+=1
            else:
                contColX+=1;

        ##################################################################

        contFilJ = 1
        contColJ = 1
        jueves = []

        while contColJ <= contDias:
            if(datosNoNaN.iloc[1:, 0][contColJ] != '0'):
                contColJ+=1
                while contFilJ <= contHoras:
                    if(datosNoNaN.iloc[:, contColJ+2][contFilJ] != '0'):
                        jueves.append(datosNoNaN.iloc[1:, 0][contFilJ])
                        jueves.append(datosNoNaN.iloc[:, contColJ+2][contFilJ])
                        contFilJ+=1
                    else:
                        contFilJ+=1
            else:
                contColJ+=1;

        ##################################################################

        contFilV = 1
        contColV = 1
        viernes = []

        while contColV <= contDias:
            if(datosNoNaN.iloc[1:, 0][contColV] != '0'):
                contColV+=1
                while contFilV <= contHoras:
                    if(datosNoNaN.iloc[:, contColV+3][contFilV] != '0'):
                        viernes.append(datosNoNaN.iloc[1:, 0][contFilV])
                        viernes.append(datosNoNaN.iloc[:, contColV+3][contFilV])
                        contFilV+=1
                    else:
                        contFilV+=1
            else:
                contColV+=1;


if __name__ == '__main__':
    extractDataTeable1_1A1C_1A2C()
