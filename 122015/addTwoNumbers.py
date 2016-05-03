# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 11:19:45 2015

@author: agoswami
"""

#https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        sumRoot = None
        
        p1 = l1
        p2 = l2
        
        r = 0
        while p1 is not None and p2 is not None: 
            s = p1.val + p2.val + r
            if s > 9:
                r = 1
                v = s % 10
            else:
                r = 0
                v = s
            
            sumRoot = insert(sumRoot, v)
            p1 = p1.next
            p2 = p2.next
        
        if p1 is not None:
            while p1 is not None:
                s = p1.val + r
                if s > 9:
                    r = 1
                    v = s % 10
                else:
                    r = 0
                    v = s
            
                sumRoot = insert(sumRoot, v)
                p1 = p1.next

        if p2 is not None:
            while p2 is not None:
                s = p2.val + r
                if s > 9:
                    r = 1
                    v = s % 10
                else:
                    r = 0
                    v = s
            
                sumRoot = insert(sumRoot, v)
                p2 = p2.next

        if r == 1:
            sumRoot = insert(sumRoot, 1)
            
        return reverse(sumRoot)
        

def insert(root, x): 
    if root is None:
        root = ListNode(x)
        return root
        
    node = ListNode(x)
    node.next = root
    return node

def reverse(root):
    previous = None
    current = root
    while current is not None:
        temp = current.next
        current.next = previous
        previous = current
        current = temp
    
    return previous
         
def show(root):
    while True:
        print "{0}->".format(root.val),
        if root.next is None:
            print "End"
            break        
        
        root = root.next
        
        
if __name__ == "__main__":
    l1 = None
    l1 = insert(l1, 9)
    l1 = insert(l1, 9)
    l1 = insert(l1, 3)
    l1 = insert(l1, 6)
    show(l1)
    
    l2 = None
    l2 = insert(l2, 6)
    l2 = insert(l2, 4)
    show(l2)
    
    s = Solution()
    soln = s.addTwoNumbers(l1, l2)
    show(soln)