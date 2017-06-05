import numpy as np
import pandas as pd

import os 
os.chdir("/Users/Margit/jiggy-maps/data/")

#base tables - upper and lower house
sldu = pd.read_excel('State Legislature Members.xlsx', 'Senators', index_col="District", na_values=['NA'])
sldl = pd.read_excel('State Legislature Members.xlsx', 'Assemblymembers', index_col="District", na_values=['NA'])



#TODO hook up scraper

  import html5lib
bill_url = 'http://leginfo.legislature.ca.gov/faces/billVotesClient.xhtml?bill_id=201720180AB378'

tables = pd.read_html(bill_url)

print(tables[0])


#for now
motion = 'AB 378 GARCIA, C. Assembly Third Reading'
vote_date = "06/01/17"
location = 'Assembly Floor'
result = 'FAIL'
ayes = ["Berman", "Bloom", "Bonta", "Burke", "Calderon", "Chau", "Chiu", "Cooley", "Eggman", "Friedman", "Cristina Garcia", "Eduardo Garcia", "Gloria", "Gomez", "Gonzalez Fletcher", "Holden", "Irwin", "Jones-Sawyer", "Kalra", "Levine", "Limón", "Low", "McCarty", "Mullin", "Muratsuchi", "Nazarian", "Quirk", "Reyes", "Santiago", "Mark Stone", "Thurmond", "Ting", "Weber", "Wood", "Rendon"]
noes=  ("Acosta", "Travis Allen", "Arambula", "Baker", "Bigelow", "Bocanegra", "Brough", "Caballero", "Cervantes", "Chávez", "Chen", "Cooper", "Cunningham", "Dahle", "Daly", "Flora", "Fong", "Frazier", "Gallagher", "Gray", "Grayson", "Harper", "Kiley", "Lackey", "Maienschein", "Mathis", "Mayes", "Medina", "Melendez", "Obernolte", "Patterson", "Quirk-Silva", "Ridley-Thomas", "Rodriguez", "Rubio", "Salas", "Steinorth", "Voepel", "Waldron")
abstain = ("Aguiar-Curry", "Choi", "Chu", "Dababneh", "Gipson", "O'Donnell")

#join ayes/noes/abstains
#match rep names

test_name = ayes[0]
#find from by Aye vote
sldl[sldl['Name'].str.contains(test_name)].Name
#could just loop this

def check_vote(name):
    if  any(voter in name for voter in ayes) :
        return 'AYE'
    elif any(voter in name for voter in noes):
        return 'NAY'
    elif any(voter in name for voter in abstain):
        return 'ABSTAIN'
    else : return NA


for name in sldl.Name :
    sldl.Vote[ sldl.Name == name] = check_vote(name)
    #ugly, but works

sldl.Vote = sldl.Name.apply(check_vote)

sldl.to_csv('votes_climate.csv')




#join to table
#export to csv
