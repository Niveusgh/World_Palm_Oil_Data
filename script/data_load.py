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

plt.figure(figsize = (20, 12))
plt.subplot(231)
plt.barh(QB_df['College'], QB_df['count(Position)'], color='green')
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.title('Most Quarterbacks by College', fontsize=27)

plt.subplot(232)
plt.barh(RB_df['College'], RB_df['count(Position)'], color='orange')
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.title('Most Running Backs by College', fontsize=27)

plt.subplot(233)
plt.barh(T_df['College'], T_df['count(Position)'])
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.title('Most Tackles by College', fontsize=27)

plt.subplot(234)
plt.barh(DE_df['College'], DE_df['count(Position)'], color='Purple')
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.title('Most Defensive Ends by College', fontsize=27)

plt.subplot(235)
plt.barh(CB_df['College'], CB_df['count(Position)'], color='Red')
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.title('Most Cornerbacks by College', fontsize=27)

plt.subplot(236)
plt.barh(LB_df['College'], LB_df['count(Position)'], color='Grey')
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.title('Most Linebackers by College', fontsize=27)


plt.tight_layout()
plt.show()