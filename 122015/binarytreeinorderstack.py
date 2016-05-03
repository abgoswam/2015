# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 00:41:47 2015

@author: agoswami
"""

# write function to print binary tree in order, without using recursion
# ..given a stack object
# Stack
#    pop
#    push
#    top

import numpy as np

class Stack:
    def __init__(self):
        self.arr = [TreeNode(i) for i in np.zeros(100)]
        self.top = -1

    def pop(self):
        if self.top < 0:
            return None
            
        
        node = self.arr[self.top]
        self.top -= 1
        return node

    def push(self, node):
        if (self.top + 1 >= len(self.arr)):
            return False
        
        self.top += 1
        self.arr[self.top] = node
        return True


class TreeNode:
    def __init__(self, v):
        self.value = v
        self.left = None
        self.right = None

def insert(root, v):
    if root is None:
        root = TreeNode(v)
        return root
        
    if v <= root.value:
        root.left = insert(root.left, v)
    else:
        root.right = insert(root.right, v)
        
    return root

def inorder(root):
    if root is None:
        return
        
    inorder(root.left)
    print root.value
    inorder(root.right)
    
    
def inorderStack(root):
    
    s = Stack()    
    node = root

    while(True):
        if node:        
            s.push(node)
            while node.left:
                s.push(node.left)
                node = node.left
                
        popedNode = s.pop()  
        if popedNode:
            print popedNode.value
            node = popedNode.right
        else:
#            Nothing else left to pop
            break



if __name__ == "__main__":
    
#    -------Tree Practise ------
    print "This only executes when %s is executed rather than imported" % __file__
    vals = [100, 50, 200, 25, 30, 75, 150, 120, 250, 220]
    root = None
    
    for item in vals:
        print item
        root = insert(root, item)
        
    print "Display values in in-order using recursion : "
    inorder(root)
    
    print "Display values in in-order using stack : "
    inorderStack(root)