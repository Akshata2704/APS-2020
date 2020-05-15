# -*- coding: utf-8 -*-
"""
Created on Fri May 15 20:46:09 2020

@author: AKSHATA
"""



import math 


def queryResults(arr,Q): 
	

	Q.sort(key=lambda x: x[1]) 
	
 
	currL,currR,currSum = 0,0,0
	
	 
	for i in range(len(Q)): 
		L,R = Q[i]
		
 
		while currL<L: 
			currSum-=arr[currL] 
			currL+=1

		while currL>L: 
			currSum+=arr[currL-1] 
			currL-=1
		while currR<=R: 
			currSum+=arr[currR] 
			currR+=1
			
		
		while currR>R+1: 
			currSum-=arr[currR-1] 
			currR-=1
		
		 
		print("Sum of",Q[i],"is",currSum) 

arr = [1, 1, 2, 1, 3, 4, 5, 2, 8] 
Q = [[0, 4], [1, 3], [2, 4]] 
queryResults(arr,Q) 

