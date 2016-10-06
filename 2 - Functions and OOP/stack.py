class Stack:
    def __init__(self):
        self.list = list()

    def push(self, element):
        self.list.append(element)

    def pop(self):
        assert self.size() > 0, 'stack is empty'    # check there is something to pop!
        return self.list.pop()

    def size(self):
        return len(self.list)
