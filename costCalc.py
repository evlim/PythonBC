# -*- coding: utf-8 -*-
"""
Created on Fri Jul 01 19:02:36 2016

@author: james.bradley
"""

costVar = raw_input('Enter variable cost: ')
costFixed = raw_input('Enter fixed cost: ')
hoursLabor = raw_input('Enter labor hours: ')
costTotal = costFixed + hoursLabor * costVar
print costTotal