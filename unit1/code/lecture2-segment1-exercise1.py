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

    With two bags there thus must be 3**n possible combinations. 
    You can imagine this by representing the two bags as a list 
    of "trinary" bits, 0, 1, or 2 (a 0 if an item is in neither 
    bag; 1 if it is in bag1; 2 if it is in bag2). With the "trinary" bits, 
    there are N bits that can each be one of three possibilities - 
    thus there must be 3**n possible combinations.  

    The idea here is that x >> y it's equal to x//2**y so to emulate
    ternary digits we do x//3**y      

    """
    N = len(items)

    # enumerate all the 3 possibles combinations
    for i in range(3**N):

        bag1 = []
        bag2 = []
        for j in range(N):
            # floor divison it's equal to 0, 1 or 2
            floor = i // (3**j)

            if (floor % 3 == 1):
                bag1.append(items[j])
            elif (floor % 3 == 2):
                bag2.append(items[j])

        yield (bag1, bag2)


items = ['a', 'b', 'c', 'd']

foo = yieldAllCombos(items)

for i in foo:
    print(i)
