#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 11:13:34 2020

@author: tejaswinis
"""

def selection_sort(arr):
    for i in range(len(arr)):
        min_number = arr[i]
        swap_index = i
        for j in range(i,len(arr)):
            if arr[j] < min_number:
                min_number = arr[j]
                swap_index = j
        arr[i],arr[swap_index] = arr[swap_index],arr[i]
        
            
arr1=[1,3,4,6,7,2]
print(selection_sort(arr1))
print(arr1)