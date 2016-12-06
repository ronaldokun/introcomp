# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def max_contig_sum(L):
    """
    L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L
    """
    
    maxSum = L[0]

    for i in range(len(L)):
        for j in range(i,len(L)):
            
            s = sum(L[i:j+1])
            
            if s > maxSum:
                maxSum = s
                
    return maxSum
    

print(max_contig_sum([3,4,-1,5,-4]))

print(max_contig_sum([3,4,-8,15,-1,2]))


            
    
