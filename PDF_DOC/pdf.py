import PyPDF2
""""
#Read PDF file
pdfFile = open('D:/python/doc.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
#print pdf file page
print(pdfReader.numPages)

pageObj = pdfReader.getPage(0)
print(pageObj.extractText())

"""

"""
#Copying Pages
#open odf file
pdfFile = open('D:/python/doc.pdf', 'rb')
pdfFile1 = open('D:/python/doc1.pdf', 'rb')

#read  pdf file
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfReader1 = PyPDF2.PdfFileReader(pdfFile1)

#write pdf file
pdfWriter = PyPDF2.PdfFileWriter()

#copy page from pdf file
for pageNum in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

#copy page from pdf file
for pageNum in range(pdfReader1.numPages):
    pageObj = pdfReader1.getPage(pageNum)
    pdfWriter.addPage(pageObj)

#Create and Open third pdf file for writting
pdfOutputFile = open('D:/python/combinedminutes.pdf', 'wb')

pdfWriter.write(pdfOutputFile)

pdfOutputFile.close()
pdfFile.close()
pdfFile1.close()

"""

"""
#Encrypting PDFs

pdfFile = open('D:/python/doc.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter = PyPDF2.PdfFileWriter()
for pageNum in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(pageNum))

pdfWriter.encrypt('ahmad')
resultPdf = open('D:/python/encryptedoc.pdf', 'wb')
pdfWriter.write(resultPdf)
resultPdf.close()
"""
"""
#Decrypting PDFs
#pdfReader = PyPDF2.PdfFileReader(open('D:/python/doc.pdf', 'rb'))
pdfReader1 = PyPDF2.PdfFileReader(open('D:/python/encryptedoc.pdf', 'rb'))

#print(pdfReader.isEncrypted)
#print(pdfReader1.isEncrypted)
#pdfReader1.getPage(0)          #Error happened
pdfReader1.decrypt('ahmad')
pageObj = pdfReader1.getPage(0)
print(pageObj.extractText())
"""

#Rotating Pages
minutesFile = open('D:/python/doc.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)
page = pdfReader.getPage(0)
page.rotateClockwise(90)

pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(page)
resultPdfFile = open('D:/python/rotatedPage.pdf', 'wb')
pdfWriter.write(resultPdfFile)
resultPdfFile.close()
minutesFile.close()

