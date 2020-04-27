#These three days covers some basic handling of data

#pyplot is a collection of functions that plot like one would do in MATLAB
#It will allow us to create figures, plots, and decorate plots
#Let's start with some vary basic visualizations

import matplotlib.pyplot as plt
import numpy as np
#plt.plot([1,2,3,4])
#plt.ylabel("values")
#plt.show()


#Now we can format the style of our plots
#Always an optional third arguement which indicates the color and line type of the plots
#plt.plot([1,2,3,4], [1,4,9,16], "ro")
#plt.show()

#we can also plot with categorical variables
names = ['miela', 'foster']
values = [1,4]
#plt.subplot(131)
#plt.bar(names, values)
#plt.scatter(names, values)
#plt.plot(names, values)

#Now we can also create a function where we plot a function of the data
def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

#just like in R we set the seed, and set the increments!
t1= np.arange(0.0, 5.0, 0.1)
plt.figure()
plt.plot(t1, f(t1), 'bo')
