# # # # # # # # # # # # # # # # # # # 
#  LIST BASED STACK IMPLEMENTATION  #
# # # # # # # # # # # # # # # # # # # 

'''
Stack implementation - Python
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

MyStack = [] # In this version my stack starts as an empty list
StackSize = 5

def DisplayStack(): # This will display the contents of the stack using a for loop
  print("Stack currently contains:")
  if len(MyStack) > 0:
    for Item in MyStack:
      print(Item)
  else:
    print('undefined')
def Push(Value): # This is the push function which will insert items into the stack
  if len(MyStack) < StackSize:
    MyStack.append(Value)
  else:
    print("Stack is full!")
def Pop(): # this will pop from the stack using the .pop() method that removes the latest entry from a list
  if len(MyStack) > 0:
    MyStack.pop()
  else:
    print("Stack is empty.")

# Now I can start pushing things into the data structure as I run the program
Push(1)
Push('b')
Push(3)
Push(7)
DisplayStack() # this displays the contents of the stack
input("Press any key when ready...")
# Now we are going to 'overfill' the poor stack to test the error string
Push(5)
Push(6)
DisplayStack() 
input("Press any key when ready...")
# Now lets start popping
Pop()
Pop()
DisplayStack()
input("Press any key when ready...")
# Ok let's pop it to empty and see what happens
Pop()
Pop()
Pop()
DisplayStack()
