#! python3
import pyperclip, re
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

emailRegex = re.compile(r'''([a-zA-Z0-9_.+-]+@[a-zA-Z0-9_.+-]+\.[a-zA-Z]{2,4})''')

text = str(pyperclip.paste())
phoneNumbers = []
for groups in phoneRegex.findall(text):
    phoneNumber = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNumber += 'x'+groups[8]
    phoneNumbers.append(phoneNumber)
if len(phoneNumbers) > 0:
    pyperclip.copy('\n'.join(phoneNumbers))
    print('Phone numbers copied')
    print(pyperclip.paste())
else:
    print('No phone numbers copied.')

emails = []
for email in emailRegex.findall(text):
    emails.append(email)
if len(emails)>0:
    pyperclip.copy('\n'.join(emails))
    print('Emails copied.')
    print(pyperclip.paste())
else:
    print('No emails copied')

# 800-420-7240
# 415-863-9900
# 415-863-9950
# info@nostarch.com
# media@nostarch.com
# academic@nostarch.com
# help@nostarch.com