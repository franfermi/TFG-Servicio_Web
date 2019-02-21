import PyPDF2
import sys
import os
import re

if(len(sys.argv) > 1):
    print ("Abriendo " + sys.argv[1])

    pdf_file = sys.argv[1]
    read_pdf = PyPDF2.PdfFileReader(pdf_file)

    number_of_pages = read_pdf.getNumPages()
    print (number_of_pages)

    page = read_pdf.getPage(0)
    page_number = read_pdf.getPageNumber(page)
    page_mode = read_pdf.getPageMode()
    print (page_number)
    print (page_mode)

    page_content = page.extractText()
    out_page_content = 'out_page.txt'
    os.system(("ps2ascii %s %s") %( pdf_file , out_page_content))
    #print (out_page_content)

    # with open("out_page.txt", "r") as f:
    #     for i in f:
    #         m = re.compile('([ALEM])')
    #         if m:
    #             print(m.group(0))

    asignatura = input("Asignatura a buscar: ")
    repetidas = 0
    f = open("out_page.txt", "r")
    lines = f.readlines()

    for line in lines:
        palabras = line.split()
        for p in palabras:
            if p==asignatura:
                repetidas = repetidas+1
                print(palabras)

    print ("La palabra \"{0}\" se repite {1} veces en el archivo {2}".format(asignatura, repetidas, pdf_file))

else:
    print ("Debes indicar el nombre del archivo")

