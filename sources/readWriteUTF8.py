# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 17:45:41 2017

@author: Uwe Ziegenhagen
"""
import io
import datetime
 
jetzt = datetime.datetime.now()
dateiname = 'example.txt'

with io.open(dateiname,'w',encoding='utf8') as datei:
    datei.write('äüöß ' + jetzt.isoformat())
    
with io.open(dateiname,'r',encoding='utf8') as datei:
    text = datei.read()
    print(text)