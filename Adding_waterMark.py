import PyPDF2

tewmplate=PyPDF2.PdfFileReader(open('BINARYTree.pdf','rb'))
watermark=PyPDF2.PdfFileReader(open('Water_mark.pdf','rb'))

output=PyPDF2.PdfFileWriter()

for i in range(tewmplate.getNumPages()):
    page=tewmplate.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)
    
    with open("new_watermarked.pdf",'wb') as file:
        output.write(file)
        
