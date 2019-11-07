import re

# Phone number
# phNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo = phNumberRegex.search('My number is 123-654-7890')
# print('Phone number found:'+ mo.group())

# #Regex groups
# phNumRegGrp = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# moGrp = phNumRegGrp.search('My number is 123-654-7890')
# print('Phone number found: '+ moGrp.group(0))
# print('Area code: '+ moGrp.group(1))
# print('Phone number: '+ moGrp.group(2))

# # Using pipe symbol
# heroRegex = re.compile(r'Batman|Tina Fey')
# mol = heroRegex.search('Batman and Tina Fey')
# print(mol.group())
# mol = heroRegex.search('Tina Fey and Batman')
# print(mol.group())
# mol = heroRegex.findall('Batman and Tina Fey1')
# print(mol)
# batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
# mo = batRegex.search('Batmobile lost a batwheel')
# mof = batRegex.findall('Batmobile lost a batwheel')
# print(mo.group())
# print(mof)

# # Using question mark (Matching zero or one)
# batRegexq = re.compile(r'Bat(wo)?man')
# moq = batRegexq.search('The adventures of Batman')
# print(moq.group())
# phoneNumberRegexq = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
# mopq = phoneNumberRegexq.search('My number is 123-945-9522.')
# print(mopq.group())
# mopq = phoneNumberRegexq.search('My number is 945-9522.')
# print(mopq.group())

# # Using + Match one or more with the plus
# batRegex = re.compile(r'Bat(wo)+man')
# mo1 = batRegex.search('The adventures of Batwoman')
# print(mo1.group())
# mo2 = batRegex.search('The adventures of Batwowowowoman aka Batwoman')
# mo3 = batRegex.findall('The adventures of Batwowowowoman aka Batwoman')
# print(mo2.group())
# print(mo3)

# # Matching specific repetitions with curly brackets
# haRegex = re.compile(r'(Ha){3}')
# mo1 = haRegex.search('HaHaHa')
# print(mo1.group())
# mo2 = haRegex.search('HaHa')
# print(mo2 == None)

# # Greedy and nongreedy matching
# greedyRegex = re.compile(r'(Ha){3,5}')
# mo1 = greedyRegex.search('HaHaHaHaHaHa')
# print(mo1.group())

# nonGreedyRegex = re.compile(r'(Ha){3,5}?')
# mo2 = nonGreedyRegex.search('HaHaHaHaHa')
# print(mo2.group())

# # Character classes
# xmasRegex = re.compile(r'\d+\s\w+')
# print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves,1 partridge'))
# vowelRegex = re.compile(r'[aeiouAEIOU]')
# print(vowelRegex.findall('Praveen Jutur'))
# consonantRegex = re.compile(r'[^aeiouAEIOU]')
# print(consonantRegex.findall('Praveen Jutur'))

# # Caret and Dollar sign characters
# beginsWithHello = re.compile(r'^Hello')
# print(beginsWithHello.findall('Hello World!'))
# print(beginsWithHello.search('Hello World!') == None)
# wholeStringNum = re.compile(r'^\d+$')
# print(wholeStringNum.search('1232111313') == None)
# print(wholeStringNum.search('12312s12312') == None)

# # Wild card character (.)
# atRegex = re.compile(r'.at')
# print(atRegex.findall('The cat in the hat sat on the flat mat.'))
# # Wild card (.*)
# nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
# mo = nameRegex.search('First Name: Praveen Reddy Last Name: Jutur')
# print(mo.group(1))
# print(mo.group(2))

# # Matching new lines with the (.*)
# noNewlineRegex = re.compile(r'.*')
# mo1 = noNewlineRegex.search('Serve the public trust. \nProtect the innocent. \nUphold the law')
# print(mo1.group())
# newlineRegex = re.compile(r'.*', re.DOTALL)
# mo1 = newlineRegex.search('Serve the public trust. \nProtect the innocent. \nUphold the law')
# print(mo1.group())

# # Case insensitive matching
# robocop = re.compile(r'robocop', re.IGNORECASE)
# print(robocop.search('Robocop is part man part machine all cop').group())
# print(robocop.search('ROBOCOP protects the innocent').group())

# # Substituting strings with SUB() method
# namesRegex = re.compile(r'Agent\s\w+')
# print(namesRegex.sub('CENSORED','Agent alice gave secret documents to Agent Bob'))
# agentNamesRegex = re.compile(r'Agent\s(\w)\w+')
# print(agentNamesRegex.sub(r'\1****', 'Agent Alice to Agent Carol that Agent Eve know Agent Bob was a double agent'))

#