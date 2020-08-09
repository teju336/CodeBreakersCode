#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 19:56:39 2020

@author: tejaswinis
"""

class LRUCache:

    def __init__(self, capacity: int):
        self.d = dict()
        self.c = capacity

    def get(self, key: int) -> int:
        if key in self.d:
            val = self.d[key]
            del self.d[key]
            self.d[key] = val
            return self.d[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            del self.d[key]
            self.d[key] = value
            return
        if self.c == 0:
            del self.d[next(iter(self.d))]
        else:
            self.c -= 1
        self.d[key] = value
        
if __name__ == "__main__":
        cache = LRUCache(2);
        print (cache.put(1, 1));
        print (cache.put(2, 2));
        print (cache.get(1));       
        print (cache.put(3, 3));    #// evicts key 2
        print (cache.put(4, 4));    #// evicts key 1
        print (cache.get(1));       #// returns -1 (not found)
        print (cache.get(3));       #// returns 3
        print (cache.get(4));   
        #/ returns 4
        