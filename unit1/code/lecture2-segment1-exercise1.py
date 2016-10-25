#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 20:11:52 2016

@author: ronaldo
"""

# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo
    

def yieldAllCombos(items):
    
    """ Generates all combinations of N item into two bags, whereby each 
    item  is in one or zero bags.

    Yields a tuple, (bag1, bag2), where each bag is represented as 
    a list of which items(s) are in each bag        

