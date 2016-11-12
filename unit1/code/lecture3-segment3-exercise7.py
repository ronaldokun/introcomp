#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 17:55:08 2016

@author: ronaldo
"""

from lecture3Segment2 import Edge

"""
    Consider once again our permutations of students in a line. 
    Recall the nodes in the graph represent permutations, and that 
    the edges represent swaps of adjacent students. We want to design 
    a weighted graph, weighting edges higher for moves that are harder 
    to make.
"""

class WeightedEdge(Edge):
    
    def __init__(self, src, dest, weight):
        Edge.__init__(self, src, dest) #Init from Edge
        self.weight = weight
    def getWeight(self):
        return self.weight
    def __str__(self):
        return Edge.__str__(self) + "(" + str(self.weight) + ")"
