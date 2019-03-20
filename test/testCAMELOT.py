#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import unittest
import camelot
import csv

import pandas as pd
from pandas.util.testing import assert_frame_equal

RESOURCE = './resources'
OUTPUT = './outputs'


class TestsCAMELOT(unittest.TestCase):
    def test_parsing_report(self):
        parsing_report = {
            'accuracy': 99.02,
            'whitespace': 12.24,
            'order': 1,
            'page': 1
        }

        filename = os.path.join(RESOURCE, 'foo.pdf')
        tables = camelot.read_pdf(filename)
        assert tables[0].parsing_report == parsing_report

    def test_PdfReaderFileLoad(self):
        tables = camelot.read_pdf(os.path.join(RESOURCE, 'foo.pdf'))

    def test_CsvReaderFileLoad(self):
        with open(os.path.join(OUTPUT, 'foo.csv')) as File:
            reader = csv.reader(File)

    def test_ConvertToCsv(self):
        tables = camelot.read_pdf(os.path.join(RESOURCE, 'foo.pdf'))
        tables.export(os.path.join(OUTPUT, 'foo.csv'), f='csv',
                      compress=False)  # json, excel, html

    def test_ComparePdfCsv(self):
        tables = camelot.read_pdf(os.path.join(RESOURCE, 'foo.pdf'))
        resultsPDF = []

        for row in tables:
            resultsPDF.append(tables[0].df)

        resultsCSV = pd.read_csv(os.path.join(OUTPUT,'foo.csv'), header=-1)
        resultsCSV_sin_nan = resultsCSV.fillna(value='')

        print('EXTRACT TO PDF')
        print(tables[0].df)
        print('----------------------')
        print('EXTRACT TO CSV')
        print(resultsCSV_sin_nan)

        assert_frame_equal(tables[0].df, resultsCSV_sin_nan)


if __name__ == '__main__':
    unittest.main()

