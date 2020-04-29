# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 00:46:08 2020

@author: AKSHATA
"""

import math as mt 
  
# Prints k factors of n if n can be written 
# as multiple of k numbers. Else prints -1 
def kFactors(n, k): 
      
    # list to store all prime factors of n 
    a = list() 
      
    #insert all 2's in list 
    while n % 2 == 0: 
        a.append(2) 
        n = n // 2
          
    # n must be odd at this point 
    # so we skip one element(i=i+2) 
    for i in range(3, mt.ceil(mt.sqrt(n)), 2): 
        while n % i == 0: 
            n = n / i; 
            a.append(i) 
              
    # This is to handle when n>2 and 
    # n is prime 
    if n > 2: 
        a.append(n) 
          
    # if size(a)<k,k factors are not possible 
    if len(a) < k: 
        return 0
    return 1
          
   
  
# Driver code 
for _ in range(int(input())):
    n,k=input().split()
    n=int(n)
    k=int(k)
    print(kFactors(n, k))