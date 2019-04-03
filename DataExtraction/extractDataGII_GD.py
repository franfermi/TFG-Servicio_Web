#!/usr/bin/env python
# -*- coding: utf-8 -*-

import camelot
import csv
import os
import sys
import pandas as pd

RESOURCE = './resources'
OUTPUT = './outputs'


def extractDataTeable2_GuiaDocente(asignatura):
    if asignatura == 'ALEM':
        tablas = camelot.read_pdf(os.path.join(RESOURCE, 'ALEM-GII.pdf'), pages='1')
        tablas.export(os.path.join(OUTPUT, 'ALEM-GII.csv'), f='csv', compress=False)

        with open(os.path.join(OUTPUT, 'ALEM-GII-page-1-table-2.csv'), 'r') as archivo:
            datos = pd.read_csv(archivo, header=-1)

            profesores = (datos.iloc[:, 0])
            contactos = (datos.iloc[:, 1])


if __name__ == '__main__':
    if sys.argv[1:]:
        asignatura = sys.argv[1]
        extractDataTeable2_GuiaDocente(asignatura)
    else:
        print('Error: indique la asignatura')
