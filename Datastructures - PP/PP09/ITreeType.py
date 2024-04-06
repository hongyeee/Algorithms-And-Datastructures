
class NodeType:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

class IterBST():
    def __init__(self):
        self.root = None
        self.order_list = []

    def insert(self, data):
        '''[10]'''
        tempPtr = self.find_node(self.root, data)
        if tempPtr == None:
            self.root = NodeType(data)
        elif data < tempPtr.info:
            tempPtr.left = NodeType(data)
        else:
            tempPtr.right = NodeType(data)

    def find(self, key):
        '''[11]'''
        temp = self.root
        pre = None
        found = False
        while temp != None and not found:
            if key < temp.info:
                pre = temp
                temp = temp.left
            elif key > temp.info:
                pre = temp
                temp = temp.right
            else:
                found = True
        return pre

    def find_node(self, root, key):
        '''[12]'''
        temp = root
        pre = None
        found = False
        while temp != None and not found:
            if key < temp.info:
                pre = temp
                temp = temp.left
            elif key > temp.info:
                pre = temp
                temp = temp.right
            else:
                found = True
        return pre

    def delete(self, key):
        '''[13]'''
        temp = self.root
        pre = None
        while temp != None:
            if key < temp.info:
                pre = temp
                temp = temp.left
            elif key > temp.info:
                pre = temp
                temp = temp.right
            else:
                self.delete_node(pre, key)
                break

    def delete_node(self, node, key):
        '''[14]'''
        if key < node.info:
            temp = node.left
        else:
            temp = node.right
        if temp.left == None and temp.right == None:
            if key < node.info:
                node.left = None
            else:
                node.right = None
        elif temp.left == None:
            temp.info = temp.right.info
            temp.right = None
        elif temp.right == None:
            temp.info = temp.left.info
            temp.left = None
        else:
            data = self.get_predecessor(temp.left, key)
            temp.info = data
            self.delete(data)
        
    def inorder(self, node):
        '''[15]'''
        if not node == None:
            self.inorder(node.left)
            self.order_list.append(node.info)
            self.inorder(node.right)
    
    def preorder(self, node):
        '''[16]'''
        if not node == None:
            self.order_list.append(node.info)
            self.preorder(node.left)
            self.preorder(node.right)
    
    def postorder(self, node):
        '''[17]'''
        if not node == None:
            self.postorder(node.left)
            self.postorder(node.right)
            self.order_list.append(node.info)

    def get_predecessor(tree, data):
        '''[18]'''
        while not tree.right == None:
            tree = tree.right
        data = tree.info

