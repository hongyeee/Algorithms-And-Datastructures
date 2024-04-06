#from types import NotImplementedType


class NodeType:
    """ Node Type """
    def __init__(self, item):
        self.info = item
        self.next = None

class UnsortedType:
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

    def retrieve_item(self, item):
        location = self.listData
        found = False
        moreToSearch = location != None

        while moreToSearch and not found:
            if item == location.info:
                found = True
            else:
                location = location.next
                moreToSearch = location != None
        return found

    def insert_item(self, item):
        '''[1]'''
        if(self.length == 0):
            location = NodeType(item)
            self.listData = location
            self.currentPos = location
            self.length += 1
        else:
            location = NodeType(item)
            self.currentPos.next = location
            self.currentPos = location
            self.length += 1

    def delete_item(self, item):
        '''[2]'''
        location = self.listData
        if item == location.info:
            tempLocation = location
            self.listData = self.listData.next
        else:
            while(not(item==(location.next.info))):
                    location = location.next
            tempLocation = location.next
            location.next = (location.next).next
        del tempLocation
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
