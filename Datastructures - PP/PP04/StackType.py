MAX_ITEMS = 100

class StackType:
    def __init__(self):
        self.info = []

    def is_empty(self):
        return len(self.info) == 0
        '''[1]'''
        
    def is_full(self):
        '''[2]'''
        return len(self.info) == MAX_ITEMS
        
    def push(self, item):
        '''[3]'''
        if(not self.is_full()):
            self.info.append(item)
        else:
            return "Stack is Full"

    def pop(self):
        '''[4]'''
        if(not self.is_empty()):
            self.info.pop(-1)
        else:
            return "Stack is Empty"

    def top(self):
        '''[5]'''
        if(not self.is_empty()):
            return self.info[-1]
        else:
            return "Stack is Empty"