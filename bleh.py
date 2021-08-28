import pyttsx3
import PyPDF2
import dlib


book=open('ObjectOrientedProgramminginC4thEdition.pdf','rb')

pdfreader=PyPDF2.PdfFileReader(book)
pages=pdfreader.numPages
print(pages)
speaker=pyttsx3.init()
speaker.say("hello world i can speak")
speaker.runAndWait()
