# This is the implementation lifted from interactivepython.org, it's awesome:

# First create the instance of the Deque class:

class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
        
# Then hold the characters in the string in a deque object and remove them one by one

def palchecker(aString):
    chardeque = Deque()

    for ch in aString: # add the characters one by one to the rear
        chardeque.addRear(ch)

    stillEqual = True # initialise stillEqual object as True

    while chardeque.size() > 1 and stillEqual: # loop over the structure while it is > 1 in size and stillEqual (the test) is still True
        first = chardeque.removeFront() # remove from the front
        last = chardeque.removeRear() # remove from the rear
        if first != last: # as soon as the front item no longer equals the rear item
            stillEqual = False # = game over its not a Palindrome

    return stillEqual

print(palchecker("lsdkjfskf"))
print(palchecker("radar"))
print(palchecker("12345"))
print(palchecker("12321"))
print(palchecker("afadafaasdfa"))
print(palchecker("morrom"))

# This is super simple and works really really fast. I love this implementation. 
