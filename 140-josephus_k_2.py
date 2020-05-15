# -*- coding: utf-8 -*-
"""
Created on Fri May 15 20:40:58 2020

@author: AKSHATA
"""


def josephus(n): 
	
	
	p = 1
	while p <= n: 
		p *= 2

	return (2 * n) - p + 1

 
n = int(input())
print ("The chosen place is", josephus(n)) 


