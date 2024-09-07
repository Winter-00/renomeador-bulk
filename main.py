import os


def rename_files(directory, newname):
    files = os.listdir(directory)
    counter = 0
    for file in files:
        filetype = title.split('.')[-1]
        os.rename(directory + '/' + file, directory + '/' + newname + str(counter) + '.' + filetype)