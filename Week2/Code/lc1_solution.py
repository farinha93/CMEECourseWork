#!/usr/bin/env python
"""Create lists from bird data"""
__author__ = 'Andre Farinha'
__version__ = '0.0.1'

birds = ( ('Passerculus sandwichensis','Savannah sparrow',18.7),
          ('Delichon urbica','House martin',19),
          ('Junco phaeonotus','Yellow-eyed junco',19.5),
          ('Junco hyemalis','Dark-eyed junco',19.6),
          ('Tachycineata bicolor','Tree swallow',20.2),
         )
#loops

latin_loops = set()
common_loops = set()
mass_loops = set()
for i in range(0, len(birds)):
    latin_loops.add(birds[i][0])
    common_loops.add(birds[i][1])
    mass_loops.add(birds[i][2])
print latin_loops
print common_loops
print mass_loops

#list comprehensions

latin_lc = set([data[0] for data in birds])
common_lc = set([data[1] for data in birds])
mass_lc = set([data[2] for data in birds])

print latin_lc
print common_lc
print mass_lc

#(1) Write three separate list comprehensions that create three different
# lists containing the latin names, common names and mean body masses for
# each species in birds, respectively. 

# (2) Now do the same using conventional loops (you can shoose to do this 
# before 1 !). 

# ANNOTATE WHAT EVERY BLOCK OR, IF NECESSARY, LINE IS DOING! 

# ALSO, PLEASE INCLUDE A DOCSTRING AT THE BEGINNING OF THIS FILE THAT 
# SAYS WHAT THE SCRIPT DOES AND WHO THE AUTHOR IS