# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 09:15:31 2017

@author: ziege
"""

from jinja2 import Template

itemlist = ['first','second','third']

template = Template(
'''\\begin{itemize}
{% for item in liste %}
 \\item {{item}}
{% endfor %}
\\end{itemize}'''
)

print(template.render(liste=itemlist))