#dictionaries
import pprint
eggs = {'name':'Zophie', 'species':'cat', 'age':'8'}
ham = {'species':'cat', 'age':'8', 'name':'Zophie'}
picnicItems = {'apples':5, 'cups':2}
# print(picnicItems.get('apples'))
# print(picnicItems.get('juice'))
# print(eggs == ham)
# print(eggs.keys())
# print(list(eggs.keys()))
# print('Zophie' in eggs.values())

#Use set default method
# print(eggs.setdefault('color', 'grey'))
# print(eggs.setdefault('name', 'praveen'))
# print(eggs)

#Use set default to count characters in a string
sentence = 'The good doctor was busy so we postponed our appointment'
count = {}
for character in sentence:
    count.setdefault(character, 0)
    count[character] += 1
print(count)
pprint.pprint(count)