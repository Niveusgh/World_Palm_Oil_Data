import pandas as pd
import os
import matplotlib.pyplot as plt


CSV_PATH = os.path.join('..', 'data','palm_oil_production.csv')
print(CSV_PATH)

COLS_TO_USE = ['Entity', 'Code', 
              'Year', 'Tonnes']

df = pd.read_csv(CSV_PATH,
#               index_col='id', 
               usecols=COLS_TO_USE)

df.to_pickle(os.path.join('..', 'data_frame.pickle'))

#print(df)

from os.path import dirname, join
current_dir = dirname(__file__)
file_path = join(current_dir, "./LURES.xlsx")


#with open(file_path, 'r') as f:

#print(os.getcwd())

# graph
#plt.plot([8,6,3,12,7], marker = 'o', 
#        color = 'magenta', linestyle = 'dashed')
#plt.show()

#exercise
#XLSX_PATH = os.path.join('..', 'data',)
#print(XLSX_PATH)
lures = pd.read_excel('LURES.xlsx', sheet_name = 'LURES')
lures

type(lures)

lures.dtypes

QTY = lures['QUANTITY']
SALES = lures['SALES']

type(QTY)

plt.figure(figsize = (12, 6))
plt.scatter(QTY, SALES)
plt.xlabel('Quantity')
plt.ylabel('Sales')
plt.title('Scatterplot of Sales vs. Quantity')
plt.show()

# plt.plot(lures['SALES'])
#plt.show()