# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 12:45:41 2016

@author: yagnesh
"""
class BinarySearchTreeNode:
    # Node for Binary Search Tree
    def __init__(self, key, value, parent=None, left=None, right=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
        
class BinarySearchTree:
    
    def __init__(self):
        self.root = None
        
    def insert(self, key, value):
        #Root node        
        if None == self.root:
            self.root = BinarySearchTreeNode(key, value)
            return True
            
        currentnode = self.root
        
        while currentnode:
            if key == currentnode.key:
                print("Key present in the tree")
                return False
            elif key < currentnode.key:
                if currentnode.left:
                    currentnode = currentnode.left
                else:
                    currentnode.left = BinarySearchTreeNode(key, value, currentnode)
                    return True
            else:
                if currentnode.right:
                    currentnode = currentnode.right
                else: 
                    currentnode.right = BinarySearchTreeNode(key, value, currentnode)
                    return True

    def findkey(self, node, key):
        #Search key from node        
        if None == node or key == node.key:
            #print(currentnode.key, leftcount, rightcount)
            return node
        elif key < node.key:
            return self.findkey(node.left, key)
        else:
            return self.findkey(node.right, key)
        
    def search(self, key):
        return self.findkey(self.root, key)
        
    def replacenode(self, node, new_node):
        parent = node.parent
        # special case: replace the root
        if node == self.root:
            self.root = new_node
            return
        if parent.left and parent.left == node:
            parent.left = new_node
        elif parent.right and parent.right == node:
            parent.right = new_node
        else:
            print("Incorrect parent-children relation!")
            raise RuntimeError
    
    def removenode(self, node):
        '''
        There are three cases to consider when looking for the successor:

        - If the node has a right child, then the successor is the smallest key in the right subtree.
        - If the node has no right child and is the left child of its parent, then the parent is the successor.
        - If the node is the right child of its parent, and itself has no right child, then the successor to this node is the successor of its parent, excluding this node.
        '''
        if node.left and node.right:
        #If node has two child
            succesor = node.right
            while succesor.left:
                succesor = succesor.left
            node.key = succesor.key
            node.value = succesor.value
            self.removenode(succesor)
        elif node.left:
            #print("left",node.parent)            
            self.replacenode(node, node.left)
        elif node.right:
            #print("right",node.parent)            
            self.replacenode(node, node.right)
        else:
            #print("leaf", node.parent)
            self.replacenode(node, None)
    
    
    def delete(self, key):
        node = self.search(key)
        if node:
            self.removenode(node)
            

mytree = BinarySearchTree()
mytree.insert(4,30)
mytree.insert(2,40)
mytree.insert(1,1000)
mytree.insert(40,50)
mytree.insert(5,13)
mytree.insert(10,4)
mytree.delete(10)
mytree.search(10)

        
                    
            
