# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 09:56:06 2016

@author: james.bradley
"""

import re
email = open('D:\TeachingMaterials\BusinessAnalytics\Programming\Python\PythonBootCamp\data\hillary-clinton-emails-august-31-release_djvu.txt')
email_list = []
for line in email:
    #print line
    email_list = email_list + re.findall('\S+@\S+',line)
    # email_list.append(re.findall('\S+@\S',line))
    #if len(email_list) > 0:
    #    print email_list
print email_list