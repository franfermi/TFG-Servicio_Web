# import tabula 

# df = tabula.read_pdf("CalendarioExamenes18-19-GII.pdf", encoding='utf-8', spreadsheet=True, pages='1-6041')

# df.to_csv('otuput.csv', encoding='utf-8')

############################################

# from tabula import convert_into

# convert_into("CalendarioExamenes18-19-GII.pdf", "test_s.tsv", encoding='utf-8', spreadsheet=True, output_format="tsv", pages='1-1')


############################################

# from tabula import wrapper

# file_path = "https://etsiit.ugr.es/pages/calendario_academico/examenes-curso-1819/calendarioexamenes1819gii/!"

# df = wrapper.read_pdf(file_path)
# tabula.convert_into("HORARIOS1819.pdf", "prueba.csv", output_format="csv")

# print(df)

import tabula

# Read pdf into DataFrame
df = tabula.read_pdf("test.pdf", options)

# Read remote pdf into DataFrame
df2 = tabula.read_pdf("https://github.com/tabulapdf/tabula-java/raw/master/src/test/resources/technology/tabula/arabic.pdf")

# convert PDF into CSV
tabula.convert_into("CalendarioExamenes18-19-GII.pdf", "output.csv", output_format="csv")

# convert all PDFs in a directory
tabula.convert_into_by_batch("input_directory", output_format='csv')
