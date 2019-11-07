def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be single character string.')
    if width <= 2:
        raise Exception('Width must be greater that 2')
    if height <= 2:
        raise Exception('Height must be greater than 2')
    print(symbol * width)
    for i in range(height-2):
        print(symbol+(' '*(width - 2))+symbol)
    print(symbol * width)

for sym,w,h in (('*', 4, 4), ('00', 20, 5), ('x',1,5), ('z',3,3)):
    try:
        boxPrint(sym,w,h)
    except Exception as err:
        print('An exception has occured:' ,err)
