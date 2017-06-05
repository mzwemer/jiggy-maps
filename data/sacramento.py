import numpy as np
import pandas as pd

import os 
os.chdir("/Users/Margit/jiggy-maps/data/")

#base tables - upper and lower house
sldu = pd.read_excel('State Legislature Members.xlsx', 'Senators', index_col="District", na_values=['NA'])
sldl = pd.read_excel('State Legislature Members.xlsx', 'Assemblymembers', index_col="District", na_values=['NA'])


import scrapy as sp
##Votes found here:
#http://leginfo.legislature.ca.gov/faces/billVotesClient.xhtml?bill_id=201720180AB378

