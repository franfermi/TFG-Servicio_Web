#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import unittest
import camelot
import csv

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

        filename = os.path.join(RESOURCE,'foo.pdf')
        tables = camelot.read_pdf(filename)
        assert tables[0].parsing_report == parsing_report

    def test_PdfReaderFileLoad(self):
        tables = camelot.read_pdf(os.path.join(RESOURCE,'foo.pdf'))

    def test_CsvReaderFileLoad(self):
        with open(os.path.join(OUTPUT,'foo.csv')) as File:  
            reader = csv.reader(File)

    def test_ConvertToCsv(self):
        tables = camelot.read_pdf(os.path.join(RESOURCE,'foo.pdf'))
        tables.export(os.path.join(OUTPUT,'foo.csv'), f='csv', compress=False) # json, excel, html

    def test_ComparePdfCsv(self):
        tables = camelot.read_pdf(os.path.join(RESOURCE,'foo.pdf'))
        resultsPDF = []

        for row in tables:
            resultsPDF.append(tables[0].df)

        resultsCSV = []
        with open(os.path.join(OUTPUT,'foo.csv')) as File:  
            reader = csv.reader(File)
            for row in reader:
                resultsCSV.append(row)
        
        # print(resultsPDF)
        # print('----------------------')
        # print(resultsCSV)

        # self.assertEqual(resultsPDF, resultsCSV,
        #         msg='PDF extracted text differs from expected value.\n\nExpected:\n\n%r\n\nExtracted:\n\n%r\n\n'
        #             % (resultsPDF, resultsCSV))
                    
if __name__ == '__main__':
    unittest.main()