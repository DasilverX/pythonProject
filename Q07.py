import pandas as pd
from pandas import Series, DataFrame

d = {'col1':[1,2], 'col2':[3,4], 'col3':[5,6], 'col4':[7,8]}

df = pd.DataFrame(d)
print(df)

# Q07--02

new_df = pd.DataFrame(d['col4'])
print(new_df)

#Q07--03

df.index = Series(['primero','segundo'])
new_df.index = Series(['primero','segundo'])
print(df)
print('-----------------------')
print(new_df)

#Q07--04
print('-------------------')
print(df.notnull())
