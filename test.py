import re, pyperclip

# emailRegex1 = re.compile(r'\w+@\w+.\w+$')
# print(emailRegex1.search('My email is praveenjutur@gmail.com').group())

emailRegex2 = re.compile(r'''([a-zA-Z0-9_.+-]+@[a-zA-Z0-9_.+-]+\.[a-zA-Z]{2,4})''')
# print(emailRegex2.search('A praveen.jutur@gmail.com').group())

text = pyperclip.paste()
print(emailRegex2.findall(text))

