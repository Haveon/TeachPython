class Queue:
    def __init__(self):
        self.list = []

    def enqueue(self, element):
        self.list.append(element)

    def dequeue(self):
        assert self.size() > 0, 'Queue is empty!'    # make sure there is something to dequeue
        return self.list.pop(0)    # pop the first element of the list

    def size(self):
        return len(self.list)
