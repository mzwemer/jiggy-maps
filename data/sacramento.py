import numpy as np
import pandas as pd
import html5lib 
import unicodedata    
import os 
os.chdir("/Users/Margit/jiggy-maps/data/")

#base tables - upper and lower house
sldu = pd.read_excel('State Legislature Members.xlsx', 'Senators', index_col="District", na_values=['NA'])
sldl = pd.read_excel('State Legislature Members.xlsx', 'Assemblymembers', index_col="District", na_values=['NA'])


bill_name = "AB42"  #no hypen
bill_url = 'http://leginfo.legislature.ca.gov/faces/billVotesClient.xhtml?bill_id=201720180' + bill_name

tables = pd.read_html(bill_url)

print(tables[0])
#TODO parse out lists

#for now
motion = 'AB 42 BONTA Assembly Third Reading'
vote_date = "06/01/17"
location = 'Assembly Floor'
result = 'FAIL'
ayes = ["Aguiar-Curry", "Berman", "Bloom", "Bonta", "Burke", "Caballero", "Chau", "Chiu", "Chu", "Dababneh", "Eggman", "Friedman", "Cristina Garcia", "Eduardo Garcia", "Gloria", "Gomez", "Gonzalez Fletcher", "Holden", "Jones-Sawyer", "Kalra", "Levine", "Limón", "Low", "McCarty", "Mullin", "Nazarian", "Quirk", "Ridley-Thomas", "Santiago", "Mark Stone", "Thurmond", "Ting", "Weber", "Wood", "Rendon"]
noes = ["Acosta", "Travis Allen", "Arambula", "Baker", "Bigelow", "Brough", "Cervantes", "Chávez", "Chen", "Cooley", "Cooper", "Cunningham", "Dahle", "Daly", "Flora", "Fong", "Frazier", "Gallagher", "Gray", "Grayson", "Harper", "Irwin", "Kiley", "Lackey", "Mathis", "Mayes", "Medina", "Melendez", "Obernolte", "Patterson", "Quirk-Silva", "Rodriguez", "Rubio", "Salas", "Steinorth", "Voepel", "Waldron"]
abstain = ("Bocanegra", "Calderon", "Choi", "Gipson", "Maienschein", "Muratsuchi", "O'Donnell", "Reyes")


test_name = ayes[0]
#find from by Aye vote
sldl[sldl['Name'].str.contains(test_name)].Name
#could just loop this

#Chavez accent bug
def check_vote(name):
  #  name = unicodedata.normalize('NFKD', uname).encode('ascii','ignore')
    if  any(voter in name for voter in ayes) :
        return 'AYE'
    elif any(voter in name for voter in noes):
        return 'NAY'
    elif any(voter in name for voter in abstain):
        return 'ABSTAIN'
    else : return ''


sldl.Name = str(sldl.Name)
temp = sldl.Name.apply( lambda name:check_vote(name) , axis=1)

#TODO fix unicode bug
#sldl.Vote = [check_vote(name) for name in sldl.Name]
sldl.to_csv('votes_' + bill_name + '.csv')




#join to table
#export to csv
