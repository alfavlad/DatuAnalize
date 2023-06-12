import pandas as pd
import os


all_data=pd.read_csv(r"C:\Users\Liene\Desktop\project\project\all_months_sale.csv")

all_data=all_data.dropna(how='all')
all_data=all_data[all_data['Order Date'].str[0:2]!='Or']

all_data['Month'] = all_data['Order Date'].str[0:2]
all_data['Month'] = all_data['Month'].astype('int')

all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered'])
all_data['Price Each'] = pd.to_numeric(all_data['Price Each'])

all_data['Sales'] = all_data['Quantity Ordered']*all_data['Price Each']

all_data = all_data.groupby("Month").sum()

'''import matplotlib.pyplot as plt

months = range(1,13)
results = all_data.groupby('Month').sum()

plt.bar(months, results['Sales'])
plt.xticks(months)
labels, location = plt.yticks()
plt.yticks(labels, (labels/1000000).astype(int))
plt.ylabel('Sales in million USD')
plt.xlabel('Month Number')
plt.show()'''

