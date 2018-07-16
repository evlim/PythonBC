# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 09:56:06 2016

@author: james.bradley
"""

import re
import time

start_time = time.time()
email = open('D:/TeachingMaterials/BusinessAnalytics/Programming/Python/BootCamp/2017/PythonBootCamp/data/hillary-clinton-emails-august-31-release_djvu.txt')
email_list = []

for line in email:
    email_list = email_list + re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]',line)

print email_list
end_time = time.time()
print '\n\nExecution time: ', end_time - start_time