#!/usr/bin/env python
"""Create lists from bird data"""
__author__ = 'Andre Farinha'
__version__ = '0.0.1'

rainfall = (('JAN',111.4),
            ('FEB',126.1),
            ('MAR', 49.9),
            ('APR', 95.3),
            ('MAY', 71.8),
            ('JUN', 70.2),
            ('JUL', 97.1),
            ('AUG',140.2),
            ('SEP', 27.0),
            ('OCT', 89.4),
            ('NOV',128.4),
            ('DEC',142.2),
           )

#loops

wet_loop = set()
dry_loop = set()
for i in range(0, len(rainfall)):
    if rainfall[i][1] > 100:
        wet_loop.add(rainfall[i]) #months with more than 100 mm and value
    if rainfall[i][1] < 50:
        dry_loop.add(rainfall[i][0]) #months with less than 50 mm
print wet_loop
print dry_loop

#list comprehensions

wet_lc = set()
dry_lc = set()
wet_lc = set([data[:] for data in rainfall if data[1] > 100])
dry_lc = set([data[0] for data in rainfall if data[1] < 50])

print wet_lc
print dry_lc

# (1) Use a list comprehension to create a list of month,rainfall tuples where
# the amount of rain was greater than 100 mm.
 
# (2) Use a list comprehension to create a list of just month names where the
# amount of rain was less than 50 mm. 

# (3) Now do (1) and (2) using conventional loops (you can choose to do 
# this before 1 and 2 !). 

# ANNOTATE WHAT EVERY BLOCK OR IF NECESSARY, LINE IS DOING! 

# ALSO, PLEASE INCLUDE A DOCSTRING AT THE BEGINNING OF THIS FILE THAT 
# SAYS WHAT THE SCRIPT DOES AND WHO THE AUTHOR IS
