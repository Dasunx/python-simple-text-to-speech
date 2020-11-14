import pyttsx3
import PyPDF2


# add pdf file in current directory and rename mypdf.pdf below 
book = open('mypdf.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
page = pdfReader.getPage(19)
text = page.extractText()
with open("my.txt", 'w',encoding='utf-8') as f:
    f.write(text)
engine = pyttsx3.init()
rate = engine.getProperty('rate')
# engine.setProperty('rate', rate+50)
# engine.save_to_file(text, "audiobook.mp3")
engine.say(text)
engine.runAndWait()



