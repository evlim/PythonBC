# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 09:56:06 2016

@author: james.bradley
"""

import re
#email = open('D:/TeachingMaterials/BusinessAnalytics/Programming/Python/BootCamp/2017/PythonBootCamp/data/hillary-clinton-emails-august-31-release_djvu.txt')
email = open('C:/Users/jrbrad/Desktop/PythonBootCamp/data/hillary-clinton-emails-august-31-release_djvu.txt')
email_list = []
for line in email:
    email_list = email_list + re.findall('@',line)
print email_list
print len(email_list)