#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 18:17:27 2016

@author: ronaldo
"""

import random

def stochasticNumber(start, end):
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    start += 2 if start % 2 == 0 else 1
    
    end += 2 if end % 2 == 0 else 1
    
    return random.randrange(start,end, 2)
    

print(stochasticNumber(9,21))