# -*- coding: utf-8 -*-
"""
Created on Sat May 16 00:11:56 2020

@author: AKSHATA
"""

import bisect 

def findSubset(arr, n, k): 
	vect1, vect2, subset1, subset2 = [], [], [], [] 


	for i in range(0, n): 

		if arr[i] > k: 
			continue
		if i <= n // 2: 
			vect1.append(arr[i]) 
		else: 
			vect2.append(arr[i]) 

 
	for i in range(0, (1 << len(vect1))): 
		value = 1
		for j in range(0, len(vect1)): 
			if i & (1 << j): 
				value *= vect1[j] 

	 
		if value <= k: 
			subset1.append(value) 

	for i in range(0, (1 << len(vect2))): 
		value = 1
		for j in range(0, len(vect2)): 
			if i & (1 << j): 
				value *= vect2[j] 

		if value <= k: 
			subset2.append(value) 
 
	subset2.sort() 

	count = 0
	for i in range(0, len(subset1)): 
		count += bisect.bisect(subset2, (k // subset1[i])) 
 
	count -= 1

	 
	return count 


arr = [4, 2, 3, 6, 5] 
n = len(arr) 
k = 25
print(findSubset(arr, n, k)) 

 
