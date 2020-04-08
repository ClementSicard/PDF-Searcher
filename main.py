# import packages
import PyPDF2
import os


def searchInPDF(filename, s):
    # open the pdf file
    f = PyPDF2.PdfFileReader(filename)
    NumPages = f.getNumPages()
    # extract text and do the search
    for i in range(0, NumPages):
        page = f.getPage(i)
        Text = page.extractText().rstrip('\n').lower()
        if s in Text:
            return True
    return False


os.system("cls")
directory = os.getcwd()
s = input("Please enter the expression you want to search : ")
inp = ""
for c in s.lower():
    if c != " ":
        inp += c

a = []

for filename in os.listdir(directory):
    if filename.endswith(".pdf"):
        print("Recherche dans", filename, "...")
        res = searchInPDF(filename, inp)
        if res == True:
            a.append(filename)
    os.system("cls")


if len(a) != 0:
    print("'" + s + "' was found in the following PDFs: ")
    print(a)
else:
    print("'" + s + "' wasn't found.")
