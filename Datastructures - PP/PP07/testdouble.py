from double import *


if __name__ == '__main__':


    doubly = DoublyLL()
    
    doubly.insert_item('head', '1')
    doubly.insert_item('1', '2')
    doubly.insert_item('2', '3')
    doubly.insert_item('3', '4')
    
    print(doubly)
    doubly.delete_item('2')
    doubly.delete_item('3')
    print(doubly)
