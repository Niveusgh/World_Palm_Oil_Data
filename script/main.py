from tkinter import Toplevel
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from IPython.display import Image

# read files from data folder 
CSV_PATH_PALM = os.path.join('..', 'data','palm_oil_production.csv')
CSV_PATH_FOREST = os.path.join('..', 'data','change_forest.csv')
CSV_PATH_LAND = os.path.join('..', 'data','land_use_palm.csv')


COLS_TO_USE = ['Entity', 'Code', 
              'Year', 'Tonnes']

df_palm = pd.read_csv(CSV_PATH_PALM, usecols=COLS_TO_USE)
df_forest = pd.read_csv(CSV_PATH_FOREST)
df_land = pd.read_csv(CSV_PATH_LAND)

#Intro image
print("Palm Crop")
Image(url= "img/intro.jpg", width=500, height=400)

# simplify column names of dataframe 
df_forest.rename(columns={"Annual net change in forest area": 
                        "Forest_Change"}, inplace=True)

df_land.rename(columns={"Crops - Oil palm fruit - 254 - Area harvested - 5312 - ha": 
                                "Palm_Land_Use"}, inplace=True)

# data cleaning
# check for null values
df_palm.isnull().sum()
df_forest.isnull().sum()
df_land.isnull().sum()

# fill out null values
df1 = df_palm.fillna(value = 'NOT COUNTRY')
df2 = df_forest.fillna(value = 'NOT COUNTRY')
df3 = df_land.fillna(value = 'NOT COUNTRY')

# Build new dataframes that contain only countries
Code = ['NOT COUNTRY', 'OWID_WRL']

indexNames1 = df1[df1['Code'].isin(Code)].index
df_palm_country = df1.drop(indexNames1)

indexNames2 = df2[df2['Code'].isin(Code)].index
df_forest_country = df2.drop(indexNames2)

indexNames3 = df3[df3['Code'].isin(Code)].index
df_land_country = df3.drop(indexNames3)


# Find the countries produce the most palm oil
df_palm_country_top = df_palm_country[df_palm_country['Tonnes'] 
                                        > df_palm_country['Tonnes'].mean()]
Top_Production_Country = df_palm_country_top.Entity.unique()


entity_counts = df_palm['Entity'].value_counts()

# check entities with large data records
s = entity_counts[entity_counts > entity_counts.mean()]



# List of the contenint 
# CONTENINT = ['']

# split into smaller data
plt.figure(figsize = (12, 6))
plt.scatter(QTY, SALES)
plt.xlabel('Quantity')
plt.ylabel('Sales')
plt.title('Scatterplot of Sales vs. Quantity')
plt.show()

# plt.plot(lures['SALES'])
#plt.show()


# df.to_pickle(os.path.join('..', 'data_frame.pickle'))

#print(df)

# from os.path import dirname, join
# current_dir = dirname(__file__)
# file_path = join(current_dir, "./LURES.xlsx")


#with open(file_path, 'r') as f:

#print(os.getcwd())

# graph
#plt.plot([8,6,3,12,7], marker = 'o', 
#        color = 'magenta', linestyle = 'dashed')
#plt.show()

# Aggregate data by continent
#grouped_continent = df_palm.groupby('Entity')['']
