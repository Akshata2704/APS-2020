# -*- coding: utf-8 -*-
"""
Created on Fri May 15 20:21:52 2020

@author: AKSHATA
"""

# Function to Sort even-placed elements 
# in increasing and odd-placed in decreasing 
# order 

def evenOddSort(input): 


	evens = [ input[i] for i in range(0,len(input)) if i%2==0 ] 
	odds = [ input[i] for i in range(0,len(input)) if i%2!=0 ] 

	print (sorted(evens) + sorted(odds,reverse=True)) 

 
input = [0, 1, 2, 3, 4, 5, 6, 7] 
evenOddSort(input) 
