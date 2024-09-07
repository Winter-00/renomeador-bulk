import os
import re

def rename_files(directory, pattern, newname):
    files = os.listdir(directory)
    counter = 1
    for file in files:
        if re.match(pattern, file):
            filetype = file.split('.')[-1]
            os.rename(directory + '/' + file, directory + '/' + newname + str(counter) + '.' + filetype)
            print ('Renaming' + file + " to " + newname + str(counter) + "." + filetype)
            counter += 1


rename_files("C:\\path\\path\\path\\path\\path", ".*[numero incial-numero final]\.*", "nome")





#C:\\path\\path\\path\\path\\path, .*[numero incial-numero final]\.*, "nome"#
#. = qualquer caracter#
#* = repetidas vezes#
#\.* = extensão


#.* = qualquer caractere(s) que aparece frequentemente
#logo .*[número].*  = caractere(s) 1.extensão do arquivo