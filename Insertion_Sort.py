#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 11:00:53 2020

@author: tejaswinis
"""

def insertion_sort(arr):
    for i in range(1,len(arr)):
        for j in range(i,0,-1):
            if arr[j] < arr[j-1]:
                arr[j],arr[j-1] = arr[j-1], arr[j]
            else:
                break
            
arr1=[1,3,4,6,7,2]
print(insertion_sort(arr1))
print(arr1)