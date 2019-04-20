#from flask import Flask, request
#from SubjectsGII_Bot.funcionesDB import *
#from flask_restful import Resource, Api
#import json

from flask import Flask, request, jsonify, render_template
import os
import json
import psycopg2

app = Flask(__name__)


{
   "status": "OK"
}

db = os.environ['NAME_DB']
host_db = os.environ['HOST_DB']
usuario = os.environ['USER_DB']
pw = os.environ['PW_DB']

def buscarAsignatura(nombAsig):
    connect_db = psycopg2.connect(database=db, user=usuario, password=pw, host=host_db)
    cursor = connect_db.cursor()

    # cursor.execute("SELECT * FROM AsignaturasGII WHERE asignatura LIKE %s", [nombAsig])
    # asig = gDocen = fExam = hTeo = ""
    # vAsig = []
    # f = cursor.fetchall()

    # for c in f:
    #     asig = "-Asignatura: " + str(c[0]) 
    #     vAsig.append(asig)
    #     gDocen = " -Guía docente: " + str(c[1])
    #     vAsig.append(gDocen)
    #     fExam = " -Fecha exámen final: " + str(c[2]) 
    #     vAsig.append(fExam)
    #     hTeo  = " -Horario teoría: " + str(c[3])
    #     vAsig.append(hTeo)

    # connect_db.close()

    # return vAsig

def obtenerGuiaDocente(nombAsig):
    connect_db = psycopg2.connect(database=db, user=usuario, password=pw, host=host_db)
    cursor = connect_db.cursor()

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

    connect_db.close()

    return vAsig

def obtenerHorarios(curso, cuatrimestre, grupo, dia):
    connect_db = psycopg2.connect(database=db, user=usuario, password=pw, host=host_db)
    cursor = connect_db.cursor()

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

    connect_db.close()

    return vHorario

def obtenerFechaEx(asignatura, semestre, convocatoria):
    connect_db = psycopg2.connect(database=db, user=usuario, password=pw, host=host_db)
    cursor = connect_db.cursor()

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

    connect_db.close()

    return vFechaExamen

@app.route("/status")
def docker():
    return jsonify(status='OK')

@app.route("/")
def index():
    try:
        connect_db = psycopg2.connect(database=db, user=usuario, password=pw, host=host_db)
        cursor = connect_db.cursor()
        print("Conexión establecida")
    except:
        print("Error en la conexión a la BD")
    return render_template("index.html")

@app.route("/busquedaProfesoresContactos", methods=['POST'])
def busquedaPC():
	asig = request.form['asignatura']
	res = obtenerGuiaDocente(asig)

	return render_template("resultGD.html", resultado=res)

@app.route("/busquedaHorarios", methods=['POST'])
def busquedaHO():
    cursoHO = request.form['curso']
    cuatrimestreHO = request.form['cuatrimestre']
    grupoHO = request.form['grupo']
    diaHO = request.form['dia']
    res = obtenerHorarios(cursoHO, cuatrimestreHO, grupoHO, diaHO)

    return render_template("resultHO.html", resultado=res)

@app.route("/busquedaExamenes", methods=['POST'])
def busquedaEX():
    asignaturaEX = request.form['asignatura']
    semestreEX = request.form['semestre']
    convocatoriaEX = request.form['convocatoria']
    res = obtenerFechaEx(asignaturaEX, semestreEX, convocatoriaEX)

    return render_template("resultEX.html", resultado=res)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('http_404.html')

if __name__ == "__main__":
	app.run('0.0.0.0',5000, debug=True)


