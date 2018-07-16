# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 09:56:06 2016

@author: james.bradley
"""

import re
import time

start_time = time.time()
email = open('D:/TeachingMaterials/BusinessAnalytics/Programming/Python/BootCamp/2017/PythonBootCamp/data/hillary-clinton-emails-august-31-release_djvu.txt')
email_count = 0
email_list = []

for line in email:
    new_add = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]',line)
    for this_new_add in new_add:
        #this_new_add = this_new_add.lstrip('mailto:')   # or the next line using regualr expressions
        this_new_add = re.sub('^mailto:',"",this_new_add)
        this_new_add = re.sub('>\S*',"",this_new_add)
        #this_new_add.rstrip(re.compile('>\S*'))
        email_list = email_list + [this_new_add]
        email_count += 1

print email_list
print len(email_list)
print 'Email count: ',email_count
end_time = time.time()
print '\n\nExecution time: ', end_time - start_time, ' sec.'