# -*- coding: utf-8 -*-
"""
Created on Sat May 16 00:15:24 2020

@author: AKSHATA
"""


from math import sqrt 
 
def checkPrime(number): 
	if(len(number) == 0): 
		return True
	num = int(number) 
	for i in range(2,int(sqrt(num)) + 1, 1): 
		if ((num % i) == 0): 
			return False
	return True


def splitIntoPrimes(number): 
	numLen = len(number) 


	splitDP = [-1 for i in range(numLen + 1)] 


	for i in range(1, numLen + 1, 1): 

	 
		if (i <= 6 and checkPrime(number[0:i])): 
			splitDP[i] = 1

		if (splitDP[i] != -1): 
			j = 1
			while(j <= 6 and i + j <= numLen): 

			
				if (checkPrime(number[i:i+j])): 

				
					if (splitDP[i + j] == -1): 
						splitDP[i + j] = 1 + splitDP[i] 
					else: 
						splitDP[i + j] = min(splitDP[i + j], 1 + splitDP[i]) 
				j += 1


	return splitDP[numLen] 
 
print(splitIntoPrimes("13499315")) 
print(splitIntoPrimes("43")) 
 
