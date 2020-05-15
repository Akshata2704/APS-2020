# -*- coding: utf-8 -*-
"""
Created on Sat May 16 00:18:06 2020

@author: AKSHATA
"""

 
def product_subarrays(arr, n): 

	product = 1; 

 
	for i in range(n): 
		for j in range(i, n): 
			product *= arr[j]; 


	print(product); 

 
arr = [ 10, 3, 7 ]; 
n = len(arr); 
product_subarrays(arr, n); 


