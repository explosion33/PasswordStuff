def create(fileName):
    file = open(fileName + ".txt", 'a')
    file.close()

def save(fileName, text):
    file = open(fileName + ".txt", 'a')
    file.write(str(text) + "\n")
    file.close()

def read(fileName):
    file = open(fileName + ".txt", 'r')
    read = file.read()
    return read
def search(fileName, key):
    file = open(fileName + ".txt", 'r')
    i = 0
    for x in file:
        if str(x) == key + "\n":
            return i
        
        i += 1
def createList(fileName):
    lest = []
    file = open(fileName)
    lest = file.readlines
    return lest 




    