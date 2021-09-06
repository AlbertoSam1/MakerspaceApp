''''# importing required modules
import PyPDF2

# creating a pdf file object
pdfFileObj = open('C:/Users/xts229/PycharmProjects/MakerspaceApp-Delta/gui/temp_files/temp_quote.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# creating a page object
pageObj = pdfReader.getPage(0)

# extracting text from page
pdf = pageObj.extractText().encode('utf-8')
print(pdf.decode("utf-8"))

from PyPDF2 import PdfFileReader
from nltk.corpus import words
'''
document_path = 'C:/Users/xts229/PycharmProjects/MakerspaceApp-Delta/gui/temp_files/temp_quote.pdf'



"""information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

    txt = f
    Information about {pdf_path}: 

    Author: {information.author}
    Creator: {information.creator}
    Producer: {information.producer}
    Subject: {information.subject}
    Title: {information.title}
    Number of pages: {number_of_pages}
# closing the pdf file object
pdfFileObj.close()"""

from tika import parser # pip install tika

raw = parser.from_file(document_path)
text = raw['content'].split("\n")
quote_id = None

for i in text:
    if 'Quote No.' in i:
        p = i.split(" ")
        quote_id = p[-1]

print(quote_id)
