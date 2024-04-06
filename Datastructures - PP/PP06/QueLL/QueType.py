#from curses.ascii import NUL


class NodeType:
    """ Node Type """
    def __init__(self, item):
        self.info = item
        self.next = None

class QueType:
    def __init__(self):
        self.front = None
        self.rear = None

    def make_empty(self):
        while self.front != None:
            tempPtr = self.front
            self.front = self.front.next
            del tempPtr
        self.rear = None

    def is_full(self):
        try:
            location = NodeType("test")
            del location
            return False
        except:
            return True

    def is_empty(self):
        return self.front == None

    def enqueue(self, item):
        '''[7]'''
        if(self.is_full()):
            return
        else:
            temp = NodeType(item)
            if(self.rear == None):
                self.front = temp
            else:
                self.rear.next = temp
            self.rear = temp


    def dequeue(self):
        '''[8]'''
        if(self.is_empty()):
            return
        else:
            tempPtr = self.front
            item = self.front.info
            self.front = self.front.next
            if(self.front == None):
                rear = None
            del tempPtr
            return item


        
