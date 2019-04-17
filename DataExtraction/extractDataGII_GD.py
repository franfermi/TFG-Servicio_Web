#!/usr/bin/env python
# -*- coding: utf-8 -*-

import camelot
import csv
import os
import sys
import pandas as pd
import psycopg2

RESOURCE = './resources'
OUTPUT = './outputs/GUIAS_DOCENTES'

db = os.environ['NAME_DB']
host_db = os.environ['HOST_DB']
usuario = os.environ['USER_DB']
pw = os.environ['PW_DB']

def extractDataTeable_GuiaDocente(asignatura):

    connect_db = psycopg2.connect(database=db, user=usuario, password=pw, host=host_db)
    cursor = connect_db.cursor()

    if asignatura == 'ALEM':
        tablas = camelot.read_pdf(os.path.join(RESOURCE, 'ALEM-GII.pdf'), pages='1')
        tablas.export(os.path.join(OUTPUT, 'ALEM-GII.csv'), f='csv', compress=False)

        with open(os.path.join(OUTPUT, 'ALEM-GII-page-1-table-2.csv'), 'r') as archivo:
            datos = pd.read_csv(archivo, header=-1)

            profesores = (datos.iloc[:, 0])
            contactos = (datos.iloc[:, 1])

            listProfesores = []
            for x in profesores:
                listProfesores.extend(x.strip().split('\n'))

            listContactos = []
            for x in contactos:
                listContactos.extend(x.strip().split('\n'))

            sql_insert_query = """INSERT INTO "GuiasDocentes" VALUES(%s, %s, %s)"""
            insert_tuple = ('ALEM', listProfesores, listContactos)
            result = cursor.execute(sql_insert_query, insert_tuple)

            connect_db.commit()
            print("Fila insertada correctamente")

    if asignatura == 'CA':
        tablas = camelot.read_pdf(os.path.join(RESOURCE, 'Cаlculo-Grado-Informatica-17-18.pdf'), pages='2')
        tablas.export(os.path.join(OUTPUT, 'Cаlculo-Grado-Informatica-17-18.csv'), f='csv', compress=False)

        with open(os.path.join(OUTPUT, 'Cаlculo-Grado-Informatica-17-18-page-1-table-2.csv'), 'r') as archivo:
            datos = pd.read_csv(archivo, header=0)
            datosNoNaN = datos.fillna(value='')

            profesores = (datosNoNaN.iloc[:, 0])
            contactos = (datos.iloc[:, 1])

            listProfesores = []
            for x in profesores:
                listProfesores.extend(x.strip().split('\n'))

            listContactos = []
            for x in contactos:
                listContactos.extend(x.strip().split('\n'))

            sql_insert_query = """INSERT INTO "GuiasDocentes" VALUES(%s, %s, %s)"""
            insert_tuple = (asignatura, listProfesores, listContactos)
            result = cursor.execute(sql_insert_query, insert_tuple)

            connect_db.commit()
            print("Fila insertada correctamente")


if __name__ == '__main__':
    if sys.argv[1:]:
        asignatura = sys.argv[1]
        extractDataTeable_GuiaDocente(asignatura)
    else:
        print('Error: indique la asignatura')
