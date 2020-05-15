# -*- coding: utf-8 -*-
"""
Created on Fri May 15 20:31:07 2020

@author: AKSHATA
"""

test_list = [9, 4, 5, 4, 4, 5, 9, 5] 


print ("Original list : " + str(test_list)) 

K = 3
 
res = [] 
for i in test_list: 
	freq = test_list.count(i) 
	if freq == K and i not in res: 
		res.append(i) 
	
 
print ("Elements with count K are : " + str(res)) 
