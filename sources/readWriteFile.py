# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 17:54:46 2017

@author: Uwe Ziegenhagen
"""
dateiname = 'exampleFile.txt'

filepointerW = open(dateiname,'w') 
# 'r' (read) oder 'a' (append)
for i in 'Hello World':
        filepointerW.write(i + '\n')
filepointerW.close()

filepointerR = open(dateiname,'r') 
# 'r' (read) oder 'a' (append)
for zeile in filepointerR:
        print(zeile)

filepointerR.close()