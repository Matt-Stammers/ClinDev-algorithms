# # # # # # # # # # # # # # # # # # # # # # #
#  PYTHON CLASS BASED STACK IMPLEMENTATION  #
# # # # # # # # # # # # # # # # # # # # # # #

'''
Stack implementation
=========================
A stack is an abstract data type that stores a collection of elements, with two principal operations:
push: adds an element to the collection
pop: removes the most recently added element that was not yet removed. The order in which elements are poped is Last In First Out aka. 

 LIFO.
LIFO Stack

A stack is a Last in First out (LIFO) with key operations having a time complexity of O(1).

It will have two key operations.
The first one is push which adds an item into the stack.
The other key operation pops an item from the stack. If there are no more items we can return an out of bound value like undefined.

Factors to keep in mind for higher scores:
Add a size method that allows you to safely find out if there are any elements present in the data structure.
'''
    
# so that last functional method was ok, but compared to this OOP method it was weak. This stack is WaaaaY better!
    
class Hay_Stack: # so first you have to initiate the stack class. Mine is going to be a Hay_Stack! Anyone seen my tractor perchance?
     def __init__(self): # this initialises the stack by default as an empty list object
         self.items = []

     def push(self, item): # this will .append() items to the stack
         self.items.append(item)

     def pop(self): # this will .pop() the items from the stack in Last In First Out (LIFO) order as per the .pop() method
         return self.items.pop()

     def peek(self): # this will show us the most recent item to go into the stack
         return self.items[len(self.items)-1]

     def size(self): # this will return the length of the stack
         return len(self.items)
         
     def isEmpty(self): # this will return the empty stack
         return self.items == []
         
# so first we can instantiate a class object, in this case s which is an instance of Hay_Stack()       
s=Hay_Stack()
# let's first check if our bound object methods are working correctly. As the stack is empty this will return True at present.
print(s.isEmpty())
# now let's push something in:
s.push('Clinical_Developer')
# and something else:
s.push(10000)
# let's take a look at our little stack! In your own environment with the above package it would print 'clin_dev' and 10000
print(s.peek())
# let's push in a bool and a float for good measure.
s.push(True)
s.push(1.334)
# this will print 4:
print(s.size())
# this will print False as the stack now contains 4 items.
print(s.isEmpty())
s.push(8.4)
# this will remove 8.4 and print it to the console
print(s.pop())
# this will remove the float and print it to the console
print(s.pop())
# this will remove the bool and print it to the console
print(s.pop())
# this will remove the 10000 int and print it to the console as it is removed...
print(s.pop())
# all you are left with is a 'clin_dev' in the stack ;)
print(s.size())
# let's take a peek:
print(s.peek())

# Tada, I hope you can see how powerful class based stacks are in comparison with purely functional / list based ones
