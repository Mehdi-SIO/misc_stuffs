#! Python3

import os
import html2text

import os
dirnum = 0
filenum = 0
for dirname, dirnames, filenames in os.walk('.'):
    # print path to all subdirectories first.
    for subdirname in dirnames:
        #print(os.path.join(dirname, subdirname))
        print(dirname)
        dirnum += 1


    # print path to all filenames.
    for filename in filenames:
        #print(os.path.join(dirname, filename))
        print(filename)

        if filename.endswith(".html"):
            html_page = open(os.path.join(dirname, filename), "r")
            f = html_page.read()
            w = open(os.path.splitext(filename)[0] + ".txt", "wb")
            w.write(html2text.html2text(f).encode('utf-8'))
            html_page.close()
            w.close()
        filenum += 1

print('Nombre de dossier: ' + str(dirnum))
print('Nombre de fichier: ' + str(filenum))