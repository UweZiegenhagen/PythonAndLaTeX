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
print(c[1:3]) # 'all'

for i in c:
	print(i)