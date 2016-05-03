# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 22:08:06 2015

@author: agoswami
"""

# implement a queue using as many stacks as needed
# queue operations = enque(), dequeue()
# stack operations = push(), pop(), top()

class Queue():
    def __init__(self):
        self.head = -1
        self.elements = []

    def deque(self):
        if (self.head + 1 == len(self.elements)):
            raise ValueError("Trying to deque an empty queue")

        self.head += 1
        return self.elements[self.head]        
        
    def enque(self, x):
        self.elements.append(x)

    def displayQueue(self):
        print "Queue Contents : ",
        for i in range(len(self.elements) - 1, self.head, -1):
            print self.elements[i],
    
        print "."

class Queue2():
    def __init__(self):
        self.insertS = Stack()
        self.readS = Stack()

    def deque(self):
        if self.readS.topIndex() < 0:
            raise ValueError("Trying to deque an empty queue")
        else:
            return self.readS.pop()
        
    def enque(self, x):
        while (self.readS.topIndex() != -1):
            v = self.readS.pop()
            self.insertS.push(v)
            
        self.insertS.push(x)
        
        while (self.insertS.topIndex() != -1):
            v = self.insertS.pop()
            self.readS.push(v)

    def displayQueue(self):
        self.readS.displayStack()

class Stack():
    def __init__(self):
        self.top = -1
        self.elements = []
        
    def push(self, x):
        self.top += 1
        if self.top == len(self.elements): 
            self.elements.append(x)
        else:
            self.elements[self.top] = x
        
    def pop(self):
        if self.top < 0:
            raise ValueError("Trying to pop from an empty stack")
        
        self.top -= 1
        return self.elements[self.top + 1]

    def topIndex(self):
        return self.top

    def displayStack(self):
        print "Stack Contents : ",
        for i in reversed(range(self.top + 1)):
            print self.elements[i],

        print "."

if __name__ == "__main__":
    
    q1 = Queue()  
    try:
        q1.enque(20)
        q1.enque(30)
        q1.enque(10)
        q1.displayQueue()
        q1.enque(40)
        q1.displayQueue()
        q1.deque(), q1.deque(), q1.deque()
        q1.displayQueue()
        q1.deque()
        q1.displayQueue()
    except Exception as e:
        print e.message
    
    print "-------------------"
    
    q2 = Queue2()  
    try:
        q2.enque(20)
        q2.enque(30)
        q2.enque(10)
        q2.displayQueue()
        q2.enque(40)
        q2.displayQueue()
        q2.deque(), q2.deque(), q2.deque()
        q2.displayQueue()
        q2.deque()
        q2.displayQueue()
    except Exception as e:
        print e.message
    
    s1 = Stack()
    try:
        s1.push(10)
        s1.push(20)
        s1.displayStack()
        s1.pop()
        s1.displayStack()
        s1.push(15)
        s1.displayStack()
        s1.pop()
        s1.displayStack()
    except Exception as e:
        print "Error : {0}".format(e.message)