'''
imported module: pyPDF2 - pip install pyPDF2
this program append the filename string into a list, 
then output the resulting pdfs

'''

from PyPDF2 import PdfFileMerger
pdfs = []
for i in range(1, 127, 1):
    pdfs.append('Output{}.pdf'.format(i))

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)
merger.write("Chap1.pdf")
merger.close()
