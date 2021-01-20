import PyPDF2
import sys
import os
from pathvalidate import ValidationError, validate_filename

while 1:
    #check if file argument is given
    try:
        file = os.path.abspath(sys.argv[1])
    except IndexError:
        print("No file arguement given")
        exit()


    #check if file exists
    if(not os.path.exists(file)):
        print("file doesnt exists!")
        exit()
    pdf = open(file, "rb")

    #check if you can open file
    try:
        pdfobj = PyPDF2.PdfFileReader(pdf)
    except:
        print("Error opening file. (Is the file a PDF?)")
        exit()
    #validate if name can be a valid filename
    try:
        nameofPdf = input("What would you like to name your file?\n")
        validate_filename(nameofPdf+".pdf")
    except ValidationError as e:
        print(f"{e}\n", file=sys.stderr)
        continue

    numPages = pdfobj.getNumPages()
    for i in range(numPages):
        page = pdfobj.getPage(i)
        writePdf = PyPDF2.PdfFileWriter()
        writePdf.addPage(page)
        writeFile = open(f"{nameofPdf}_{i+1}.pdf", "wb+")
        writePdf.write(writeFile)
        writeFile.close()
    break


