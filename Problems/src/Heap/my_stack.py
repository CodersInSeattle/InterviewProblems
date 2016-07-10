from heapq import heappush, heappop


class MyStack(object):
    def __init__(self):
        self.items = []
        self.priority = 0

    def push(self, element):
        heappush(self.items, (self.priority, element))
        self.priority -= 1

    def pop(self):
        _, data = heappop(self.items)
        return data

    def peek(self):
        return self.items[0]
