#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 17:16:32 2020

@author: tejaswinis
"""

class Node:
    def __init__(self,item):
        self.item = item
        self.next = None
class Queue:
    def __init__(self):
        self._size = 0
        self.head = Node("dummy")
        self.tail = self.head
    
        
    def enqueue(self,item):
        self.tail.next = Node(item)
        self.tail = self.tail.next
        self._size += 1
    
        
    def dequeue(self):
        if self.is_empty():
            print("Empty Queue")
            return 
        out = self.head.next
        self.head.next = self.head.next.next
        self._size -= 1
        
        if self.is_empty():
            self.tail = self.head
         
    def is_empty(self):
        return self.size() == 0
        
    
    def items(self):
        out =[]
        cur = self.head.next
        while cur:
            out.append(cur.item)
            cur = cur.next
        return out
    
        
    def size(self):
        return self._size

if __name__ == '__main__':
    queue = Queue()
    print(queue.is_empty())
    for i in range (3):
        queue.enqueue(i)
    print(queue.items())
    queue.dequeue()
    print(queue.items())
    