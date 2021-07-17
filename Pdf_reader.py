import pyttsx3
import PyPDF2
page=int(input("Page No : "))
book=open("book.pdf","rb")
pdfReader=PyPDF2.PdfFileReader(book)
pages=pdfReader.numPages
print(pages)
speak=pyttsx3.init()
page=pdfReader.getPage(page+17)
text=page.extractText()
speak.say(text)
speak.runAndWait()
