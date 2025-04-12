import os
import re

# Get the folder path
sourceFolder = input('Folder path : ') + '/'

# The new name of the texture
replaceName = input('New name : ')

# Rename all files in the directory and keep textures name and UDIM
def Rename():

    # Check if teh use gave a folder path
    if sourceFolder == '':
        print('No folder path given.')
    
    else:

        # Make a list of element in the given directory path
        filesName = [f for f in os.listdir(sourceFolder)]
        print('There are ' + str(len(filesName)) + ' elements in the folder.')

        # For each elements in Files names
        for index, value in enumerate(filesName):
            fullFiles = [sourceFolder + filesName[index]]

            # If the element is a file, rename the file
            if os.path.isfile(fullFiles[0]):
                placeolderName = fullFiles[0].replace(sourceFolder, '')
                placeolderName = re.sub(r'^.*(?=([_]\w{1,}[.]\d{4}[.]))', replaceName, placeolderName)
                os.rename(fullFiles[0], sourceFolder + placeolderName)

            # If the element is a folder
            else:
                print('Not renaming folder : ' + fullFiles[0].replace(sourceFolder, ''))

Rename()