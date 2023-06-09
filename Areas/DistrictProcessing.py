import pandas as pd
import psycopg2

#Creates a df the Province column only, deletes duplicates values and reset the indexes from 1 to 7
data = pd.read_csv("Districts_of_Costa_Rica_1.csv")
provincias = data["Province"].copy()
provincias = provincias.drop_duplicates()
provincias = provincias.reset_index(drop=True)
provincias.index = provincias.index + 1


canton = data[["Province","Canton"]].copy()
canton = canton.drop_duplicates()
canton = canton.reset_index(drop=True)
canton.index = canton.index + 1
#print(data)
#print(provincias)
#print(type(provincias))

#for indx, values in provincias.items():
#    print('index: ', indx, 'value: ', values)

for indx, values in canton.iterrows():
    #print(indx, values)
    #print(indx)
    print(values["Province"],values["Canton"])