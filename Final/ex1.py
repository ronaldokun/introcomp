#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 13:57:44 2016

@author: ronaldo
"""

import random, pylab

A = []

B = []

for i in range(1000):
    A.append(random.gauss(1,3))
    B.append(random.gauss(1,5))
    
pylab.hist(A)
pylab.figure()
pylab.hist(B)

