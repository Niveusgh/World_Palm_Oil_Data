import pandas as pd
import os

CSV_PATH = os.path.join('..', 'data','palm_oil_production.csv')
print(CSV_PATH)

COLS_TO_USE = ['Entity', 'Code', 
              'Year', 'Tonnes']

df = pd.read_csv(CSV_PATH,
#               index_col='id', 
               usecols=COLS_TO_USE)

df.to_pickle(os.path.join('..', 'data_frame.pickle'))

print(df)

