import PyPDF2
with open('dummy.pdf','rb') as file:
    read=PyPDF2.PdfFileReader(file)
    print(read.numPages)
    
