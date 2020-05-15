# -*- coding: utf-8 -*-
"""
Created on Fri May 15 20:22:47 2020

@author: AKSHATA
"""



from collections import Counter 

ini_list = [1, 2, 3, 4, 4, 5, 5, 5, 5, 7, 
			1, 1, 2, 4, 7, 8, 9, 6, 6, 6]  
print ("initial list", (ini_list)) 
result = [item for items, c in Counter(ini_list).most_common() 
									for item in [items] ] 

print("final list", (result)) 
