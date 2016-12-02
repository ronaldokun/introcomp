#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 12:48:38 2016

@author: ronaldo
"""

def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """
    
    m = 0
    
    
    for number in L:
        
        i = 1
        
        if s == 0:
            break
        
        while i * number <= s:
            
            i += 1
            
        m += i - 1
        
        s -= (i - 1) * number

    else:
        if s!= 0:
            return "no solution"
        else:
            return m
    return m

soma = 101

lista = sorted([3,4,5,6,7,8,9,10,11], reverse=True)

print(greedySum(lista, soma))