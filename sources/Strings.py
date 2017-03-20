# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 20:25:27 2017

@author: Uwe
"""
a = 'Hallo'
b = 'Welt'

c = a + ' ' + b
'W' in c # True
print(c[0]) # 'H'
print(c[-1]) # 't'
print(c[1:3]) # 'al'
print(c[1:4]) # 'all'
print(c[1:-1]) # 'allo Wel'
print(c[1:])   # 'allo Welt'
     
for i in c:
	print(i)