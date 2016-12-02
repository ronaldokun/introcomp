#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 17:03:47 2016

@author: ronaldo
"""

import random

def drawBalls(bucket, numDraws):
    
    """
    Receives a list bucket with a number of different balls with the same
    quantity and draws without replacement numDraws times
    
    Returns a list with the balls drawned from the bucket
    
    """
    
    ball = []
    
    copy = list.copy(bucket)
    
    for i in range(numDraws):
        
        try:
            
            
            ball.append(copy.pop(random.randrange(0, len(copy))))
            
        except:
            
            return ValueError("The Bucket is empty!")
    
    return ball
            
def noReplacementSimulation(bucket, numDraws, numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing draws balls out of a bucket containing
    an equal number of different balls.
    Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times the 
    balls of the same color were drawn.
    '''
    
    draw = [] 
    
    success = 0
    
    typesOfBalls = set(bucket)
    
    if numDraws > len(bucket)/len(typesOfBalls):
        
        print("The number of draws is bigger than the number of different \
        balls available")
       
        return None
        
    
        
    for t in range(numTrials):
        
        draw = drawBalls(bucket, numDraws)
        
        ratio = sum(draw)/len(draw)
        
        if ratio in typesOfBalls: # it means the draws are equal
            success += 1
            
    return success/numTrials
    
def bucket(typesOfBalls, lenBucket):
    
    bucket = []
    
    assert lenBucket%len(typesOfBalls) == 0 
        
    
    while len(bucket) < lenBucket:        
        for ball in typesOfBalls:
           bucket.append(ball)
            
    return bucket
    
bucket = bucket([0,1], 8)

print(noReplacementSimulation(bucket, 4, 5000))