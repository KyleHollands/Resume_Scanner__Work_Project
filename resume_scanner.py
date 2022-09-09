import os
import docx2txt
import PyPDF2
import shutil
import sys

# Summary
# Loop through a directory of files, and convert to plain text (.pdf/.docx, etc). Then, open the file and search for specific keywords. If keywords are found,
# move the original file to a new folder.

def main(argv):

    keywords = ["virtual", "zoom", "speak", "public", "presentation", "present"]
    origin = r'C:\Users\Personal\Desktop\Mods\\'
    destination = r'C:\Users\Personal\Desktop\Mods\First Pass'
    
    for fname in os.listdir(r'C:\Users\Personal\Desktop\Mods'): # Set directory to search

        # If the file ends with .docx
        if fname.endswith(".docx"):
            temp = docx2txt.process(origin + fname)
            clean_search(temp, fname, destination, keywords, origin)  

        # If the file ends with .pdf          
        elif fname.endswith(".pdf"):
            pdffileobj = open(origin + fname,'rb')
            pdfreader = PyPDF2.PdfFileReader(pdffileobj, strict=False)
            pages = pdfreader.numPages
            output = []

            for i in range(pages):
                pageobj = pdfreader.getPage(i)
                output.append(pageobj.extractText())
                seperator = ','
                temp = seperator.join(output)
            clean_search(temp, fname, destination, keywords, origin)

        else:
            pass

def clean_search(temp, fname, destination, keywords, origin):
    temp.replace(" ", "")
    temp.strip()
    temp = ''.join(temp.split())
    temp = ''.join(e for e in temp if e.isalnum())
    temp = temp.lower()

    contained = [x for x in keywords if x in temp]
    
    if ((len(contained) / len(keywords)) * 100) >= 25:
        print("At least 25% of keywords found.")
        shutil.copy(origin + fname, destination)

    else:
        print("Less than 25% of keywords found.") 

if __name__ == "__main__":
    main(sys.argv)

input('Press ENTER to exit')