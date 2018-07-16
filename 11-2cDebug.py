# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 09:56:06 2016

@author: james.bradley
"""

import re
import time

start_time = time.time()
email = open('D:\TeachingMaterials\BusinessAnalytics\Programming\Python\PythonBootCamp\data\hillary-clinton-emails-august-31-release_djvu.txt')
time_list = []

for line in email:
    #time_list = time_list + re.findall('Sent:.*([0-9][0-9]:[0-9][0-9]:[0-9][0-9])',line)
    time_list = time_list + re.findall('Sent:',line)
    if re.search('Sent:',line):
        print line
    #print time_list

print time_list
end_time = time.time()
print '\n\nExecution time: ', end_time - start_time