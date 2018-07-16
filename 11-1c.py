# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 09:56:06 2016

@author: james.bradley
"""

import re

email = open('D:\TeachingMaterials\BusinessAnalytics\Programming\Python\PythonBootCamp\data\MSBAEmailMessage_typo.txt')
for line in email:
    line = line.lstrip()
    if re.search('^F.*m', line):
        print line