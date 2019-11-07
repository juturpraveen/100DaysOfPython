# #Raw string ignores escape characters 
# print(r'I am not \' escape character')

# #Multiline strings begin with 3 single or double quotes
# print('''Dear Alice,

# Eve's cat has been arrested for catnapping, cat burglary and extortion.

# Sincerely,
# Bob''')

""" This is 
multiline
comment."""

spam = "Hello world!"
stlist = ['My', "name", "is", "praveen"]
# print('hahaha'.join(stlist))
# sent = ' '.join(stlist)
# print(sent)
# newList = sent.split()
# print(newList)
# print(sent.split('a'))

# multiLine = '''Dear Alice,

# Eve's cat has been arrested for catnapping, cat burglary and extortion.

# Sincerely,
# Bob'''

# print(multiLine.split())

# text = 'Hello'
# print(text.rjust(15, '*'))
# print(text.ljust(15, '-'))
# print(text.center(15,'|'))

#Stripping the white spaces
stripText = "       Hello       "
print(stripText)
print(stripText.strip())
print(stripText.lstrip())
print(stripText.rstrip())