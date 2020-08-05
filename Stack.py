#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 09:10:08 2020

@author: tejaswinis
"""

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
class Stack:
    def __init__(self):
        self.first_item = None
        self._size=0
    
    def __str__(self):
        cur = self.first_item
        out =""
        while cur:
            out += str(cur.val)+"|"
            cur =cur.next
        return out
            
    def push(self,item):
        old_first_item = self.first_item
        self.first_item =Node(item)
        self.first_item.next =  old_first_item 
        self._size +=1

    def pop(self):
        if is_Empty ():
            return 
        old_first_item = self.first_item
        self.first_item = self.first_item.next 
        self._size -= 1
        
    def is_Empty(self):
        return self.size() == 0
    
    def size(self):
        return self._size
    
if __name__ == '__main__':
    stack =Stack()
    for i in range (5):
        stack.push(i)
    print(stack)

        
        