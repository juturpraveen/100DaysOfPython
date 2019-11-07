def printPicnic(itemsDict, leftwidth, rightwidth):
    print('PICNIC TABLE'.center(leftwidth+rightwidth, '*'))
    for k, v in itemsDict.items():
        print(k.ljust(leftwidth,'.')+str(v).rjust(rightwidth,'.'))

picnicItems = {'sandwiches':4, 'apples':12, 'cups':10, 'cookies':1000}
printPicnic(picnicItems, 10, 10)