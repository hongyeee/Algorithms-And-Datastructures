from enum import Enum
from lib2to3.pgen2.token import EQUAL, GREATER, LESS

MAX_ITEMS = 100

class Compare(Enum):
    LESS = 0
    GREATER = 1
    EQUAL = 2
    
class ItemType:
    """ Item Type """

    def __init__(self, val):
        """ [1] """
        self.value = val

    def compared_to(self, otherItem):
        """ [2] """
        if(self.value < otherItem.value) : 
            return LESS
        elif(self.value >otherItem.value):
            return GREATER
        else:
            return EQUAL
    def __str__(self):
        """ [3] """
        return str(self.value)

class SortedType:
    """ Chapter 3: Sorted List """
    def __init__(self):
        """ [4] """
        self.length = 0
        self.info = []


    def make_empty(self):
        self.length = 0

    def length_is(self):
        return self.length

    def is_full(self):
        if self.length == MAX_ITEMS:
            return True
        return False

    def insert_item(self, item):
        """ [5] """
        location = 0;
        moreToSearch = (location < self.length)
        self.info.append(0)

        while (moreToSearch):
            if(item.compared_to(self.info[location]) == LESS):
                moreToSearch = False
            elif(item.compared_to(self.info[location]) == GREATER):
                location += 1
                moreToSearch = (location < self.length)
        for index in range(self.length, location, -1):
            self.info[index] = self.info[index-1]
        self.info[location] = item
        self.length += 1


    def retrieve_item(self, item): # Binary Search
        """ [6] """
        first = 0
        last = self.length -1
        moreToSearch = (first <= last)
        found = False

        while(moreToSearch and not found):
            midPoint = (first + last) // 2

            if(item.compared_to(self.info[midPoint]) == LESS):
                last = midPoint -1
                moreToSearch = (first <= last)
            elif(item.compared_to(self.info[midPoint]) == GREATER):
                first = midPoint +1
                moreToSearch = first <= last
            elif(item.compared_to(self.info[midPoint]) == EQUAL):
                found = True
                item = self.info[midPoint]
                break
        return found


    def delete_item(self, item):
        """ [7] """
        location = 0
        while (item.compared_to(self.info[location]) != EQUAL):
            location += 1
        for index in range(location+1, self.length, 1):
            self.info[index-1] = self.info[index]
        self.length -= 1

    def reset_list(self):
        self.current_pos = -1

    def get_next_item(self):
        self.current_pos += 1
        return self.info[self.current_pos]

    def __str__(self):
        """ [8] """
        print_sen = ""
        for index in range(0, self.length, 1):
            print_sen += str(self.info[index])+ " "
        return str(print_sen)
