# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 09:15:31 2017

@author: ziege
"""

import jinja2
import os
from jinja2 import Template

jinja_env = jinja2.Environment(
 loader = jinja2.FileSystemLoader(os.path.abspath('.'))
 )

template = jinja_env.get_template('test-min.txt')
print(template.render(variable='Welt'))