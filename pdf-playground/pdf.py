import PyPDF2

# rd --> read binaries
with open('dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)
    print(reader.getPage(0))
    page = reader.getPage(0)
    rotated_page = page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(rotated_page)
    with open('tilt.pdf','wb') as file:
        writer.write(file)
