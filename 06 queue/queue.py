# # # # # # # # # # # # #
#  Queue implementation #
# # # # # # # # # # # # #

'''
A queue is an abstract data type that serves as a collection of elements, with two principal operations: enqueue, which adds an element to the collection, and dequeue, which removes the earliest added element. The order in which elements are dequeued is First In First Out aka. FIFO. The term queue takes it name from the real world queues e.g. "a queue at the ticket counter".
FIFO Queue

Factors to keep in mind for higher scores:

push and shift Javascript implementations may seem easy, but are not actually the fastest as they have an average runtime of 0(n) instead of the fastest 0(1) operation cost.
Consider tracking the nextEnqueueIndex and lastDequeuedIndex which we initialize to 0.
In short the implementation is simply maintaining a map and tracking our queue and dequeue indexes within the enqueue and dequeue methods.
Add a size function which returns the number of elements in the queue.
'''

class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, items):
        return self.items.insert(0,items)
    
    def isEmpty(self):
        return self.items == []
    
    def dequeue(self):
        return self.items.pop()
        
    def size(self):
        return len(self.items)
        
    def peek(self):
        return self.items[len(self.items)-1]

    
q = Queue()
print('Will print True:')
print(q.isEmpty())
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print('Will print 5 as there are 5 items in the queue:')
print(q.size())
print('Will remove 1 as this was the first in and this is a FIFO data structure:')
print(q.dequeue())
print('Will now print 4 as there are 4 items left:')
print(q.size())
print('This time the peek will peek out 2 as it is the next item at the end of the list ie. to fall out:')
print(q.peek())
print('Now we can take out number 2:')
print(q.dequeue())
print('Now we can display the size which is obviously three now:')
print(q.size())
