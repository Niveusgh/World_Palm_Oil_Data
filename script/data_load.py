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

print(df)

# graph
#plt.plot([8,6,3,12,7], marker = 'o', 
#        color = 'magenta', linestyle = 'dashed')
#plt.show()

#exercise
XLSX_PATH = os.path.join('..', 'data','LURES.xlsx')
print(XLSX_PATH)
lures = pd.read_excel(XLSX_PATH, sheet_name = 'LURES')
lures
