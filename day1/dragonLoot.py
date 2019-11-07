def displayInventory(inventory):
    totalCount = 0
    for k, v in inventory.items():
        print(v, k)
        totalCount += v
    print('Total number of items: ', totalCount)

# displayInventory(stuff)

def addToInventory(inventory, addedItems):
    for item in addedItems:
        count = 0
        inventory.setdefault(item, 0)
        inventory[item] += count + 1
    return inventory

inv = {'gold coin':42, 'rope':1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)