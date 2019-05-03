#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import psycopg2

db = os.environ['NAME_DB']
host_db = os.environ['HOST_DB']
usuario = os.environ['USER_DB']
pw = os.environ['PW_DB']

connect_db = psycopg2.connect(database=db, user=usuario, password=pw, host=host_db)
cursor = connect_db.cursor()

def conexionBD():
    try:
        connect_db = psycopg2.connect(database=db, user=usuario, password=pw, host=host_db)
        cursor = connect_db.cursor()
        print("Conexión establecida")
    except:
        print("Error en la conexión a la BD")

def obtenerGuiaDocente(nombAsig):

    asignatura = nombAsig.upper()

    cursor.execute('SELECT * FROM "GuiasDocentes" WHERE asignatura = %s', [asignatura])

    connect_db.commit()

    asig = profesores = contactos = ""
    vAsig = []
    f = cursor.fetchall()

    for c in f:
        asig = "-Asignatura: " + str(c[0])
        vAsig.append(asig)
        profesores = " -Profesores: " + str(c[1].replace('","', ', ').replace('{', '').replace('}', '').replace('"', ''))
        vAsig.append(profesores)
        contactos = " -Contactos: " + str(c[2].replace('","', ', ').replace('{', '').replace('}', '').replace('"', '')) 
        vAsig.append(contactos)

    return vAsig

def obtenerHorarios(curso, cuatrimestre, grupo, dia):

    cursor.execute('SELECT * FROM "Horarios" WHERE curso = %s and cuatrimestre = %s and grupo = %s and dia = %s', [(curso), (cuatrimestre), (grupo), (dia.upper())])

    connect_db.commit()

    cursoH = cuatrimestreH = grupoH = diaH = diaHorario = ''
    vHorario = []
    f = cursor.fetchall()

    for c in f:
        cursoH = "-Curso: " + str(c[0])
        vHorario.append(cursoH)
        cuatrimestreH = "-Cuatrimestre: " + str(c[1])
        vHorario.append(cuatrimestreH)
        grupoH = "-Grupo: " + str(c[2])
        vHorario.append(grupoH)
        diaH = "-Día: " + str(c[3])
        vHorario.append(diaH)
        diaHorario = "-Horario: " + str(c[4].replace('"', '').replace(',', ', ').replace('{', '').replace('}', ''))
        vHorario.append(diaHorario)

    return vHorario

def obtenerFechaEx(asignatura, semestre, convocatoria):

    cursor.execute('SELECT * FROM "FechasExamenes" WHERE asignatura = %s and semestre = %s and convocatoria = %s', [(asignatura), (semestre), (convocatoria.lower())])

    connect_db.commit()

    asignaturaEX = semestreEX = convocatoriaEX = fechaEX = ''
    vFechaExamen = []
    f = cursor.fetchall()

    for c in f:
        asignaturaEX = "-Asignatura: " + str(c[0])
        vFechaExamen.append(asignaturaEX)
        semestreEX = "-Semestre: " + str(c[1])
        vFechaExamen.append(semestreEX)
        convocatoriaEX = "-Convocatoria: " + str(c[2])
        vFechaExamen.append(convocatoriaEX)
        fechaEX = "-Fecha exámen (M=mañana y T=tarde): " + str(c[3].replace('"', '').replace(',', ', ').replace('{', '').replace('}', ''))
        vFechaExamen.append(fechaEX)
        vFechaExamen.append("Los exámenes por la mañana serán a las 9:00 y los exámenes por la tarde a las 16:00.")

    return vFechaExamen