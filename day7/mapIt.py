#! python3
# mapIt.py launches a map in the browser using an address from the command line
# or clip board

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    address = '+'.join(sys.argv[1:])
    print(address)
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place' +address)