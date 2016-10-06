from stack import Stack    # DRY. check the stack solution to see how this works

class Queue:
    def __init__(self):
        self.mainStack = Stack()
        self.scratchStack = Stack()

    def enqueue(self, element):
        self.mainStack.push(element)

    def dequeue(self):
        assert self.size() > 0, 'Queue is empty'
        # Now the "fun" part, we need to get the element at the bottom of the stack
        while self.mainStack.size() > 1:  # Will exit when only one element left
            tmp = self.mainStack.pop()    # get it out of one
            self.scratchStack.push(tmp)   # put it in the other

        element = self.mainStack.pop()

        # Now the top of the main stack went into the bottom of the scratch
        # stack. This means that we have actually reversed the order of the
        # stack. We're going to put it back the way it was

        while self.scratchStack.size() > 0:   # Exit when the stack is empty
            tmp = self.scratchStack.pop()     # out of one again
            self.mainStack.push(tmp)          # and into the other

        return element

    def size(self):
        return self.mainStack.size()
