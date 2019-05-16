#!/bin/usr/python
# -*- coding: utf-8 -*-

import os
import psycopg2

db = os.environ['NAME_DB']
host_db = os.environ['HOST_DB']
usuario = os.environ['USER_DB']
pw = os.environ['PW_DB']

connect_db = psycopg2.connect(database=db, user=usuario, password=pw, host=host_db)
cursor = connect_db.cursor()

def obtenerGuiaDocente(nombAsig):

    asignatura = nombAsig.upper()

    cursor.execute('SELECT * FROM "GuiasDocentes" WHERE asignatura = %s', [asignatura.upper()])

    connect_db.commit()

    guiaDocente = []
    f = cursor.fetchall()

    for c in f:
        res = '-Asignatura: ' + str(c[0]) \
            + '\n\n-Guía docente: ' + str(c[1])
        guiaDocente.append(res)

    return guiaDocente

def obtenerHorarios(curso, cuatrimestre, grupo, dia):

    cursor.execute('SELECT * FROM "Horarios" WHERE curso = %s and cuatrimestre = %s and grupo = %s and dia = %s', [(curso), (cuatrimestre), (grupo.upper()), (dia.upper())])

    connect_db.commit()

    horario = []
    f = cursor.fetchall()

    for c in f:
        res = "-Curso: " + str(c[0]) \
            + "\n\n-Semestre: " + str(c[1]) \
            + "\n\n-Grupo: " + str(c[2]) \
            + "\n\n-Día: " + str(c[3]) \
            + "\n\n-Horario: " + str(c[4].replace('"', '').replace(',', ', ').replace('{', '').replace('}', ''))
        horario.append(res)

    return horario

def obtenerFechaEx(asignatura, semestre, convocatoria):

    cursor.execute('SELECT * FROM "FechasExamenes" WHERE asignatura = %s and semestre = %s and convocatoria = %s', [(asignatura), (semestre), (convocatoria.lower())])

    connect_db.commit()

    examen = []
    f = cursor.fetchall()

    for c in f:
        res = "-Asignatura: " + str(c[0]) \
            + "\n\n-Semestre: " + str(c[1]) \
            + "\n\n-Convocatoria: " + str(c[2]) \
            + "\n\n-Fecha exámen (M=mañana y T=tarde): " + str(c[3].replace('"', '').replace(',', ', ').replace('{', '').replace('}', '')) \
            + "\n\nLos exámenes por la mañana serán a las 9:00 y los exámenes por la tarde a las 16:00."
        examen.append(res)

    return examen
