import PyPDF2
with open('dummy.pdf','rb') as file:
    read=PyPDF2.PdfFileReader(file)
    page=read.getPage(0)
    page.rotateClockwise(90)
    writer=PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('rotated.pdf','wb') as new:
        writer.write(new)
    
    
