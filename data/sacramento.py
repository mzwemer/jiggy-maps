import numpy as np
import pandas as pd
import html5lib 
from unidecode import unidecode
import os 
os.chdir("/Users/Margit/jiggy-maps/data/")

#base tables - upper and lower house
sldu = pd.read_excel('State Legislature Members.xlsx', 'Senators', index_col="District", na_values=['NA'])
sldl = pd.read_excel('State Legislature Members.xlsx', 'Assemblymembers', index_col="District", na_values=['NA'])

bill_name = "AB42"  #no hypen
bill_url = 'http://leginfo.legislature.ca.gov/faces/billVotesClient.xhtml?bill_id=201720180' + bill_name

tables = pd.read_html(bill_url)
table = pd.DataFrame(tables[0])å

#TODO parse out lists in more general way
#for now, assumes most recent vote
i = 0
motion = table.Motion[i]
vote_date = table.Date[i]
location = table.Location[i]
result = table.Result[i]

def extract_votes(j):
    return unidecode(table.Result[i+j]).split(': ')[1].split(', ')

ayes = extract_votes(1)
noes = extract_votes(2)
abstain = extract_votes(3)


def check_vote(name):
    name = unidecode(name)
    if  any(voter in name for voter in ayes) :
        return 'AYE'
    elif any(voter in name for voter in noes):
        return 'NAY'
    elif any(voter in name for voter in abstain):
        return 'ABSTAIN'
    else : return ''


sldl['Vote'] = sldl.Name.apply( lambda name:check_vote(name)) 
sldl.to_csv('votes_' + bill_name + '.csv')

