import pandas as pd
import psycopg2

#Creates a df the Province column only, deletes duplicates values and reset the indexes from 1 to 7
data = pd.read_csv('Districts_of_Costa_Rica_1.csv')
provincias = pd.DataFrame(data['Province'].copy())
provincias = provincias.drop_duplicates()
provincias = provincias.reset_index(drop=True)
provincias.index = provincias.index + 1
provincias['Index'] = provincias.index


canton = data[['Province','Canton']].copy()
canton = canton.drop_duplicates()
canton = canton.reset_index(drop=True)
canton.index = canton.index + 1
canton['Index'] = canton.index

district = data[['Canton','District']].copy()
district = district.drop_duplicates()
district = district.reset_index(drop=True)
district.index = district.index + 1

print(district)
'''print(provincias)
print(provincias[provincias['Province'] == 'San José'])
#print(type(provincias))



for indx, values in canton.iterrows():
    #print(indx, values)
    #print(indx)
    print(values["Province"],values["Canton"])
    print(provincias[provincias['Province'] == values["Province"]]['Index'])'''
#print(provincias)
for _, values in provincias.iterrows():
    canton.loc[canton['Province'] == values['Province'],'Province'] = values['Index']

print(canton)

for _, values in canton.iterrows():
    district.loc[district['Canton'] == values['Canton'],'Canton'] = values['Index']

print(district)
print("Cantones")
for _, values in canton.iterrows():
    print(values["Canton"], values["Index"])