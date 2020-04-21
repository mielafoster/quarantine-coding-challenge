#First we need ot import the panda dataset
import pandas as pd
import numpy as np

#Remember we can create series with any type of dataframe
#Let's make one with a dictionary

data = {'Miela': 7, 'Harvard': 9, 'College': 10}
series2 = pd.Series(data)
print(series2)

#We can also really easily index things
print(series2[0])

#We can also retrieve like the first # of elements index and item
print(series2[:3])

#We denote the last element with a negative sign
print(series2[-2:])

#now that we've done series data ( which is one dimensional) we can move onto 2D dataset
#A data frame is a two dimensional data structure if it has rows and columns
#We can create data frames using pandas
data2 = [1,2,3]
df =pd.DataFrame(data2)
print(df)

#We can also add columns and stuff
df =pd.DataFrame(data2, columns = ['Height'])
print(df)

# We can also add df really easily

df2 = series2 + df
print(df2)

#And we would delete by simply doing the follow
series2.pop('Miela')
#or we could delete
del series2['Miela']
