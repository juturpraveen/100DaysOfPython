stuff = {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow': 12}
def displayInventory(inventory):
    totalCount = 0
    for k, v in inventory.items():
        print(v, k)
        totalCount += v
    print('Total number of items: ', totalCount)

displayInventory(stuff)

