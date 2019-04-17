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
        profesores = " -Profesores: " + str(c[1])
        vAsig.append(profesores)
        contactos = " -Contactos: " + str(c[2]) 
        vAsig.append(contactos)

    connect_db.close()

    return vAsig

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

@app.route("/busqueda", methods=['POST'])
def busqueda():
	asig = request.form['asignatura']
	res = obtenerGuiaDocente(asig)

	return render_template("result.html", resultado=res)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('http_404.html')

if __name__ == "__main__":
	app.run('0.0.0.0',5000, debug=True)


