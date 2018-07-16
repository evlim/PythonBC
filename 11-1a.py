# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 09:56:06 2016

@author: james.bradley
"""

import re

email = open('D:\TeachingMaterials\BusinessAnalytics\Programming\Python\PythonBootCamp\data\MSBAEmailMessage_WS.txt')
for line in email:
    if re.search('^From', line):
        print line