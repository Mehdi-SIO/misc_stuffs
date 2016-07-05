
import os

chemin = os.getcwd()
print(os.listdir(chemin))
file_count = 0
outFile = open('out.txt', 'w')
for file in os.listdir(chemin):
    print(file)
    outFile.write(file + '\n')
    file_count += 1
outFile.close()
print(file_count)



#Ecriture du fichier out.txt
outFile = open('out.txt', 'w')
outFile.write('file_name' + '\n')

import os
dirnum = 0
filenum = 0
for dirname, dirnames, filenames in os.walk('.'):
    # print path to all subdirectories first.
    for subdirname in dirnames:
        print(os.path.join(dirname, subdirname))
        dirnum += 1


    # print path to all filenames.
    for filename in filenames:
        print(os.path.join(dirname, filename))
        filenum += 1

print('Nombre de dossier: ' + str(dirnum))
print('Nombre de fichier: ' + str(filenum))
'''
    # Advanced usage:
    # editing the 'dirnames' list will stop os.walk() from recursing into there.
    if '.git' in dirnames:
        # don't go into any .git directories.
        dirnames.remove('.git')

'''