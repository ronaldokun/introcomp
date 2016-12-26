#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 15:46:54 2016

@author: ronaldo
"""

import random, pylab
xVals = []
yVals = []
wVals = []
for i in range(1000):
    xVals.append(random.random())
    yVals.append(random.random())
    wVals.append(random.random())
xVals = pylab.array(xVals)
yVals = pylab.array(yVals)
wVals = pylab.array(wVals)
xVals = xVals + xVals
zVals = xVals + yVals
tVals = xVals + yVals + wVals

pylab.hist(xVals)
pylab.figure()
pylab.hist(zVals)
pylab.figure()
pylab.hist(tVals)
pylab.figure()
pylab.plot(xVals,zVals)
pylab.figure()
pylab.plot(xVals,yVals)
