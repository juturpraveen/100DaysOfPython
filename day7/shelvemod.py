import shelve
shelfFile = shelve.open('myFileData')
cats = ['rat', 'catloco', 'marpat']
shelfFile['cats'] = cats
shelfFile.close()


# Read the file contents
shelfFileRead = shelve.open('myFileData')
print(type(shelfFileRead))
print(shelfFileRead['cats'])
shelfFile.close()