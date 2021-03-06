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

        if(cuatrimestre == '1' or cuatrimestre == 'primero' or cuatrimestre == 'uno'):
            if(dia.lower() == 'lunes'):
                return listLunes
            if(dia.lower() == 'martes'):
                return listMartes
            if(dia.lower() == 'miercoles'):
                return listMiercoles
            if(dia.lower() == 'jueves'):
                return listJueves
            if(dia.lower() == 'viernes'):
                return listViernes
        
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

        if(cuatrimestre == '2' or cuatrimestre == 'segundo' or cuatrimestre == 'dos'):
            if(dia.lower() == 'lunes'):
                return listLunes
            if(dia.lower() == 'martes'):
                return listMartes
            if(dia.lower() == 'miercoles'):
                return listMiercoles
            if(dia.lower() == 'jueves'):
                return listJueves
            if(dia.lower() == 'viernes'):
                return listViernes

def extractDataTable1_1B1C_1B2C(cuatrimestre, dia):
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

        if(cuatrimestre == '1' or cuatrimestre == 'primero' or cuatrimestre == 'uno'):
            if(dia.lower() == 'lunes'):
                return listLunes
            if(dia.lower() == 'martes'):
                return listMartes
            if(dia.lower() == 'miercoles'):
                return listMiercoles
            if(dia.lower() == 'jueves'):
                return listJueves
            if(dia.lower() == 'viernes'):
                return listViernes        
        
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

        if(cuatrimestre == '2' or cuatrimestre == 'segundo' or cuatrimestre == 'dos'):
            if(dia.lower() == 'lunes'):
                return listLunes
            if(dia.lower() == 'martes'):
                return listMartes
            if(dia.lower() == 'miercoles'):
                return listMiercoles
            if(dia.lower() == 'jueves'):
                return listJueves
            if(dia.lower() == 'viernes'):
                return listViernes

def extractDataTable1_1C1C_1C2C(cuatrimestre, dia):
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

        if(cuatrimestre == '1' or cuatrimestre == 'primero' or cuatrimestre == 'uno'):
            if(dia.lower() == 'lunes'):
                return listLunes
            if(dia.lower() == 'martes'):
                return listMartes
            if(dia.lower() == 'miercoles'):
                return listMiercoles
            if(dia.lower() == 'jueves'):
                return listJueves
            if(dia.lower() == 'viernes'):
                return listViernes
        
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

        if(cuatrimestre == '2' or cuatrimestre == 'segundo' or cuatrimestre == 'dos'):
            if(dia.lower() == 'lunes'):
                return listLunes
            if(dia.lower() == 'martes'):
                return listMartes
            if(dia.lower() == 'miercoles'):
                return listMiercoles
            if(dia.lower() == 'jueves'):
                return listJueves
            if(dia.lower() == 'viernes'):
                return listViernes

def extractDataTable1_1D1C_1D2C(cuatrimestre, dia):
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

        if(cuatrimestre == '1' or cuatrimestre == 'primero' or cuatrimestre == 'uno'):
            if(dia.lower() == 'lunes'):
                return listLunes
            if(dia.lower() == 'martes'):
                return listMartes
            if(dia.lower() == 'miercoles'):
                return listMiercoles
            if(dia.lower() == 'jueves'):
                return listJueves
            if(dia.lower() == 'viernes'):
                return listViernes
        
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

        if(cuatrimestre == '2' or cuatrimestre == 'segundo' or cuatrimestre == 'dos'):
            if(dia.lower() == 'lunes'):
                return listLunes
            if(dia.lower() == 'martes'):
                return listMartes
            if(dia.lower() == 'miercoles'):
                return listMiercoles
            if(dia.lower() == 'jueves'):
                return listJueves
            if(dia.lower() == 'viernes'):
                return listViernes

def extractDataTable1_1E1C_1E2C(cuatrimestre, dia):
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

        if(cuatrimestre == '1' or cuatrimestre == 'primero' or cuatrimestre == 'uno'):
            if(dia.lower() == 'lunes'):
                return listLunes
            if(dia.lower() == 'martes'):
                return listMartes
            if(dia.lower() == 'miercoles'):
                return listMiercoles
            if(dia.lower() == 'jueves'):
                return listJueves
            if(dia.lower() == 'viernes'):
                return listViernes
        
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

        if(cuatrimestre == '2' or cuatrimestre == 'segundo' or cuatrimestre == 'dos'):
            if(dia.lower() == 'lunes'):
                return listLunes
            if(dia.lower() == 'martes'):
                return listMartes
            if(dia.lower() == 'miercoles'):
                return listMiercoles
            if(dia.lower() == 'jueves'):
                return listJueves
            if(dia.lower() == 'viernes'):
                return listViernes

def extractDataTable1_1F1C_1F2C(cuatrimestre, dia):
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

        if(cuatrimestre == '1' or cuatrimestre == 'primero' or cuatrimestre == 'uno'):
            if(dia.lower() == 'lunes'):
                return listLunes
            if(dia.lower() == 'martes'):
                return listMartes
            if(dia.lower() == 'miercoles'):
                return listMiercoles
            if(dia.lower() == 'jueves'):
                return listJueves
            if(dia.lower() == 'viernes'):
                return listViernes

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

        if(cuatrimestre == '2' or cuatrimestre == 'segundo' or cuatrimestre == 'dos'):
            if(dia.lower() == 'lunes'):
                return listLunes
            if(dia.lower() == 'martes'):
                return listMartes
            if(dia.lower() == 'miercoles'):
                return listMiercoles
            if(dia.lower() == 'jueves'):
                return listJueves
            if(dia.lower() == 'viernes'):
                return listViernes

def extractDataTable1_2A1C_2A2C(cuatrimestre, dia):
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

        if(cuatrimestre == '1' or cuatrimestre == 'primero' or cuatrimestre == 'uno'):
            if(dia.lower() == 'lunes'):
                return listLunes
            if(dia.lower() == 'martes'):
                return listMartes
            if(dia.lower() == 'miercoles'):
                return listMiercoles
            if(dia.lower() == 'jueves'):
                return listJueves
            if(dia.lower() == 'viernes'):
                return listViernes
        
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

        if(cuatrimestre == '2' or cuatrimestre == 'segundo' or cuatrimestre == 'dos'):
            if(dia.lower() == 'lunes'):
                return listLunes
            if(dia.lower() == 'martes'):
                return listMartes
            if(dia.lower() == 'miercoles'):
                return listMiercoles
            if(dia.lower() == 'jueves'):
                return listJueves
            if(dia.lower() == 'viernes'):
                return listViernes

def extractDataTable1_2B1C_2B2C(cuatrimestre, dia):
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

        if(cuatrimestre == '1' or cuatrimestre == 'primero' or cuatrimestre == 'uno'):
            if(dia.lower() == 'lunes'):
                return listLunes
            if(dia.lower() == 'martes'):
                return listMartes
            if(dia.lower() == 'miercoles'):
                return listMiercoles
            if(dia.lower() == 'jueves'):
                return listJueves
            if(dia.lower() == 'viernes'):
                return listViernes
        
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

        if(cuatrimestre == '2' or cuatrimestre == 'segundo' or cuatrimestre == 'dos'):
            if(dia.lower() == 'lunes'):
                return listLunes
            if(dia.lower() == 'martes'):
                return listMartes
            if(dia.lower() == 'miercoles'):
                return listMiercoles
            if(dia.lower() == 'jueves'):
                return listJueves
            if(dia.lower() == 'viernes'):
                return listViernes

def extractDataTable1_2C1C_2C2C(cuatrimestre, dia):
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

        if(cuatrimestre == '1' or cuatrimestre == 'primero' or cuatrimestre == 'uno'):
            if(dia.lower() == 'lunes'):
                return listLunes
            if(dia.lower() == 'martes'):
                return listMartes
            if(dia.lower() == 'miercoles'):
                return listMiercoles
            if(dia.lower() == 'jueves'):
                return listJueves
            if(dia.lower() == 'viernes'):
                return listViernes
        
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

        if(cuatrimestre == '2' or cuatrimestre == 'segundo' or cuatrimestre == 'dos'):
            if(dia.lower() == 'lunes'):
                return listLunes
            if(dia.lower() == 'martes'):
                return listMartes
            if(dia.lower() == 'miercoles'):
                return listMiercoles
            if(dia.lower() == 'jueves'):
                return listJueves
            if(dia.lower() == 'viernes'):
                return listViernes

def extractDataTable1_2D1C_2D2C(cuatrimestre, dia):
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

        if(cuatrimestre == '1' or cuatrimestre == 'primero' or cuatrimestre == 'uno'):
            if(dia.lower() == 'lunes'):
                return listLunes
            if(dia.lower() == 'martes'):
                return listMartes
            if(dia.lower() == 'miercoles'):
                return listMiercoles
            if(dia.lower() == 'jueves'):
                return listJueves
            if(dia.lower() == 'viernes'):
                return listViernes
        
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

        if(cuatrimestre == '2' or cuatrimestre == 'segundo' or cuatrimestre == 'dos'):
            if(dia.lower() == 'lunes'):
                return listLunes
            if(dia.lower() == 'martes'):
                return listMartes
            if(dia.lower() == 'miercoles'):
                return listMiercoles
            if(dia.lower() == 'jueves'):
                return listJueves
            if(dia.lower() == 'viernes'):
                return listViernes

def extractDataTable1_3A1C(dia):
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
        
        if(cuatrimestre == '1' or cuatrimestre == 'primero' or cuatrimestre == 'uno'):
            if(dia.lower() == 'lunes'):
                return listLunes
            if(dia.lower() == 'martes'):
                return listMartes
            if(dia.lower() == 'miercoles'):
                return listMiercoles
            if(dia.lower() == 'jueves'):
                return listJueves
            if(dia.lower() == 'viernes'):
                return listViernes

def extractDataTable1_3B1C(dia):
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
        
        if(cuatrimestre == '1' or cuatrimestre == 'primero' or cuatrimestre == 'uno'):
            if(dia.lower() == 'lunes'):
                return listLunes
            if(dia.lower() == 'martes'):
                return listMartes
            if(dia.lower() == 'miercoles'):
                return listMiercoles
            if(dia.lower() == 'jueves'):
                return listJueves
            if(dia.lower() == 'viernes'):
                return listViernes
            
def extractDataTable1_3C1C(dia):
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
        
        if(cuatrimestre == '1' or cuatrimestre == 'primero' or cuatrimestre == 'uno'):
            if(dia.lower() == 'lunes'):
                return listLunes
            if(dia.lower() == 'martes'):
                return listMartes
            if(dia.lower() == 'miercoles'):
                return listMiercoles
            if(dia.lower() == 'jueves'):
                return listJueves
            if(dia.lower() == 'viernes'):
                return listViernes
     
def extractDataTable1_3C_Computadores(dia):
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
        
        if(dia.lower() == 'lunes'):
            return listLunes
        if(dia.lower() == 'martes'):
            return listMartes
        if(dia.lower() == 'miercoles'):
            return listMiercoles
        if(dia.lower() == 'jueves'):
            return listJueves
        if(dia.lower() == 'viernes'):
            return listViernes
 
def extractDataTable1_3C_Software(dia):
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
        
        if(dia.lower() == 'lunes'):
            return listLunes
        if(dia.lower() == 'martes'):
            return listMartes
        if(dia.lower() == 'miercoles'):
            return listMiercoles
        if(dia.lower() == 'jueves'):
            return listJueves
        if(dia.lower() == 'viernes'):
            return listViernes
 
def extractDataTable1_3C_Computacion_SistemasInteligentes(dia):
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
        
        if(dia.lower() == 'lunes'):
            return listLunes
        if(dia.lower() == 'martes'):
            return listMartes
        if(dia.lower() == 'miercoles'):
            return listMiercoles
        if(dia.lower() == 'jueves'):
            return listJueves
        if(dia.lower() == 'viernes'):
            return listViernes

def extractDataTable1_3C_SistemasInformacion(dia):
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
        
        if(dia.lower() == 'lunes'):
            return listLunes
        if(dia.lower() == 'martes'):
            return listMartes
        if(dia.lower() == 'miercoles'):
            return listMiercoles
        if(dia.lower() == 'jueves'):
            return listJueves
        if(dia.lower() == 'viernes'):
            return listViernes
 
def extractDataTable1_3C_TecnologiasInformacion(dia):
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
        
        if(dia.lower() == 'lunes'):
            return listLunes
        if(dia.lower() == 'martes'):
            return listMartes
        if(dia.lower() == 'miercoles'):
            return listMiercoles
        if(dia.lower() == 'jueves'):
            return listJueves
        if(dia.lower() == 'viernes'):
            return listViernes
 
def extractDataTable1_4C_1C_2C_Computadores(cuatrimestre, dia):
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

        if(cuatrimestre == '1' or cuatrimestre == 'primero' or cuatrimestre == 'uno'):
            if(dia.lower() == 'lunes'):
                return listLunes
            if(dia.lower() == 'martes'):
                return listMartes
            if(dia.lower() == 'miercoles'):
                return listMiercoles
            if(dia.lower() == 'jueves'):
                return listJueves
            if(dia.lower() == 'viernes'):
                return listViernes
        
    with open(os.path.join(OUTPUT, './HORARIOS/HORARIOS1819-page-19-table-2.csv'), 'r') as archivo:
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

        if(cuatrimestre == '2' or cuatrimestre == 'segundo' or cuatrimestre == 'dos'):
            if(dia.lower() == 'lunes'):
                return listLunes
            if(dia.lower() == 'martes'):
                return listMartes
            if(dia.lower() == 'miercoles'):
                return listMiercoles
            if(dia.lower() == 'jueves'):
                return listJueves
            if(dia.lower() == 'viernes'):
                return listViernes

def extractDataTable1_4C_1C_2C_Software(cuatrimestre, dia):
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

        if(cuatrimestre == '1' or cuatrimestre == 'primero' or cuatrimestre == 'uno'):
            if(dia.lower() == 'lunes'):
                return listLunes
            if(dia.lower() == 'martes'):
                return listMartes
            if(dia.lower() == 'miercoles'):
                return listMiercoles
            if(dia.lower() == 'jueves'):
                return listJueves
            if(dia.lower() == 'viernes'):
                return listViernes
        
    with open(os.path.join(OUTPUT, './HORARIOS/HORARIOS1819-page-20-table-2.csv'), 'r') as archivo:
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

        if(cuatrimestre == '2' or cuatrimestre == 'segundo' or cuatrimestre == 'dos'):
            if(dia.lower() == 'lunes'):
                return listLunes
            if(dia.lower() == 'martes'):
                return listMartes
            if(dia.lower() == 'miercoles'):
                return listMiercoles
            if(dia.lower() == 'jueves'):
                return listJueves
            if(dia.lower() == 'viernes'):
                return listViernes

def extractDataTable1_4C_1C_2C_Computacion_SistemasInteligentes(cuatrimestre, dia):
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

        if(cuatrimestre == '1' or cuatrimestre == 'primero' or cuatrimestre == 'uno'):
            if(dia.lower() == 'lunes'):
                return listLunes
            if(dia.lower() == 'martes'):
                return listMartes
            if(dia.lower() == 'miercoles'):
                return listMiercoles
            if(dia.lower() == 'jueves'):
                return listJueves
            if(dia.lower() == 'viernes'):
                return listViernes
        
    with open(os.path.join(OUTPUT, './HORARIOS/HORARIOS1819-page-21-table-2.csv'), 'r') as archivo:
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

        if(cuatrimestre == '2' or cuatrimestre == 'segundo' or cuatrimestre == 'dos'):
            if(dia.lower() == 'lunes'):
                return listLunes
            if(dia.lower() == 'martes'):
                return listMartes
            if(dia.lower() == 'miercoles'):
                return listMiercoles
            if(dia.lower() == 'jueves'):
                return listJueves
            if(dia.lower() == 'viernes'):
                return listViernes 

def extractDataTable1_4C_1C_2C_SistemasInformacion(cuatrimestre, dia):
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

        if(cuatrimestre == '1' or cuatrimestre == 'primero' or cuatrimestre == 'uno'):
            if(dia.lower() == 'lunes'):
                return listLunes
            if(dia.lower() == 'martes'):
                return listMartes
            if(dia.lower() == 'miercoles'):
                return listMiercoles
            if(dia.lower() == 'jueves'):
                return listJueves
            if(dia.lower() == 'viernes'):
                return listViernes
        
    with open(os.path.join(OUTPUT, './HORARIOS/HORARIOS1819-page-22-table-2.csv'), 'r') as archivo:
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

        if(cuatrimestre == '2' or cuatrimestre == 'segundo' or cuatrimestre == 'dos'):
            if(dia.lower() == 'lunes'):
                return listLunes
            if(dia.lower() == 'martes'):
                return listMartes
            if(dia.lower() == 'miercoles'):
                return listMiercoles
            if(dia.lower() == 'jueves'):
                return listJueves
            if(dia.lower() == 'viernes'):
                return listViernes 

def extractDataTable1_4C_1C_2C_TecnologiasInformacion(cuatrimestre, dia):
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

        if(cuatrimestre == '1' or cuatrimestre == 'primero' or cuatrimestre == 'uno'):
            if(dia.lower() == 'lunes'):
                return listLunes
            if(dia.lower() == 'martes'):
                return listMartes
            if(dia.lower() == 'miercoles'):
                return listMiercoles
            if(dia.lower() == 'jueves'):
                return listJueves
            if(dia.lower() == 'viernes'):
                return listViernes
        
    with open(os.path.join(OUTPUT, './HORARIOS/HORARIOS1819-page-23-table-2.csv'), 'r') as archivo:
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

        if(cuatrimestre == '2' or cuatrimestre == 'segundo' or cuatrimestre == 'dos'):
            if(dia.lower() == 'lunes'):
                return listLunes
            if(dia.lower() == 'martes'):
                return listMartes
            if(dia.lower() == 'miercoles'):
                return listMiercoles
            if(dia.lower() == 'jueves'):
                return listJueves
            if(dia.lower() == 'viernes'):
                return listViernes  


if __name__ == '__main__':
    if(sys.argv[4:]):
        cuatrimestre = sys.argv[3]
        dia = sys.argv[4].upper()
        especialidad = ''

        if((sys.argv[1] == '3' and cuatrimestre == '2') or sys.argv[1] == '4'):
            especialidad = sys.argv[5].upper()
        
        connect_db = psycopg2.connect(database=db, user=usuario, password=pw, host=host_db)
        cursor = connect_db.cursor()

        if(sys.argv[1] == '1' or sys.argv[1] == 'primero' or sys.argv[1] == 'uno'):
            if(sys.argv[2] == 'A' or sys.argv[2] == 'a'):
                if(cuatrimestre == '1' or cuatrimestre == 'primero' or cuatrimestre == 'primer'):
                    listDia = extractDataTable1_1A1C_1A2C(cuatrimestre, dia)

                    sql_insert_query = """INSERT INTO "Horarios" VALUES(%s, %s, %s, %s, %s)"""
                    insert_tuple = (1, 1, 'A', dia, listDia)
                    result = cursor.execute(sql_insert_query, insert_tuple)

                    connect_db.commit()
                    print("Fila insertada correctamente")

                if(cuatrimestre == '2' or cuatrimestre == 'segundo'):
                    listDia = extractDataTable1_1A1C_1A2C(cuatrimestre, dia)

                    sql_insert_query = """INSERT INTO "Horarios" VALUES(%s, %s, %s, %s, %s)"""
                    insert_tuple = (1, 2, 'A', dia, listDia)
                    result = cursor.execute(sql_insert_query, insert_tuple)

                    connect_db.commit()
                    print("Fila insertada correctamente")

            if(sys.argv[2] == 'B' or sys.argv[2] == 'b'):
                if(cuatrimestre == '1' or cuatrimestre == 'primero' or cuatrimestre == 'primer'):
                    listDia = extractDataTable1_1B1C_1B2C(cuatrimestre, dia)

                    sql_insert_query = """INSERT INTO "Horarios" VALUES(%s, %s, %s, %s, %s)"""
                    insert_tuple = (1, 1, 'B', dia, listDia)
                    result = cursor.execute(sql_insert_query, insert_tuple)

                    connect_db.commit()
                    print("Fila insertada correctamente")

                if(cuatrimestre == '2' or cuatrimestre == 'segundo'):
                    listDia = extractDataTable1_1B1C_1B2C(cuatrimestre, dia)

                    sql_insert_query = """INSERT INTO "Horarios" VALUES(%s, %s, %s, %s, %s)"""
                    insert_tuple = (1, 2, 'B', dia, listDia)
                    result = cursor.execute(sql_insert_query, insert_tuple)

                    connect_db.commit()
                    print("Fila insertada correctamente")

            if(sys.argv[2] == 'C' or sys.argv[2] == 'c'):
                if(cuatrimestre == '1' or cuatrimestre == 'primero' or cuatrimestre == 'primer'):
                    listDia = extractDataTable1_1C1C_1C2C(cuatrimestre, dia)

                    sql_insert_query = """INSERT INTO "Horarios" VALUES(%s, %s, %s, %s, %s)"""
                    insert_tuple = (1, 1, 'C', dia, listDia)
                    result = cursor.execute(sql_insert_query, insert_tuple)

                    connect_db.commit()
                    print("Fila insertada correctamente")

                if(cuatrimestre == '2' or cuatrimestre == 'segundo'):
                    listDia = extractDataTable1_1C1C_1C2C(cuatrimestre, dia)

                    sql_insert_query = """INSERT INTO "Horarios" VALUES(%s, %s, %s, %s, %s)"""
                    insert_tuple = (1, 2, 'C', dia, listDia)
                    result = cursor.execute(sql_insert_query, insert_tuple)

                    connect_db.commit()
                    print("Fila insertada correctamente")
            
            if(sys.argv[2] == 'D' or sys.argv[2] == 'd'):
                if(cuatrimestre == '1' or cuatrimestre == 'primero' or cuatrimestre == 'primer'):
                    listDia = extractDataTable1_1D1C_1D2C(cuatrimestre, dia)

                    sql_insert_query = """INSERT INTO "Horarios" VALUES(%s, %s, %s, %s, %s)"""
                    insert_tuple = (1, 1, 'D', dia, listDia)
                    result = cursor.execute(sql_insert_query, insert_tuple)

                    connect_db.commit()
                    print("Fila insertada correctamente")

                if(cuatrimestre == '2' or cuatrimestre == 'segundo'):
                    listDia = extractDataTable1_1D1C_1D2C(cuatrimestre, dia)

                    sql_insert_query = """INSERT INTO "Horarios" VALUES(%s, %s, %s, %s, %s)"""
                    insert_tuple = (1, 2, 'C', dia, listDia)
                    result = cursor.execute(sql_insert_query, insert_tuple)

                    connect_db.commit()
                    print("Fila insertada correctamente")
            
            if(sys.argv[2] == 'E' or sys.argv[2] == 'e'):
                if(cuatrimestre == '1' or cuatrimestre == 'primero' or cuatrimestre == 'primer'):
                    listDia = extractDataTable1_1E1C_1E2C(cuatrimestre, dia)

                    sql_insert_query = """INSERT INTO "Horarios" VALUES(%s, %s, %s, %s, %s)"""
                    insert_tuple = (1, 1, 'E', dia, listDia)
                    result = cursor.execute(sql_insert_query, insert_tuple)

                    connect_db.commit()
                    print("Fila insertada correctamente")

                if(cuatrimestre == '2' or cuatrimestre == 'segundo'):
                    listDia = extractDataTable1_1E1C_1E2C(cuatrimestre, dia)

                    sql_insert_query = """INSERT INTO "Horarios" VALUES(%s, %s, %s, %s, %s)"""
                    insert_tuple = (1, 2, 'E', dia, listDia)
                    result = cursor.execute(sql_insert_query, insert_tuple)

                    connect_db.commit()
                    print("Fila insertada correctamente")

            if(sys.argv[2] == 'F' or sys.argv[2] == 'f'):
                if(cuatrimestre == '1' or cuatrimestre == 'primero' or cuatrimestre == 'primer'):
                    listDia = extractDataTable1_1F1C_1F2C(cuatrimestre, dia)

                    sql_insert_query = """INSERT INTO "Horarios" VALUES(%s, %s, %s, %s, %s)"""
                    insert_tuple = (1, 1, 'F', dia, listDia)
                    result = cursor.execute(sql_insert_query, insert_tuple)

                    connect_db.commit()
                    print("Fila insertada correctamente")

                if(cuatrimestre == '2' or cuatrimestre == 'segundo'):
                    listDia = extractDataTable1_1F1C_1F2C(cuatrimestre, dia)

                    sql_insert_query = """INSERT INTO "Horarios" VALUES(%s, %s, %s, %s, %s)"""
                    insert_tuple = (1, 2, 'F', dia, listDia)
                    result = cursor.execute(sql_insert_query, insert_tuple)

                    connect_db.commit()
                    print("Fila insertada correctamente")

        if(sys.argv[1] == '2' or sys.argv[1] == 'segundo' or sys.argv[1] == 'dos'):
            if(sys.argv[2] == 'A' or sys.argv[2] == 'a'):
                if(cuatrimestre == '1' or cuatrimestre == 'primero' or cuatrimestre == 'primer'):
                    listDia = extractDataTable1_2A1C_2A2C(cuatrimestre, dia)

                    sql_insert_query = """INSERT INTO "Horarios" VALUES(%s, %s, %s, %s, %s)"""
                    insert_tuple = (2, 1, 'A', dia, listDia)
                    result = cursor.execute(sql_insert_query, insert_tuple)

                    connect_db.commit()
                    print("Fila insertada correctamente")

                if(cuatrimestre == '2' or cuatrimestre == 'segundo'):
                    listDia = extractDataTable1_2A1C_2A2C(cuatrimestre, dia)

                    sql_insert_query = """INSERT INTO "Horarios" VALUES(%s, %s, %s, %s, %s)"""
                    insert_tuple = (2, 2, 'A', dia, listDia)
                    result = cursor.execute(sql_insert_query, insert_tuple)

                    connect_db.commit()
                    print("Fila insertada correctamente")
    
            if(sys.argv[2] == 'B' or sys.argv[2] == 'b'):
                if(cuatrimestre == '1' or cuatrimestre == 'primero' or cuatrimestre == 'primer'):
                    listDia = extractDataTable1_2B1C_2B2C(cuatrimestre, dia)

                    sql_insert_query = """INSERT INTO "Horarios" VALUES(%s, %s, %s, %s, %s)"""
                    insert_tuple = (2, 1, 'B', dia, listDia)
                    result = cursor.execute(sql_insert_query, insert_tuple)

                    connect_db.commit()
                    print("Fila insertada correctamente")

                if(cuatrimestre == '2' or cuatrimestre == 'segundo'):
                    listDia = extractDataTable1_2B1C_2B2C(cuatrimestre, dia)

                    sql_insert_query = """INSERT INTO "Horarios" VALUES(%s, %s, %s, %s, %s)"""
                    insert_tuple = (2, 2, 'B', dia, listDia)
                    result = cursor.execute(sql_insert_query, insert_tuple)

                    connect_db.commit()
                    print("Fila insertada correctamente")

            if(sys.argv[2] == 'C' or sys.argv[2] == 'c'):
                if(cuatrimestre == '1' or cuatrimestre == 'primero' or cuatrimestre == 'primer'):
                    listDia = extractDataTable1_2C1C_2C2C(cuatrimestre, dia)

                    sql_insert_query = """INSERT INTO "Horarios" VALUES(%s, %s, %s, %s, %s)"""
                    insert_tuple = (2, 1, 'C', dia, listDia)
                    result = cursor.execute(sql_insert_query, insert_tuple)

                    connect_db.commit()
                    print("Fila insertada correctamente")

                if(cuatrimestre == '2' or cuatrimestre == 'segundo'):
                    listDia = extractDataTable1_2C1C_2C2C(cuatrimestre, dia)

                    sql_insert_query = """INSERT INTO "Horarios" VALUES(%s, %s, %s, %s, %s)"""
                    insert_tuple = (2, 2, 'C', dia, listDia)
                    result = cursor.execute(sql_insert_query, insert_tuple)

                    connect_db.commit()
                    print("Fila insertada correctamente")

            if(sys.argv[2] == 'D' or sys.argv[2] == 'd'):    
                if(cuatrimestre == '1' or cuatrimestre == 'primero' or cuatrimestre == 'primer'):
                    listDia = extractDataTable1_2D1C_2D2C(cuatrimestre, dia)

                    sql_insert_query = """INSERT INTO "Horarios" VALUES(%s, %s, %s, %s, %s)"""
                    insert_tuple = (2, 1, 'D', dia, listDia)
                    result = cursor.execute(sql_insert_query, insert_tuple)

                    connect_db.commit()
                    print("Fila insertada correctamente")

                if(cuatrimestre == '2' or cuatrimestre == 'segundo'):
                    listDia = extractDataTable1_2D1C_2D2C(cuatrimestre, dia)

                    sql_insert_query = """INSERT INTO "Horarios" VALUES(%s, %s, %s, %s, %s)"""
                    insert_tuple = (2, 2, 'D', dia, listDia)
                    result = cursor.execute(sql_insert_query, insert_tuple)

                    connect_db.commit()
                    print("Fila insertada correctamente")

        if(sys.argv[1] == '3' or sys.argv[1] == 'tercero' or sys.argv[1] == 'tres'):
            if(sys.argv[2] == 'A' or sys.argv[2] == 'a'):
                if(cuatrimestre == '1' or cuatrimestre == 'primero' or cuatrimestre == 'primer'):
                    listDia = extractDataTable1_3A1C(dia)

                    sql_insert_query = """INSERT INTO "Horarios" VALUES(%s, %s, %s, %s, %s)"""
                    insert_tuple = (3, 1, 'A', dia, listDia)
                    result = cursor.execute(sql_insert_query, insert_tuple)

                    connect_db.commit()
                    print("Fila insertada correctamente")

            if(sys.argv[2] == 'B' or sys.argv[2] == 'b'):
                if(cuatrimestre == '1' or cuatrimestre == 'primero' or cuatrimestre == 'primer'):
                    listDia = extractDataTable1_3B1C(dia)

                    sql_insert_query = """INSERT INTO "Horarios" VALUES(%s, %s, %s, %s, %s)"""
                    insert_tuple = (3, 1, 'B', dia, listDia)
                    result = cursor.execute(sql_insert_query, insert_tuple)

                    connect_db.commit()
                    print("Fila insertada correctamente")

            if(sys.argv[2] == 'C' or sys.argv[2] == 'c'):
                if(cuatrimestre == '1' or cuatrimestre == 'primero' or cuatrimestre == 'primer'):
                    listDia = extractDataTable1_3C1C(dia)

                    sql_insert_query = """INSERT INTO "Horarios" VALUES(%s, %s, %s, %s, %s)"""
                    insert_tuple = (3, 1, 'C', dia, listDia)
                    result = cursor.execute(sql_insert_query, insert_tuple)

                    connect_db.commit()
                    print("Fila insertada correctamente")

            if(sys.argv[2] == '-'):
                if(especialidad == 'COMPUTADORES'):
                    listDia = extractDataTable1_3C_Computadores(dia)

                    sql_insert_query = """INSERT INTO "Horarios" VALUES(%s, %s, %s, %s, %s, %s)"""
                    insert_tuple = (3, 2, '-', dia, listDia, especialidad)
                    result = cursor.execute(sql_insert_query, insert_tuple)

                    connect_db.commit()
                    print("Fila insertada correctamente")

                if(especialidad == 'SOFTWARE'):
                    listDia = extractDataTable1_3C_Software(dia)

                    sql_insert_query = """INSERT INTO "Horarios" VALUES(%s, %s, %s, %s, %s, %s)"""
                    insert_tuple = (3, 2, '-', dia, listDia, especialidad)
                    result = cursor.execute(sql_insert_query, insert_tuple)

                    connect_db.commit()
                    print("Fila insertada correctamente")

                if(especialidad == 'SISTEMAS INTELIGENTES'):
                    listDia = extractDataTable1_3C_Computacion_SistemasInteligentes(dia)

                    sql_insert_query = """INSERT INTO "Horarios" VALUES(%s, %s, %s, %s, %s, %s)"""
                    insert_tuple = (3, 2, '-', dia, listDia, especialidad)
                    result = cursor.execute(sql_insert_query, insert_tuple)

                    connect_db.commit()
                    print("Fila insertada correctamente")

                if(especialidad == 'SISTEMAS INFORMACION'):
                    listDia = extractDataTable1_3C_SistemasInformacion(dia)

                    sql_insert_query = """INSERT INTO "Horarios" VALUES(%s, %s, %s, %s, %s, %s)"""
                    insert_tuple = (3, 2, '-', dia, listDia, especialidad)
                    result = cursor.execute(sql_insert_query, insert_tuple)

                    connect_db.commit()
                    print("Fila insertada correctamente")

                if(especialidad == 'TECNOLOGIAS INFORMACION'):
                    listDia = extractDataTable1_3C_TecnologiasInformacion(dia)

                    sql_insert_query = """INSERT INTO "Horarios" VALUES(%s, %s, %s, %s, %s, %s)"""
                    insert_tuple = (3, 2, '-', dia, listDia, especialidad)
                    result = cursor.execute(sql_insert_query, insert_tuple)

                    connect_db.commit()
                    print("Fila insertada correctamente")

        if(sys.argv[1] == '4' or sys.argv[1] == 'cuarto' or sys.argv[1] == 'cuatro'):
            if(cuatrimestre == '1' or cuatrimestre == 'primero' or cuatrimestre == 'primer'):
                if(especialidad == 'COMPUTADORES'):
                    listDia = extractDataTable1_4C_1C_2C_Computadores(cuatrimestre, dia)

                    sql_insert_query = """INSERT INTO "Horarios" VALUES(%s, %s, %s, %s, %s, %s)"""
                    insert_tuple = (4, 1, '-', dia, listDia, especialidad)
                    result = cursor.execute(sql_insert_query, insert_tuple)

                    connect_db.commit()
                    print("Fila insertada correctamente")

                if(especialidad == 'SOFTWARE'):
                    listDia = extractDataTable1_4C_1C_2C_Software(cuatrimestre, dia)

                    sql_insert_query = """INSERT INTO "Horarios" VALUES(%s, %s, %s, %s, %s, %s)"""
                    insert_tuple = (4, 1, '-', dia, listDia, especialidad)
                    result = cursor.execute(sql_insert_query, insert_tuple)

                    connect_db.commit()
                    print("Fila insertada correctamente")

                if(especialidad == 'SISTEMAS INTELIGENTES'):
                    listDia = extractDataTable1_4C_1C_2C_Computacion_SistemasInteligentes(cuatrimestre, dia)

                    sql_insert_query = """INSERT INTO "Horarios" VALUES(%s, %s, %s, %s, %s, %s)"""
                    insert_tuple = (4, 1, '-', dia, listDia, especialidad)
                    result = cursor.execute(sql_insert_query, insert_tuple)

                    connect_db.commit()
                    print("Fila insertada correctamente")

                if(especialidad == 'SISTEMAS INFORMACION'):
                    listDia = extractDataTable1_4C_1C_2C_SistemasInformacion(cuatrimestre, dia)

                    sql_insert_query = """INSERT INTO "Horarios" VALUES(%s, %s, %s, %s, %s, %s)"""
                    insert_tuple = (4, 1, '-', dia, listDia, especialidad)
                    result = cursor.execute(sql_insert_query, insert_tuple)

                    connect_db.commit()
                    print("Fila insertada correctamente")

                if(especialidad == 'TECNOLOGIAS INFORMACION'):
                    listDia = extractDataTable1_4C_1C_2C_TecnologiasInformacion(cuatrimestre, dia)

                    sql_insert_query = """INSERT INTO "Horarios" VALUES(%s, %s, %s, %s, %s, %s)"""
                    insert_tuple = (4, 1, '-', dia, listDia, especialidad)
                    result = cursor.execute(sql_insert_query, insert_tuple)

                    connect_db.commit()
                    print("Fila insertada correctamente")

            if(cuatrimestre == '2' or cuatrimestre == 'segundo'):
                if(especialidad == 'COMPUTADORES'):
                    listDia = extractDataTable1_4C_1C_2C_Computadores(cuatrimestre, dia)

                    sql_insert_query = """INSERT INTO "Horarios" VALUES(%s, %s, %s, %s, %s, %s)"""
                    insert_tuple = (4, 2, '-', dia, listDia, especialidad)
                    result = cursor.execute(sql_insert_query, insert_tuple)

                    connect_db.commit()
                    print("Fila insertada correctamente")

                if(especialidad == 'SOFTWARE'):
                    listDia = extractDataTable1_4C_1C_2C_Software(cuatrimestre, dia)

                    sql_insert_query = """INSERT INTO "Horarios" VALUES(%s, %s, %s, %s, %s, %s)"""
                    insert_tuple = (4, 2, '-', dia, listDia, especialidad)
                    result = cursor.execute(sql_insert_query, insert_tuple)

                    connect_db.commit()
                    print("Fila insertada correctamente")

                if(especialidad == 'SISTEMAS INTELIGENTES'):
                    listDia = extractDataTable1_4C_1C_2C_Computacion_SistemasInteligentes(cuatrimestre, dia)

                    sql_insert_query = """INSERT INTO "Horarios" VALUES(%s, %s, %s, %s, %s, %s)"""
                    insert_tuple = (4, 2, '-', dia, listDia, especialidad)
                    result = cursor.execute(sql_insert_query, insert_tuple)

                    connect_db.commit()
                    print("Fila insertada correctamente")

                if(especialidad == 'SISTEMAS INFORMACION'):
                    listDia = extractDataTable1_4C_1C_2C_SistemasInformacion(cuatrimestre, dia)

                    sql_insert_query = """INSERT INTO "Horarios" VALUES(%s, %s, %s, %s, %s, %s)"""
                    insert_tuple = (4, 2, '-', dia, listDia, especialidad)
                    result = cursor.execute(sql_insert_query, insert_tuple)

                    connect_db.commit()
                    print("Fila insertada correctamente")

                if(especialidad == 'TECNOLOGIAS INFORMACION'):
                    listDia = extractDataTable1_4C_1C_2C_TecnologiasInformacion(cuatrimestre, dia)

                    sql_insert_query = """INSERT INTO "Horarios" VALUES(%s, %s, %s, %s, %s, %s)"""
                    insert_tuple = (4, 2, '-', dia, listDia, especialidad)
                    result = cursor.execute(sql_insert_query, insert_tuple)

                    connect_db.commit()
                    print("Fila insertada correctamente")
                
            # extractDataTable1_4C_1C_2C_Computadores()
            # extractDataTable1_4C_1C_2C_Software()
            # extractDataTable1_4C_1C_2C_Computacion_SistemasInteligentes()
            # extractDataTable1_4C_1C_2C_SistemasInformacion()
            # extractDataTable1_4C_1C_2C_TecnologiasInformacion()
    else:
        print("Error: indicar el curso, el grupo, el cuatrimestre y el día")
