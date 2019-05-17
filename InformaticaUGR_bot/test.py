#!/bin/usr/python
# -*- coding: utf-8 -*-

import unittest
import funcionesDB

class TestMetodos(unittest.TestCase):

    """ Test que comprueba que una guía docente está disponible"""
    def test_guia_docente_disponible(self):
        guia = funcionesDB.obtenerGuiaDocente("TFG")
        self.assertTrue(guia)

    """ Test que comprueba que una guía docente no está disponible"""
    def test_guia_docente_no_disponible(self):
        guia = funcionesDB.obtenerGuiaDocente("YYY")
        self.assertFalse(guia)

    """ Test que comprueba que un horario está disponible"""
    def test_horario_disponible(self):
        horario = funcionesDB.obtenerHorarios(3, 1, "A", "Lunes")
        self.assertTrue(horario)

    """ Test que comprueba que un horario no está disponible"""
    def test_horario_no_disponible(self):
        horario = funcionesDB.obtenerHorarios(3, 3, "D", "Lunes")
        self.assertFalse(horario)

    """ Test que comprueba que la fecha exámen está disponible"""
    def test_fechaEx_disponible(self):
        fecha = funcionesDB.obtenerFechaEx("IV", 1, "ordinaria")
        self.assertTrue(fecha)

    """ Test que comprueba que la fecha exámen no está disponible"""
    def test_fechaEx_no_disponible(self):
        fecha = funcionesDB.obtenerFechaEx("VV", 1, "ordinaria")
        self.assertFalse(fecha)

if __name__ == '__main__':
   unittest.main()
