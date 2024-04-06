from tkinter import N


class TreeNode:

    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
    
class BST():

    def __init__(self):
        self.root = None
        self.order_list = []
    
    def is_empty(self):
        return (self.root == None)
    
    def count_nodes(self, tree):
        '''[1]'''
        if tree == None:
            return 0
        else:
            return self.count_nodes(tree.left) + self.count_nodes(tree.right) +1

    def length_is(self):
        return self.count_nodes(self.root)

    def insert(self, item):
        '''[2]'''
        if self.root == None:
            self.root = TreeNode(item)
        elif item < self.root.info:
            if(self.root.left == None):
                self.root.left = TreeNode(item)
            else:
                self.insert_item(self.root.left, item)
        else:
            if(self.root.right == None):
                self.root.right = TreeNode(item)
            else:
                self.insert_item(self.root.right, item)


    def insert_item(self, node, item):
        '''[3]'''
        if node == None:
            node = TreeNode(item)
        elif item < node.info:
            if(node.left == None):
                node.left = TreeNode(item)
            else:
                self.insert_item(node.left, item)
        else:
            if(node.right == None):
                node.right = TreeNode(item)
            else:
                self.insert_item(node.right, item)

    def inorder(self, node):
        '''[4]'''
        if not node == None:
            self.inorder(node.left)
            self.order_list.append(node.info)
            self.inorder(node.right)
    
    def preorder(self, node):
        '''[5]'''
        if not node == None:
            self.order_list.append(node.info)
            self.preorder(node.left)
            self.preorder(node.right)
    
    def postorder(self, node):
        '''[6]'''
        if not node == None:
            self.postorder(node.left)
            self.postorder(node.right)
            self.order_list.append(node.info)

    def delete(self, item):
        '''[7]'''
        tempPtr = self.delete_node(self.root, item)
        if tempPtr != None:
            if item < tempPtr.info:
                nodePtr = tempPtr.left
            elif item > tempPtr.info:
                nodePtr = tempPtr.right
            if nodePtr.left == None and nodePtr.right == None:
                if item < tempPtr.info:
                    tempPtr.left = None
                else:
                    tempPtr.right = None
            elif nodePtr.left == None:
                nodePtr.info = nodePtr.right.info
                nodePtr.right = None
            elif nodePtr.right == None:
                nodePtr.info = nodePtr.left.info
                nodePtr.left = None
            else:
                data = self.get_predecessor(nodePtr.left, item)
                nodePtr.info = data
                self.delete(data)
    
    def delete_node(self, current, item):
        '''[8]'''
        if current == None:
            return None
        elif item < current.info:
            if current.left.info == item:
                return current
            else:
                return self.delete_node(current.left, item)
        else:
            if current.right.info == item:
                return current
            else:
                return self.delete_node(current.right, item)


    def get_predecessor(tree, data):
        '''[9]'''
        while not tree.right == None:
            tree = tree.right
        data = tree.info
        
