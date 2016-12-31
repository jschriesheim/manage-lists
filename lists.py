# manage list functions

lists = []
items = []

def createList(list):
    if (lists.count(list) == 0):
        lists.append(list)
        items.append([])
        return True
    else:
        print('List ' + list + ' already exists')
        return False

def deleteList(list):
    if (lists.count(list) != 0):
        items.pop(lists.index(list))
        lists.remove(list)
        return True
    else:
        print('List ' + list + ' not found')
        return False


def addItem(item, list):
    if (lists.count(list) == 0):
        print('List ' + list + ' not found')
        return False
    else:
        items[lists.index(list)].append(item)
        return True
    

def removeItem(item, list):
    if (lists.count(list) == 0):
        print('List ' + list + ' not found')
        return False
    elif (items[lists.index(list)].count(item) == 0):
        print('Item ' + item + ' not found on ' + list + ' list')
        return False
    else:
        items[lists.index(list)].remove(item)
        return True

def readList(list):
    if (lists.count(list) == 0):
        print('List ' + list + ' not found')
        return []
    else:
        return items[lists.index(list)]
