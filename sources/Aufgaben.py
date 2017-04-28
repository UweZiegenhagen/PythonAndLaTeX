# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 19:59:15 2017dcxy

@author: ziege
"""
import random
import os
 
min = 1 # number to start with
max = 100 # maximum number
count = 120000 # 12 fit on one page
 
with open('Aufgaben.tex', 'w') as texfile:
	texfile.write("\\documentclass[15pt]{scrartcl}\n")
	texfile.write("\\usepackage[utf8]{inputenc}\n")
	texfile.write("\\usepackage{tgschola,longtable}\n")
	texfile.write("\\usepackage[T1]{fontenc}\n")
	texfile.write("\\setlength{\\parindent}{0pt}\n")
	texfile.write("\\pagestyle{empty}\n")
	texfile.write("\\renewcommand*{\\arraystretch}{1.5}\n")
	texfile.write("\\begin{document}\n")
	texfile.write("\\huge\n")
	texfile.write("\\begin{longtable}{cccp{8cm}r}\n")
 
	for i in range(count):
		a = random.randint(min, max)
		b = random.randint(min, max)
 
		result = a + b;
 
		texfile.write('%s &+& %s &=& %s \\\\ \\hline\n' % (str(a), str(b), str(result)))
 
	texfile.write("\\end{longtable}\n")
	texfile.write("\\end{document}\n")
 
os.system("pdflatex Aufgaben.tex")
os.startfile("Aufgaben.pdf") # Windows-only