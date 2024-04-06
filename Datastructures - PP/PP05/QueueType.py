MAX_ITEMS = 100

class QueueType():
    def __init__(self):
        self.info = []
        self.front = -1
        self.rear = -1;

    def enqueue(self, data):
        '''[1]'''
        self.rear += 1
        self.info.append(data)

    def dequeue(self):
        '''[2]'''
        self.front += 1
        return (self.info[self.front])

    def is_empty(self):
        '''[3]'''
        return (self.front == self.rear)

    def is_full(self):
        '''[4]'''
        return (self.rear == MAX_ITEMS -1)

    def make_empty(self):
        '''[5]'''
        self.front = -1
        self.rear = -1