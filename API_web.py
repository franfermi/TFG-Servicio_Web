#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify, render_template
import os
import json
import psycopg2
import funciones_API

app = Flask(__name__)

{
   "status": "OK"
}

db = os.environ['NAME_DB']
host_db = os.environ['HOST_DB']
usuario = os.environ['USER_DB']
pw = os.environ['PW_DB']

@app.route("/status")
def docker():
    return jsonify(status='OK')

@app.route("/")
def index():
    funciones_API.conexionBD()
    return render_template("index.html")

@app.route("/busquedaProfesoresContactos", methods=['POST'])
def busquedaPC():
	asig = request.form['asignatura']
	res = funciones_API.obtenerGuiaDocente(asig)

	return render_template("resultGD.html", resultado=res)

@app.route("/busquedaHorarios", methods=['POST'])
def busquedaHO():
    cursoHO = request.form['curso']
    cuatrimestreHO = request.form['cuatrimestre']
    grupoHO = request.form['grupo']
    diaHO = request.form['dia']
    res = funciones_API.obtenerHorarios(cursoHO, cuatrimestreHO, grupoHO, diaHO)

    return render_template("resultHO.html", resultado=res)

@app.route("/busquedaExamenes", methods=['POST'])
def busquedaEX():
    asignaturaEX = request.form['asignatura']
    semestreEX = request.form['semestre']
    convocatoriaEX = request.form['convocatoria']
    res = funciones_API.obtenerFechaEx(asignaturaEX, semestreEX, convocatoriaEX)

    return render_template("resultEX.html", resultado=res)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('http_404.html')

if __name__ == "__main__":
	app.run('0.0.0.0',5000, debug=True)