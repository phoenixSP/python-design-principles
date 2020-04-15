# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 14:58:54 2020

@author: shrey
"""

class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        
        if not set(B).issubset(A):
            return -1
        
        i = ceil(len(B)/len(A))
          
        if (A*i).find(B) != -1:
            return i
        elif (A*(i+1)).find(B) != -1:
            return i+1
        else:
            return -1
        
sol = Solution()
x = sol.repeatedStringMatch('abcd', 'cdabcdab')