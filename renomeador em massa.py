import os


def rename_files(directory, newname):
    files = os.listdir(directory)
    counter = 1
    for file in files:
        filetype = file.split('.')[-1]
        os.rename(directory + '/' + file, directory + '/' + newname + str(counter) + '.' + filetype)
        print ('Renaming' + file + " to " + newname + str(counter) + "." + filetype)
        counter += 1


rename_files("C:\\path\\path\\path\\path\\path", "digite nome aqui")

#C:\\path\\path\\path\\path\\path", "digite nome aqui"