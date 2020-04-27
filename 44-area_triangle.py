# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 00:32:49 2020

@author: AKSHATA
"""

def area_triangle(l,b):
    return (l*b*0.5)
l,b=map(int,input().split())
print(area_triangle(l,b))