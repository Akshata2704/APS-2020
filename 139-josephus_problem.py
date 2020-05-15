# -*- coding: utf-8 -*-
"""
Created on Fri May 15 20:38:39 2020

@author: AKSHATA
"""


def josephus(n, k): 

	if (n == 1): 
		return 1
	else: 
		return (josephus(n - 1, k) + k-1) % n + 1

 

n = int(input())
k = int(input())

print("The chosen place is ", josephus(n, k)) 


