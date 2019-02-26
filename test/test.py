#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import unittest
import binascii

from PyPDF2 import PdfFileReader, PdfFileWriter

class PdfReaderTestCases(unittest.TestCase):
        def test_PdfReaderFileLoad(self):
            with open('./resources/CalendarioExamenes18-19-GII.pdf', 'rb') as inputfile:
                # Load PDF file from file
                ipdf = PdfFileReader(inputfile)
                ipdf_p1 = ipdf.getPage(0)

                # Retrieve the text of the PDF
                with open('./resources/out_page.txt', 'rb') as pdftext_file:
                    pdftext = pdftext_file.read()

                ipdf_p1_text = ipdf_p1.extractText().replace('\n', '').encode('utf-8')

                # Compare the text of the PDF to a known source
                # self.assertEqual(ipdf_p1_text, pdftext,
                #     msg='PDF extracted text differs from expected value.\n\nExpected:\n\n%r\n\nExtracted:\n\n%r\n\n'
                #         % (pdftext, ipdf_p1_text))
                    
if __name__ == '__main__':
    unittest.main()