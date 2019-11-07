allGuests = {'Alice':{'apples':5, 'pretzels': 12},
             'Bob':{'sandwiches':10, 'apples':6},
             'Carol':{'cups':4, 'pies':10}
            }

def totalBought(guests, item):
    numBought = 0
    for guest, things in guests.items():
        numBought += things.get(item,0)
    return numBought

print("Number of things bought: ")
print(" - Apples "+ str(totalBought(allGuests, 'apples')))
