from tkinter.messagebox import NO


class NodeType:
    """ Node Type """
    def __init__(self, item):
        self.info = item
        self.next = None
        self.back = None

class DoublyLL:
    def __init__(self):
        self.head = NodeType('head')
    
    def find_item(self, item):
        '''[1]'''
        moreToSearch = True
        location = self.head
        while location.next != None:
            if location.info == item:
                return location
            else:
                location = location.next
        return location
    
    def insert_item(self, item, new):
        '''[2]'''
        location = self.find_item(item)
        if location.next == None:
            temp = NodeType(new)
            location.next = temp
            temp.back = location
        else:
            temp = location.next
            newNode = NodeType(new)
            temp.back = newNode
            location.next = newNode


    def delete_item(self, item):

        '''[3]'''
        location = self.find_item(item)
        front = location.back
        rear = location.next
        front.next = rear
        rear.back = front

            
    def __str__(self):
        cur_node = self.head
        items = []
        while cur_node is not None:
            items.append("(" + str(cur_node.info) + ")\n")
            cur_node = cur_node.next
        return "".join(items)

