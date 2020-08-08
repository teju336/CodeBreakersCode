#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 11:33:26 2020

@author: tejaswinis
"""

class Node:
    def __init__(self,key,value):
        self.key =key
        self.val = value
        self.next = None
    
class SeparateChainningHashmaps:
    def __init__(self,capacity):
        self.map =[Node("dummy","dummy")for _ in range (capacity)]
    
        
    def hashedIndex(self,key):
        return key % len(self.map)
    
    def get(self,key):
        idx = self.hashedIndex(key)
        cur = self.map[idx]
        while (cur.next):
            if cur.next.key == key:
                return cur.next.val
            cur = cur.next
        
    
    def put(self,key,value):
        idx = self.hashedIndex(key)
        cur = self.map[idx]
        while (cur.next):
            if cur.next.key ==key:
                cur.next.val = val
                return
            cur = cur.next
        cur.next =Node(key,value)
            
    
    def delete(self,key):
        idx = self.hashedIndex(key)
        prev = self.map[idx]
        cur = prev.next
        while (cur):
            if cur.key == key :
                prev.next = cur.next
            prev = cur 
            cur = cur.next
                
    
    def __str__(self):
        out = ""
        for idx in range(len(self.map)):
            cur = self.map[idx].next
            while(cur):
                out += str(cur.val) + " "
                cur = cur.next
            out += "\n"
        return out
    
if __name__ == '__main__':
   map =  SeparateChainningHashmaps(3)
   for i in range(10):
       map.put(i,i*2)
   print(map)
       

    
        