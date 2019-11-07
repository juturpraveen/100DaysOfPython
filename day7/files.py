import os
# path = os.path.join('usr', 'bin', 'spam')
# # print(path)

# myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
# for filename in myFiles:
#     print(os.path.join('usr/bin/spam', filename))

# # Current working directory
# print(os.getcwd())
# os.chdir('/Users/praveenjutur/ml/100')
# print(os.getcwd())

# # Create new directory
# os.makedirs('Users/praveenjutur/ml/100/day7/day71/day72')

#File handling
helloPath = os.path.join(os.getcwd(), 'Hello.txt')
# print(helloPath)
helloFile = open(helloPath)
# helloContent = helloFile.read()
# print(helloContent)
helloFile = open(helloPath,'w')
helloFile.write('New Hello for Praveen Jutur')
helloFile.close()
helloFile = open(helloPath)
helloContent = helloFile.read()
helloFile.close()
print(helloContent)