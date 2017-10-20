#!/usr/bin/env python
"""Create lists from bird data"""
__author__ = 'Andre Farinha'
__version__ = '0.0.1'

taxa = [ ('Myotis lucifugus','Chiroptera'),
         ('Gerbillus henleyi','Rodentia',),
         ('Peromyscus crinitus', 'Rodentia'),
         ('Mus domesticus', 'Rodentia'),
         ('Cleithrionomys rutilus', 'Rodentia'),
         ('Microgale dobsoni', 'Afrosoricida'),
         ('Microgale talazaci', 'Afrosoricida'),
         ('Lyacon pictus', 'Carnivora'),
         ('Arctocephalus gazella', 'Carnivora'),
         ('Canis lupus', 'Carnivora'),
        ]

taxa_dic = {}
for i in range(0, len(taxa)):
    if i == 0:
        taxa_dic[taxa[i][1]] = set()
        taxa_dic[taxa[i][1]].add(taxa[i][0])# = taxa[i][0] # Add first order and species
        
    orders_list = taxa_dic.keys() #uptade order list
    # not in -- operator for if conditions with dictionaries/lists/tuples
    not_new =1;
    for j in range(0, len(orders_list)): #cycle through existing orders
        if (i!= 0) and (taxa[i][1] == orders_list[j]):
            taxa_dic[orders_list[j]].add(taxa[i][0]) #append species to existing order
            not_new = 0
    if (i!= 0) and (not_new == 1):
        taxa_dic[taxa[i][1]] = set()
        taxa_dic[taxa[i][1]].add(taxa[i][0])# = taxa[i][0] #append new oder and species
print taxa_dic
        
    
    
    


# Write a short python script to populate a dictionary called taxa_dic 
# derived from  taxa so that it maps order names to sets of taxa. 
# E.g. 'Chiroptera' : set(['Myotis lucifugus']) etc. 

# ANNOTATE WHAT EVERY BLOCK OR IF NECESSARY, LINE IS DOING! 

# ALSO, PLEASE INCLUDE A DOCSTRING AT THE BEGINNING OF THIS FILE THAT 
# SAYS WHAT THE SCRIPT DOES AND WHO THE AUTHOR IS

# Write your script here: