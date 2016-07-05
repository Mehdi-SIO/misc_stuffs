import os

#This script counts the numer of html files in the PATH directory
i = 0
PATH = "/home/mehdi/scrapping_doc_python2/python_doc/docs.python.org/2/howto"
for file in os.listdir(PATH):
    if file.endswith(".html"):
        i += 1
print(i)
