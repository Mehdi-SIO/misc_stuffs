import PyPDF2

pdfFileObj = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print (pdfReader.numPages)

pageObj = pdfReader.getPage(1)
result = pageObj.extractText()
print result