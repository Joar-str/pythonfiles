from collections import deque

# x = set([4, 2, 9, 3, 1])
# y = set([5, 4, 8])

# print(x.union(y))
# print(x.difference(y))
# print(x.intersection(y))

class Queue:
    def __init__(self):
        self._values = deque() # Skapar en tom lista

    def enqueue(self, value):
        self._values.append(value) # Lägger till ett värde till höger (sist) i listan

    def dequeue(self):
        assert(len(self._values) > 0)
        return self._values.popleft() # Tar bort och returnerar värdet till vänster (först) i listan.

    def front(self):
        assert(len(self._values) > 0)
        return self._values[0] # Returnerar första värdet i listan

    def __len__(self): # Gör att vi kan använda len-funktionen på kö-objektet
        return len(self._values) 

    def __str__(self): #Gör att vi kan få en strängrepresentation av kön.
        return str(self._values)
    
#     #Uppgift A

val = [1,2,3,4,5,6,7]
q = Queue()
for ele in val:
    q.enqueue(ele)
print(q._values)
print(q.__len__())

# class Stack:
#     def __init__(self):
#         self._queue = []

#     def push(self, item):
#         self._queue.append(item)

#     def pop(self):
#         return self._queue.pop(0)
    
#     def top(self):
#         return self._queue[0]
    
# val = [1,2,3,4,5,6,7]
# q = Stack()
# for ele in val:
#     q.push(ele)
#     print(q.pop())

        
