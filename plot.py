import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import pylab

#test = np.random.normal(160,15, 1200)
#print(test)
test = np.random.uniform(0,1,1000)

#plt.hist(test)
#plt.show()
sm.qqplot(test, line='s')
plt.show()
#pylab.show()
#foo = [ 1, 3, 4, 8, 10, 13, 14, 25, 35 ]
#foo = np.array(foo)
#plt.boxplot(foo)
#sm.qqplot(foo,line='q')
#plt.show()
