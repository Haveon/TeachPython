from queue import Queue    # DRY. check queue solution to see how this works

class Stack:
    def __init__(self):
        self.mainQueue = Queue()
        self.scratchQueue = Queue()

    def push(self, element):
        self.mainQueue.enqueue(element)

    def pop(self):
        assert self.size() > 0, 'Stack is empty'
        # Now the "fun" part, we need to get the element at the back of the queue
        while self.mainQueue.size() > 1:     # will exit when only one element left
            tmp = self.mainQueue.dequeue()   # get it out of one
            self.scratchQueue.enqueue(tmp)   # put it in the other

        element = self.mainQueue.dequeue()

        # Now, the first element of the queue went into scratch, then the
        # second, and so on. That means the order of the elements has
        # remained unchanged. If we swap the labels of the queues, then
        # we'll be back where we started, minus the element at the back
        # of the queue
        self.mainQueue, self.scratchQueue = self.scratchQueue, self.mainQueue

        return element

    def size(self):
        return self.mainQueue.size()
