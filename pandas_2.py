#Now we're going to continue to work with pandas
#This time we will focus on 3D data
#A panel is a 3D containter of data

import pandas as pd
import numpy as np

#Now lets start by creating a random 3D array

three_d = np.random.rand(2,3,4)
panel = pd.Panel(three_d)
print(panel)

#Now we can make two items and put each one in an individual dataframe

data = {'1' : pd.DataFrame(np.random.randn(4,3)), '2': pd.DataFrame(np.random.randn(4,2))}
#Now we want to make our data into a Panel
panel2 =pd.Panel(data)
print panel2['1']
print panel2['2']

#We can also access individual amjor or minor axises
print(panel2.major_xs(1))
