# pip3 install PyPDF2

import PyPDF2
import os

merger = PyPDF2.PdfMerger()

# This program will iterate through the current directory in a for loop
# And combine the documents in order from top to bottom

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger.append(file)
    # The name below will be the new name, change if needed
    merger.write("CombinedPDF.pdf")
