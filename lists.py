# manage list functions
import os
import redis
import json

r = redis.from_url(os.environ.get("REDIS_URL"))

lists = []
items = []

def getLists():
    # get lists from redis
    savedLists = r.get('lists')
    if savedLists == None: # lists not saved previously
        lists = []
    else:
        lists = json.loads(savedLists)
    # get items from redis
    savedItems = r.get('items')
    if savedItems == None: # items not saved previously
        items = []
    else:
        items = json.loads(savedItems)
    return True

def putLists():
    r.set('lists', json.dumps(lists))
    r.set('items', json.dumps(items))
    return True



def createList(list):
    getLists()
    if (lists.count(list) == 0):
        lists.append(list)
        items.append([])
        putLists()
        return True
    else:
        return False

def deleteList(list):
    getLists()
    if (lists.count(list) != 0):
        items.pop(lists.index(list))
        lists.remove(list)
        putLists()
        return True
    else:
        return False


def addItem(item, list):
    getLists()
    if (lists.count(list) == 0):
        return False
    else:
        items[lists.index(list)].append(item)
        putLists()
        return True
    

def removeItem(item, list):
    getLists()
    if (lists.count(list) == 0):
        return False
    elif (items[lists.index(list)].count(item) == 0):
        return False
    else:
        items[lists.index(list)].remove(item)
        putLists()
        return True

def readList(list):
    getLists()
    if (lists.count(list) == 0):
        return []
    else:
        return items[lists.index(list)]
