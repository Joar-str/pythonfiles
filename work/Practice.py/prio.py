import random


class PriorityQueue:
    def __init__(self):
        self._queue = []
    
    def __str__(self):
        return "["+",".join(["("+str(e[0])+","+str(e[1])+")" for e in self._queue])+"]"

    def enqueue(self, elem, priority):
        self._queue.append([elem, priority])
        #self._queue.sort(key=lambda x: x[1], reverse=False)          

    def dequeue(self):
        #assert(len(self._queue) > 0) 
        #return self._queue.pop()[0]

        value = None
        prio = None
        index = -1
        for i, elem in enumerate(self._queue):
            if prio == None or elem[1] > prio:
                index = i
                prio = elem[1]
        if index >= 0:
            value = self._queue.pop(index)[0]

        return value

    def front(self):
        #assert(len(self._queue) > 0)
        return self._queue.pop(0)
    
    def is_empty(self):
        empty = True
        if len(self._queue) == 0:
            empty = False
        return empty

    def __len__(self):
        return len(self._queue)
    
class Biker:
    def __init__(self, name, strength, dare):
        assert(0 <= strength <= 1)
        assert(0 <= dare <= 1)
        assert( 0<= (strength+dare) <=1)
        self._name = name
        self._strenght = float(strength)
        self._dare = float(dare)
    
    @property
    def strength(self):
        return self._strenght

    @property
    def dare(self):
        return self._dare

    @property
    def __str__(self):
        return self._name
    
    
    
class Straight:
    def __init__(self, lenght):
        self._bikers = PriorityQueue()
        self._length = float(lenght)

    def push(self, biker):
        priority = int(biker.strength*random.randint(1,40)*self._length/(1+len(self._bikers)))
        self._bikers.enqueue(biker, priority)

    def pop(self):
        return self._bikers.dequeue()
    
    def __str__(self):
        return str(self._bikers)
    
    def is_empty(self):
        return self._bikers.is_empty()

class Curve:
    def __init__(self, radius):
        self._bikers = PriorityQueue()
        self._radius = float(radius)

    def push(self, biker):
        dr = int(Biker.dare*random.randint(1,10) / (self._radius*(1+len(self._bikers))))
        self._bikers.enqueue(biker, dr)
    
    def pop(self):
        return self._bikers.dequeue()
    
    def is_empty(self):
        pass


if __name__ == "__main__":
    
    ring =[Straight(0.4), Curve(0.3), Straight(0.2), Curve(0.2), Curve(0.6), Straight(0.8)]
    bikers = [Biker("Olstam", 0.6, 0.4), Biker("Holmegard", 0.45, 0.55)]
    for biker in bikers:
        ring[0].push(biker)
    for i in range(len(ring)-1):
        while not ring[i].is_empty():
            ring[i+1].push(ring[i].pop())
    print("The winner is: "+ring[-1].pop().name)
                
