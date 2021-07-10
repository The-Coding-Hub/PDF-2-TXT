# Programme Topic: .pdf to .txt converter using Python

import PyPDF2

file = input("Enter the path of the file below:\n")
if file.endswith(".pdf"):
    pdf = PyPDF2.PdfFileReader(file)
    pages = pdf.numPages
    text = ""
    for i in range(1, pages + 1):
        text += pdf.getPage(1).extractText()

    with open("MainFile.txt", "w", encoding="UTF-8") as main_file:
        main_file.write(text)
else:
    print("Not a PDF File!")