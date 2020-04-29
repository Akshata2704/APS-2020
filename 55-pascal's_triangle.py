# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 23:04:14 2020

@author: AKSHATA
"""

def printPascal(n):  
  
    for line in range(1, n + 1):  
        C = 1; 
        for i in range(1, line + 1):  
              
         
            print(C, end = " ");  
            C = int(C * (line - i) / i);  
        print("");  
  

n = 15;  
printPascal(n);