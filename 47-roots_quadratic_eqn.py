# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 00:37:53 2020

@author: AKSHATA
"""
import math
def find_roots(a,b,c):
    if(a==0):
        return [0]
    d=(b**2)-(4*a*c)
    if(d==0):
        return [1,((-b)/(2*a))]
    elif(d>0):
    
        r1=((-b)+math.sqrt(d))/(2*a)
        
        r2=((-b)-math.sqrt(d))/(2*a)
        return [2,r1,r2]
    else:
        return [3,-b/(2*a),math.sqrt((-1)*d)/(2*a)]
    
print("Enter eqn coffiecients for eqn of the form ax^2+bx+c=0")
a,b,c=map(float,input().split())
r=find_roots(a,b,c)
if(r[0]==0):
    print("Eqn isnt quadratic")
elif(r[0]==2):
    print("roots are real and distinct and they are: ",r[1],r[2])
elif(r[0]==1):
    print("roots are real and same and are: ",r[1],r[1])
else:
    print("roots are imaginary: ",str(r[1])+"+i"+str(r[2]),str(r[1])+"-i"+str(r[2]))
    
    