# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 09:20:09 2017

@author: ziege
"""

import jinja2
import os
from jinja2 import Template
import codecs

latex_jinja_env = jinja2.Environment(
block_start_string = '\BLOCK{',
block_end_string = '}',
variable_start_string = '\VAR{',
variable_end_string = '}',
comment_start_string = '\#{',
comment_end_string = '}',
line_statement_prefix = '%-',
line_comment_prefix = '%#',
trim_blocks = True,
autoescape = False,
loader = jinja2.FileSystemLoader(os.path.abspath('.'))
)

# Laden des Templates aus einer Datei
template = latex_jinja_env.get_template('jinja2-test.tex')
dokument = template.render(hallo='hello', welt='world')

print(dokument)

with codecs.open ('helloworld.tex', 'w', 'utf-8') as file:
    file.write(dokument);
    file.close();
    os.system('pdflatex helloworld.tex')
    os.startfile('helloworld.pdf')