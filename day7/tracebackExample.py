import traceback

def car():
    raise Exception("Tis is error!")

try:
    car()
except:
    errorFile = open('ErrorFile.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('Error logged into the ErrorFile.txt')

