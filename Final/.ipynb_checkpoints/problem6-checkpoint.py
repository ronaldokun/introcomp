#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 22:01:53 2016

@author: ronaldo
"""
import numpy as np

from itertools import *


def possibleBins(choices):
    """
    choices: a non-empty list of ints
    
    Returns a list with 
    
    the power set of 0's and 1's of len(choices), e.g. 2**len(choices)
    
    e.g. choices= [1,2,3] -> [0,0,0], [1,0,0], [0,1,0], [0,0,1], [1,1,0] ,
                             [1,0,1], [0,1,1], [1,1,1]
    
    """
    
    comb = [] 
    
    for i in range(len(choices)):
        array = len(choices) * [0]
        for j in range(i+1):
            array[j] = 1
        comb = comb + [i for i in permutations(array)]

    comb = set(comb)
    
    return comb
    
    
def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    
    # I could find an implementation which uses this hint gave at the 
    # exercise:
    # choices = np.array([bin(i)[2:] for i in choices])

    choices = np.array(choices)
    
    combinations = possibleBins(choices)
    
    # Initialize the best values
    maxValue = 0
    
    bestComb = np.array([0] * len(choices))
    
        
    for comb in combinations:
        
        # The purpose of this function is to maximize this value and minimize
        # the sum of true values in the bestComb array
        v = np.dot(np.array(comb),choices)
        
        # This is the constraint
        if v > total:
            next
        
        elif v < total:
            
            if v > maxValue:
                maxValue = v
                bestComb = np.array(comb)
                
            elif v == maxValue:
                # tests if current match is better
                if sum(np.array(comb)) < sum(bestComb):
                    bestComb = np.array(comb)
                
                
        else: # v == total
            if maxValue == v: #There is already a match kept
                # it tests if it is a better array
                if sum(np.array(comb)) < sum(bestComb):
                    bestComb = np.array(comb)
            else: # This is the best match 
                maxValue = v
                bestComb = np.array(comb)
            
    return bestComb
            
            
print(find_combination([1,2,2,3], 4))   

print(find_combination([4, 6, 3, 5, 2], 10))  

print(find_combination([1, 3, 4, 2, 5], 16)) 

print(find_combination([4, 10, 3, 5, 8], 1))  
    
        
