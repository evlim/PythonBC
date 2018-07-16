# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 09:56:06 2016

@author: james.bradley
"""

import re
import time

sent_count = 0
start_time = time.time()
email = open('D:\TeachingMaterials\BusinessAnalytics\Programming\Python\PythonBootCamp\data\hillary-clinton-emails-august-31-release_djvu.txt')
time_list = []

for line in email:
    if re.search('Sent:',line):
        sent_count = sent_count + 1
    time_list = time_list + re.findall('Sent:.*([0-9][0-9]:[0-9][0-9]:[0-9][0-9])',line)
    #print time_list

print time_list
end_time = time.time()
print '\n\nNumber of lines with \'Sent:\': ',sent_count
print 'Number of times: ', len(time_list)
print 'Execution time: ', end_time - start_time