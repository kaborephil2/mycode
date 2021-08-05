#!/usr/bin/python3

import pandas as pd

#display all the data in the file
df = pd.read_csv('pokemon_data.csv')
print("****************************************************************************************************************************\n")

#display the first 10 lines of data
print(df.head(10))
print("****************************************************************************************************************************\n")

#display the last 3 line of data
print(df.tail(5))
print("****************************************************************************************************************************\n")

#display each column for name, type 1 and HP
print(df[['Name',  'Type 1',  'HP' ]])
print("****************************************************************************************************************************\n")

#display sorting data/ ascending
print(df.sort_values('Name', ascending=True).head(8))
