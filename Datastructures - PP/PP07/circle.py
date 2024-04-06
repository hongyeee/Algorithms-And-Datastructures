from hashlib import new
#from itertools import Predicate


class NodeType:
    """ Node Type """
    def __init__(self, item):
        self.info = item
        self.next = None

class CircularLL:
    def __init__(self):
        self.listData = None
        self.length = 0
        self.currentPos = None

    def is_full(self):
        try:
            location = NodeType("test")
            return False
        except:
            return True

    def length_is(self):
        return self.length

    def make_empty(self):
        while self.listData != None:
            tempPtr = self.listData.next
            del self.listData
            self.listData = tempPtr
        self.length = 0

    def find_item(self, listData, item):

        '''[4]'''
        moreToSearch = True
        location = listData.next
        preloc = listData

        while moreToSearch:
            if item <= location.info:
                moreToSearch = False
            else:
                preloc = location
                location = location.next
                moreToSearch = (location != listData.next)
        return preloc
            
    def insert_item(self, item):

        '''[5]'''
        newNode = NodeType(item)

        if self.length == 0:
            self.listData = newNode
            newNode.next = newNode
        else:
            preloc = self.find_item(self.listData, item)
            newNode.next = preloc.next
            preloc.next = newNode
            location = NodeType(item)
            if self.listData.info <item:
                self.listData = newNode
        self.length += 1


    def delete_item(self, item):

        '''[6]'''
        preloc = self.find_item(self.listData, item)
        location = preloc.next
        if preloc == location:
            self.listData = None
        else:
            preloc.next = location.next
            if location == self.listData:
                self.listData = preloc
        del location
        self.length -= 1

    def reset_list(self):
        self.currentPos = None

    def get_next_item(self):
        if self.currentPos == None:
            self.currentPos = self.listData
        else:
            self.currentPos = self.currentPos.next
        return self.currentPos.info

    def __str__(self):
        self.reset_list()
        items = []
        for i in range(0, self.length):
            t = self.get_next_item()
            items.append(str(t))
        return " ".join(items)
