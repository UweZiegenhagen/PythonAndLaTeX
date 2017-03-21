# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 20:34:01 2017

@author: Uwe
"""
def add(a,b):
	return a+b
	
def multiply(a=2,b=3,c=4):
	return a*b*c

print(multiply())
print(multiply(2, 4, 6))
print(multiply(a=5))