# WAP to manipulate pdf files using pyPDF. Your program should be able to merge multiple pdf files into a single pdf. 
# You are welcome to add more functionalities
# pypdf is a free and open-source pure-python PDF library capable of splitting, merging, cropping, and transforming the pages 
# of PDF files. It can also add custom data, viewing options, and password to PDF files. pypdg can retrieve text and metadata 
# from PDFs as well.


from PyPDF2 import PdfWriter
import os

merger = PdfWriter()
files = [file for file in os.listdir() if file.endswith(".pdf")]

for pdf in files:
    merger.append(pdf)


merger.write("Merger_PDF_file.pdf")
merger.close()

# See this code correctly running and merging in Master Python Language (Part-2)



