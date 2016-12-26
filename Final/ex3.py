#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 15:59:19 2016

@author: ronaldo
"""
import random

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    
    # This is a simple way to model the problem   
    bucket = [1,1,1,1,0,0,0,0]
    
    random.shuffle(bucket)
    
    count = 0
        
    for i in range(numTrials):
        
        # It makes a copy so it won't disrupt the original bucket
        copy = bucket.copy()
        draw = []
    
        for j in range(3):        
        
            k = random.choice(range(len(copy)))
            draw.append(copy.pop(k))
        
        # It tests if the draws are equal
        if sum(draw) == 0 or sum(draw) == 3:
            count += 1

    return float(count/numTrials)
    
print(drawing_without_replacement_sim(10000))
