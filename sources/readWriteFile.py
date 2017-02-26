# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 17:54:46 2017

@author: Uwe
"""
dateiname = 'exampleFile.txt'

filepointer = open(dateiname,'r') 
# 'r' (read) oder 'a' (append)
for zeile in filepointer:
        print(zeile)

filepointer.close()