#!/usr/bin/env python
# -*- coding: utf-8 -*-

import camelot
import csv
import os
import pandas as pd
import sys

RESOURCE = './resources'
OUTPUT = './outputs'

def extractDataTable1_1A1C_1A2C(cuatrimestre, dia):
    tablas = camelot.read_pdf(os.path.join(
        RESOURCE, 'HORARIOS1819.pdf'), pages='1')
    tablas.export(os.path.join(
        OUTPUT, './HORARIOS/HORARIOS1819.csv'), f='csv', compress=False)

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

        listLunes = []
        for x in lunes:
            listLunes.extend(x.strip().split('\n'))

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

        listMartes = []
        for x in martes:
            listMartes.extend(x.strip().split('\n'))

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

        listMiercoles = []
        for x in miercoles:
            listMiercoles.extend(x.strip().split('\n'))

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

        listJueves = []
        for x in jueves:
            listJueves.extend(x.strip().split('\n'))

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

        listViernes = []
        for x in viernes:
            listViernes.extend(x.strip().split('\n'))

        if(cuatrimestre == '1'):
            if(dia.lower() == 'lunes'):
                print(listLunes)
            if(dia.lower() == 'martes'):
                print(listMartes)
            if(dia.lower() == 'miercoles'):
                print(listMiercoles)
            if(dia.lower() == 'jueves'):
                print(listJueves)
            if(dia.lower() == 'viernes'):
                print(listViernes)
        
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

        listLunes = []
        for x in lunes:
            listLunes.extend(x.strip().split('\n'))

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
            
        listMartes = []
        for x in martes:
            listMartes.extend(x.strip().split('\n'))

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

        listMiercoles = []
        for x in miercoles:
            listMiercoles.extend(x.strip().split('\n'))

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

        listJueves = []
        for x in jueves:
            listJueves.extend(x.strip().split('\n'))

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

        listViernes = []
        for x in viernes:
            listViernes.extend(x.strip().split('\n'))

        if(cuatrimestre == '2'):
            if(dia.lower() == 'lunes'):
                print(listLunes)
            if(dia.lower() == 'martes'):
                print(listMartes)
            if(dia.lower() == 'miercoles'):
                print(listMiercoles)
            if(dia.lower() == 'jueves'):
                print(listJueves)
            if(dia.lower() == 'viernes'):
                print(listViernes)

def extractDataTable1_1B1C_1B2C():
    tablas = camelot.read_pdf(os.path.join(
        RESOURCE, 'HORARIOS1819.pdf'), pages='2')
    tablas.export(os.path.join(
        OUTPUT, './HORARIOS/HORARIOS1819.csv'), f='csv', compress=False)

    with open(os.path.join(OUTPUT, './HORARIOS/HORARIOS1819-page-2-table-1.csv'), 'r') as archivo:
        datos = pd.read_csv(archivo, header=0)
        datosNoNaN = datos.fillna(value='0')

        contDias = datosNoNaN.iloc[0, :].count()-1;
        contHoras = datosNoNaN.iloc[1:, 0].count()
        hora = datosNoNaN.iloc[1:, 0][1]
        contFilL = 1
        contColL = 1
        lunes = []

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
        
    with open(os.path.join(OUTPUT, './HORARIOS/HORARIOS1819-page-2-table-2.csv'), 'r') as archivo:
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

def extractDataTable1_1C1C_1C2C():
    tablas = camelot.read_pdf(os.path.join(
        RESOURCE, 'HORARIOS1819.pdf'), pages='3')
    tablas.export(os.path.join(
        OUTPUT, './HORARIOS/HORARIOS1819.csv'), f='csv', compress=False)

    with open(os.path.join(OUTPUT, './HORARIOS/HORARIOS1819-page-3-table-1.csv'), 'r') as archivo:
        datos = pd.read_csv(archivo, header=0)
        datosNoNaN = datos.fillna(value='0')

        contDias = datosNoNaN.iloc[0, :].count()-1;
        contHoras = datosNoNaN.iloc[1:, 0].count()
        hora = datosNoNaN.iloc[1:, 0][1]
        contFilL = 1
        contColL = 1
        lunes = []

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
        
    with open(os.path.join(OUTPUT, './HORARIOS/HORARIOS1819-page-3-table-2.csv'), 'r') as archivo:
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

def extractDataTable1_1D1C_1D2C():
    tablas = camelot.read_pdf(os.path.join(
        RESOURCE, 'HORARIOS1819.pdf'), pages='4')
    tablas.export(os.path.join(
        OUTPUT, './HORARIOS/HORARIOS1819.csv'), f='csv', compress=False)

    with open(os.path.join(OUTPUT, './HORARIOS/HORARIOS1819-page-4-table-1.csv'), 'r') as archivo:
        datos = pd.read_csv(archivo, header=0)
        datosNoNaN = datos.fillna(value='0')

        contDias = datosNoNaN.iloc[0, :].count()-1;
        contHoras = datosNoNaN.iloc[1:, 0].count()
        hora = datosNoNaN.iloc[1:, 0][1]
        contFilL = 1
        contColL = 1
        lunes = []

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
        
    with open(os.path.join(OUTPUT, './HORARIOS/HORARIOS1819-page-4-table-2.csv'), 'r') as archivo:
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

def extractDataTable1_1E1C_1E2C():
    tablas = camelot.read_pdf(os.path.join(
        RESOURCE, 'HORARIOS1819.pdf'), pages='5')
    tablas.export(os.path.join(
        OUTPUT, './HORARIOS/HORARIOS1819.csv'), f='csv', compress=False)

    with open(os.path.join(OUTPUT, './HORARIOS/HORARIOS1819-page-5-table-1.csv'), 'r') as archivo:
        datos = pd.read_csv(archivo, header=0)
        datosNoNaN = datos.fillna(value='0')

        contDias = datosNoNaN.iloc[0, :].count()-1;
        contHoras = datosNoNaN.iloc[1:, 0].count()
        hora = datosNoNaN.iloc[1:, 0][1]
        contFilL = 1
        contColL = 1
        lunes = []

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
        
    with open(os.path.join(OUTPUT, './HORARIOS/HORARIOS1819-page-5-table-2.csv'), 'r') as archivo:
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

def extractDataTable1_1F1C_1F2C():
    tablas = camelot.read_pdf(os.path.join(
        RESOURCE, 'HORARIOS1819.pdf'), pages='6')
    tablas.export(os.path.join(
        OUTPUT, './HORARIOS/HORARIOS1819.csv'), f='csv', compress=False)

    with open(os.path.join(OUTPUT, './HORARIOS/HORARIOS1819-page-6-table-1.csv'), 'r') as archivo:
        datos = pd.read_csv(archivo, header=0)
        datosNoNaN = datos.fillna(value='0')

        contDias = datosNoNaN.iloc[0, :].count()-1;
        contHoras = datosNoNaN.iloc[1:, 0].count()
        hora = datosNoNaN.iloc[1:, 0][1]
        contFilL = 1
        contColL = 1
        lunes = []

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
        
    with open(os.path.join(OUTPUT, './HORARIOS/HORARIOS1819-page-6-table-2.csv'), 'r') as archivo:
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

def extractDataTable1_2A1C_2A2C():
    tablas = camelot.read_pdf(os.path.join(
        RESOURCE, 'HORARIOS1819.pdf'), pages='7')
    tablas.export(os.path.join(
        OUTPUT, './HORARIOS/HORARIOS1819.csv'), f='csv', compress=False)

    with open(os.path.join(OUTPUT, './HORARIOS/HORARIOS1819-page-7-table-1.csv'), 'r') as archivo:
        datos = pd.read_csv(archivo, header=0)
        datosNoNaN = datos.fillna(value='0')

        contDias = datosNoNaN.iloc[0, :].count()-1;
        contHoras = datosNoNaN.iloc[1:, 0].count()
        hora = datosNoNaN.iloc[1:, 0][1]
        contFilL = 1
        contColL = 1
        lunes = []

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
        
    with open(os.path.join(OUTPUT, './HORARIOS/HORARIOS1819-page-7-table-2.csv'), 'r') as archivo:
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

def extractDataTable1_2B1C_2B2C():
    tablas = camelot.read_pdf(os.path.join(
        RESOURCE, 'HORARIOS1819.pdf'), pages='8')
    tablas.export(os.path.join(
        OUTPUT, './HORARIOS/HORARIOS1819.csv'), f='csv', compress=False)

    with open(os.path.join(OUTPUT, './HORARIOS/HORARIOS1819-page-8-table-1.csv'), 'r') as archivo:
        datos = pd.read_csv(archivo, header=0)
        datosNoNaN = datos.fillna(value='0')

        contDias = datosNoNaN.iloc[0, :].count()-1;
        contHoras = datosNoNaN.iloc[1:, 0].count()
        hora = datosNoNaN.iloc[1:, 0][1]
        contFilL = 1
        contColL = 1
        lunes = []

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
        
    with open(os.path.join(OUTPUT, './HORARIOS/HORARIOS1819-page-8-table-2.csv'), 'r') as archivo:
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

def extractDataTable1_2C1C_2C2C():
    tablas = camelot.read_pdf(os.path.join(
        RESOURCE, 'HORARIOS1819.pdf'), pages='9')
    tablas.export(os.path.join(
        OUTPUT, './HORARIOS/HORARIOS1819.csv'), f='csv', compress=False)

    with open(os.path.join(OUTPUT, './HORARIOS/HORARIOS1819-page-9-table-1.csv'), 'r') as archivo:
        datos = pd.read_csv(archivo, header=0)
        datosNoNaN = datos.fillna(value='0')

        contDias = datosNoNaN.iloc[0, :].count()-1;
        contHoras = datosNoNaN.iloc[1:, 0].count()
        hora = datosNoNaN.iloc[1:, 0][1]
        contFilL = 1
        contColL = 1
        lunes = []

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
        
    with open(os.path.join(OUTPUT, './HORARIOS/HORARIOS1819-page-9-table-2.csv'), 'r') as archivo:
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

def extractDataTable1_2D1C_2D2C():
    tablas = camelot.read_pdf(os.path.join(
        RESOURCE, 'HORARIOS1819.pdf'), pages='10')
    tablas.export(os.path.join(
        OUTPUT, './HORARIOS/HORARIOS1819.csv'), f='csv', compress=False)

    with open(os.path.join(OUTPUT, './HORARIOS/HORARIOS1819-page-10-table-1.csv'), 'r') as archivo:
        datos = pd.read_csv(archivo, header=0)
        datosNoNaN = datos.fillna(value='0')

        contDias = datosNoNaN.iloc[0, :].count()-1;
        contHoras = datosNoNaN.iloc[1:, 0].count()
        hora = datosNoNaN.iloc[1:, 0][1]
        contFilL = 1
        contColL = 1
        lunes = []

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
        
    with open(os.path.join(OUTPUT, './HORARIOS/HORARIOS1819-page-10-table-2.csv'), 'r') as archivo:
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

def extractDataTable1_3A1C():
    tablas = camelot.read_pdf(os.path.join(
        RESOURCE, 'HORARIOS1819.pdf'), pages='11')
    tablas.export(os.path.join(
        OUTPUT, './HORARIOS/HORARIOS1819.csv'), f='csv', compress=False)

    with open(os.path.join(OUTPUT, './HORARIOS/HORARIOS1819-page-11-table-1.csv'), 'r') as archivo:
        datos = pd.read_csv(archivo, header=0)
        datosNoNaN = datos.fillna(value='0')

        contDias = datosNoNaN.iloc[0, :].count()-1;
        contHoras = datosNoNaN.iloc[1:, 0].count()
        hora = datosNoNaN.iloc[1:, 0][1]
        contFilL = 1
        contColL = 1
        lunes = []

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

def extractDataTable1_3B1C():
    tablas = camelot.read_pdf(os.path.join(
        RESOURCE, 'HORARIOS1819.pdf'), pages='12')
    tablas.export(os.path.join(
        OUTPUT, './HORARIOS/HORARIOS1819.csv'), f='csv', compress=False)

    with open(os.path.join(OUTPUT, './HORARIOS/HORARIOS1819-page-12-table-1.csv'), 'r') as archivo:
        datos = pd.read_csv(archivo, header=0)
        datosNoNaN = datos.fillna(value='0')

        contDias = datosNoNaN.iloc[0, :].count()-1;
        contHoras = datosNoNaN.iloc[1:, 0].count()
        hora = datosNoNaN.iloc[1:, 0][1]
        contFilL = 1
        contColL = 1
        lunes = []

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
            
def extractDataTable1_3C1C():
    tablas = camelot.read_pdf(os.path.join(
        RESOURCE, 'HORARIOS1819.pdf'), pages='13')
    tablas.export(os.path.join(
        OUTPUT, './HORARIOS/HORARIOS1819.csv'), f='csv', compress=False)

    with open(os.path.join(OUTPUT, './HORARIOS/HORARIOS1819-page-13-table-1.csv'), 'r') as archivo:
        datos = pd.read_csv(archivo, header=0)
        datosNoNaN = datos.fillna(value='0')

        contDias = datosNoNaN.iloc[0, :].count()-1;
        contHoras = datosNoNaN.iloc[1:, 0].count()
        hora = datosNoNaN.iloc[1:, 0][1]
        contFilL = 1
        contColL = 1
        lunes = []

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
     
def extractDataTable1_3C_Computadores():
    tablas = camelot.read_pdf(os.path.join(
        RESOURCE, 'HORARIOS1819.pdf'), pages='14')
    tablas.export(os.path.join(
        OUTPUT, './HORARIOS/HORARIOS1819.csv'), f='csv', compress=False)

    with open(os.path.join(OUTPUT, './HORARIOS/HORARIOS1819-page-14-table-1.csv'), 'r') as archivo:
        datos = pd.read_csv(archivo, header=0)
        datosNoNaN = datos.fillna(value='0')

        contDias = datosNoNaN.iloc[0, :].count()-1;
        contHoras = datosNoNaN.iloc[1:, 0].count()
        hora = datosNoNaN.iloc[1:, 0][1]
        contFilL = 1
        contColL = 1
        lunes = []

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
 
def extractDataTable1_3C_Software():
    tablas = camelot.read_pdf(os.path.join(
        RESOURCE, 'HORARIOS1819.pdf'), pages='15')
    tablas.export(os.path.join(
        OUTPUT, './HORARIOS/HORARIOS1819.csv'), f='csv', compress=False)

    with open(os.path.join(OUTPUT, './HORARIOS/HORARIOS1819-page-15-table-1.csv'), 'r') as archivo:
        datos = pd.read_csv(archivo, header=0)
        datosNoNaN = datos.fillna(value='0')

        contDias = datosNoNaN.iloc[0, :].count()-1;
        contHoras = datosNoNaN.iloc[1:, 0].count()
        hora = datosNoNaN.iloc[1:, 0][1]
        contFilL = 1
        contColL = 1
        lunes = []

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
 
def extractDataTable1_3C_Computacion_SistemasInteligentes():
    tablas = camelot.read_pdf(os.path.join(
        RESOURCE, 'HORARIOS1819.pdf'), pages='16')
    tablas.export(os.path.join(
        OUTPUT, './HORARIOS/HORARIOS1819.csv'), f='csv', compress=False)

    with open(os.path.join(OUTPUT, './HORARIOS/HORARIOS1819-page-16-table-1.csv'), 'r') as archivo:
        datos = pd.read_csv(archivo, header=0)
        datosNoNaN = datos.fillna(value='0')

        contDias = datosNoNaN.iloc[0, :].count()-1;
        contHoras = datosNoNaN.iloc[1:, 0].count()
        hora = datosNoNaN.iloc[1:, 0][1]
        contFilL = 1
        contColL = 1
        lunes = []

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
 
def extractDataTable1_3C_SistemasInformacion():
    tablas = camelot.read_pdf(os.path.join(
        RESOURCE, 'HORARIOS1819.pdf'), pages='17')
    tablas.export(os.path.join(
        OUTPUT, './HORARIOS/HORARIOS1819.csv'), f='csv', compress=False)

    with open(os.path.join(OUTPUT, './HORARIOS/HORARIOS1819-page-17-table-1.csv'), 'r') as archivo:
        datos = pd.read_csv(archivo, header=0)
        datosNoNaN = datos.fillna(value='0')

        contDias = datosNoNaN.iloc[0, :].count()-1;
        contHoras = datosNoNaN.iloc[1:, 0].count()
        hora = datosNoNaN.iloc[1:, 0][1]
        contFilL = 1
        contColL = 1
        lunes = []

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
 
def extractDataTable1_3C_TecnologiasInformacion():
    tablas = camelot.read_pdf(os.path.join(
        RESOURCE, 'HORARIOS1819.pdf'), pages='18')
    tablas.export(os.path.join(
        OUTPUT, './HORARIOS/HORARIOS1819.csv'), f='csv', compress=False)

    with open(os.path.join(OUTPUT, './HORARIOS/HORARIOS1819-page-18-table-1.csv'), 'r') as archivo:
        datos = pd.read_csv(archivo, header=0)
        datosNoNaN = datos.fillna(value='0')

        contDias = datosNoNaN.iloc[0, :].count()-1;
        contHoras = datosNoNaN.iloc[1:, 0].count()
        hora = datosNoNaN.iloc[1:, 0][1]
        contFilL = 1
        contColL = 1
        lunes = []

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
 
def extractDataTable1_4C_1C_2C_Computadores():
    tablas = camelot.read_pdf(os.path.join(
        RESOURCE, 'HORARIOS1819.pdf'), pages='19')
    tablas.export(os.path.join(
        OUTPUT, './HORARIOS/HORARIOS1819.csv'), f='csv', compress=False)

    with open(os.path.join(OUTPUT, './HORARIOS/HORARIOS1819-page-19-table-1.csv'), 'r') as archivo:
        datos = pd.read_csv(archivo, header=0)
        datosNoNaN = datos.fillna(value='0')

        contDias = datosNoNaN.iloc[0, :].count()-1;
        contHoras = datosNoNaN.iloc[1:, 0].count()
        hora = datosNoNaN.iloc[1:, 0][1]
        contFilL = 1
        contColL = 1
        lunes = []

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
        
    with open(os.path.join(OUTPUT, './HORARIOS/HORARIOS1819-page-19-table-2.csv'), 'r') as archivo:
        datos = pd.read_csv(archivo, header=0)
        datosNoNaN = datos.fillna(value='0')

        contDias = datosNoNaN.iloc[0, :].count()-1;
        contHoras = datosNoNaN.iloc[1:, 0].count()
        hora = datosNoNaN.iloc[1:, 0][1]
        contFilL = 1
        contColL = 1
        lunes = []

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

def extractDataTable1_4C_1C_2C_Software():
    tablas = camelot.read_pdf(os.path.join(
        RESOURCE, 'HORARIOS1819.pdf'), pages='20')
    tablas.export(os.path.join(
        OUTPUT, './HORARIOS/HORARIOS1819.csv'), f='csv', compress=False)

    with open(os.path.join(OUTPUT, './HORARIOS/HORARIOS1819-page-20-table-1.csv'), 'r') as archivo:
        datos = pd.read_csv(archivo, header=0)
        datosNoNaN = datos.fillna(value='0')

        contDias = datosNoNaN.iloc[0, :].count()-1;
        contHoras = datosNoNaN.iloc[1:, 0].count()
        hora = datosNoNaN.iloc[1:, 0][1]
        contFilL = 1
        contColL = 1
        lunes = []

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
        
    with open(os.path.join(OUTPUT, './HORARIOS/HORARIOS1819-page-20-table-2.csv'), 'r') as archivo:
        datos = pd.read_csv(archivo, header=0)
        datosNoNaN = datos.fillna(value='0')

        contDias = datosNoNaN.iloc[0, :].count()-1;
        contHoras = datosNoNaN.iloc[1:, 0].count()
        hora = datosNoNaN.iloc[1:, 0][1]
        contFilL = 1
        contColL = 1
        lunes = []

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

def extractDataTable1_4C_1C_2C_Computacion_SistemasInteligentes():
    tablas = camelot.read_pdf(os.path.join(
        RESOURCE, 'HORARIOS1819.pdf'), pages='21')
    tablas.export(os.path.join(
        OUTPUT, './HORARIOS/HORARIOS1819.csv'), f='csv', compress=False)

    with open(os.path.join(OUTPUT, './HORARIOS/HORARIOS1819-page-21-table-1.csv'), 'r') as archivo:
        datos = pd.read_csv(archivo, header=0)
        datosNoNaN = datos.fillna(value='0')

        contDias = datosNoNaN.iloc[0, :].count()-1;
        contHoras = datosNoNaN.iloc[1:, 0].count()
        hora = datosNoNaN.iloc[1:, 0][1]
        contFilL = 1
        contColL = 1
        lunes = []

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
        
    with open(os.path.join(OUTPUT, './HORARIOS/HORARIOS1819-page-21-table-2.csv'), 'r') as archivo:
        datos = pd.read_csv(archivo, header=0)
        datosNoNaN = datos.fillna(value='0')

        contDias = datosNoNaN.iloc[0, :].count()-1;
        contHoras = datosNoNaN.iloc[1:, 0].count()
        hora = datosNoNaN.iloc[1:, 0][1]
        contFilL = 1
        contColL = 1
        lunes = []

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

def extractDataTable1_4C_1C_2C_SistemasInformacion():
    tablas = camelot.read_pdf(os.path.join(
        RESOURCE, 'HORARIOS1819.pdf'), pages='22')
    tablas.export(os.path.join(
        OUTPUT, './HORARIOS/HORARIOS1819.csv'), f='csv', compress=False)

    with open(os.path.join(OUTPUT, './HORARIOS/HORARIOS1819-page-22-table-1.csv'), 'r') as archivo:
        datos = pd.read_csv(archivo, header=0)
        datosNoNaN = datos.fillna(value='0')

        contDias = datosNoNaN.iloc[0, :].count()-1;
        contHoras = datosNoNaN.iloc[1:, 0].count()
        hora = datosNoNaN.iloc[1:, 0][1]
        contFilL = 1
        contColL = 1
        lunes = []

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
        
    with open(os.path.join(OUTPUT, './HORARIOS/HORARIOS1819-page-22-table-2.csv'), 'r') as archivo:
        datos = pd.read_csv(archivo, header=0)
        datosNoNaN = datos.fillna(value='0')

        contDias = datosNoNaN.iloc[0, :].count()-1;
        contHoras = datosNoNaN.iloc[1:, 0].count()
        hora = datosNoNaN.iloc[1:, 0][1]
        contFilL = 1
        contColL = 1
        lunes = []

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

def extractDataTable1_4C_1C_2C_TecnologiasInformacion():
    tablas = camelot.read_pdf(os.path.join(
        RESOURCE, 'HORARIOS1819.pdf'), pages='23')
    tablas.export(os.path.join(
        OUTPUT, './HORARIOS/HORARIOS1819.csv'), f='csv', compress=False)

    with open(os.path.join(OUTPUT, './HORARIOS/HORARIOS1819-page-23-table-1.csv'), 'r') as archivo:
        datos = pd.read_csv(archivo, header=0)
        datosNoNaN = datos.fillna(value='0')

        contDias = datosNoNaN.iloc[0, :].count()-1;
        contHoras = datosNoNaN.iloc[1:, 0].count()
        hora = datosNoNaN.iloc[1:, 0][1]
        contFilL = 1
        contColL = 1
        lunes = []

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
        
    with open(os.path.join(OUTPUT, './HORARIOS/HORARIOS1819-page-23-table-2.csv'), 'r') as archivo:
        datos = pd.read_csv(archivo, header=0)
        datosNoNaN = datos.fillna(value='0')

        contDias = datosNoNaN.iloc[0, :].count()-1;
        contHoras = datosNoNaN.iloc[1:, 0].count()
        hora = datosNoNaN.iloc[1:, 0][1]
        contFilL = 1
        contColL = 1
        lunes = []

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


if __name__ == '__main__':
    if(sys.argv[3:]):
        if(sys.argv[1] == '1'):
            cuatrimestre = sys.argv[2]
            dia = sys.argv[3]
            extractDataTable1_1A1C_1A2C(cuatrimestre, dia)
            # extractDataTable1_1B1C_1B2C()
            # extractDataTable1_1C1C_1C2C()
            # extractDataTable1_1D1C_1D2C()
            # extractDataTable1_1E1C_1E2C()
            # extractDataTable1_1F1C_1F2C()

            # extractDataTable1_2A1C_2A2C()
            # extractDataTable1_2B1C_2B2C()
            # extractDataTable1_2C1C_2C2C()
            # extractDataTable1_2D1C_2D2C()

            # extractDataTable1_3A1C()
            # extractDataTable1_3B1C()
            # extractDataTable1_3C1C()

            # extractDataTable1_3C_Computadores()
            # extractDataTable1_3C_Software()
            # extractDataTable1_3C_Computacion_SistemasInteligentes()
            # extractDataTable1_3C_SistemasInformacion()
            # extractDataTable1_3C_TecnologiasInformacion()

            # extractDataTable1_4C_1C_2C_Computadores()
            # extractDataTable1_4C_1C_2C_Software()
            # extractDataTable1_4C_1C_2C_Computacion_SistemasInteligentes()
            # extractDataTable1_4C_1C_2C_SistemasInformacion()
            # extractDataTable1_4C_1C_2C_TecnologiasInformacion()
    else:
        print("Error: indicar el curso, el cuatrimestre y el día")