# manage list functions
import os
import redis
import json

r = redis.from_url(os.environ.get("REDIS_URL"))

def getLists():
    savedLists = r.get('lists')
    if savedLists == None:
        lists = []
    else:
        lists = json.loads(savedLists)
    savedItems = r.get('items')
    if savedItems == None:
        items = []
    else:
        items = json.loads(savedItems)
    return True

def putLists()
    r.put('lists', json.dumps(lists))
    r.pub('items', json.dumps(items))
    return True



def createList(list):
    getLists()
    if (lists.count(list) == 0):
        lists.append(list)
        items.append([])
        putLists()
        return True
    else:
        print('List ' + list + ' already exists')
        return False

def deleteList(list)
    getLists()
    if (lists.count(list) != 0):
        items.pop(lists.index(list))
        lists.remove(list)
        putLists()
        return True
    else:
        print('List ' + list + ' not found')
        return False


def addItem(item, list):
    getLists()
    if (lists.count(list) == 0):
        print('List ' + list + ' not found')
        return False
    else:
        items[lists.index(list)].append(item)
        putLists()
        return True
    

def removeItem(item, list):
    getLists()
    if (lists.count(list) == 0):
        print('List ' + list + ' not found')
        return False
    elif (items[lists.index(list)].count(item) == 0):
        print('Item ' + item + ' not found on ' + list + ' list')
        return False
    else:
        items[lists.index(list)].remove(item)
        putLists()
        return True

def readList(list):
    getLists()
    if (lists.count(list) == 0):
        print('List ' + list + ' not found')
        return []
    else:
        return items[lists.index(list)]
