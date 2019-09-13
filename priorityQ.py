## -------------------------------------------------------- ##
#   Exercise 3: Branch and Bound
#
#   Rafael Belmock Pedruzzi
#
#   priorityQ.py: implements a priority queue
## -------------------------------------------------------- ##

import heapq

heap = []

def isEmpty():
    if len(heap) == 0:
        return True
    else:
        return False

def insert(key,value):
    heapq.heappush(heap, (key,value) )

def remove():
    return (heapq.heappop(heap))[1]
