#!
'''
Add bullet point for each line of text on the clip board.
'''
import pyperclip

text = pyperclip.paste()

textList = text.split('.')

for i in range(len(textList)):
    textList[i] = '* ' + textList[i]

text = '\n'.join(textList)
pyperclip.copy(text)
 