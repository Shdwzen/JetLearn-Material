import pandas as pd
import random as rand
import numpy as np
import scipy as sci

vals = [12,4,2334,23231,3,123,2323,23]
valseries = pd.Series(vals)
val2 = [0.7,2.5,2.5,0.7,0.2]
newval = np.array(val2)
scimode = sci.stats.mode(newval)
for i in range(7):
    val2.append(rand.uniform(10,100))
val2series = pd.Series(val2)
print(valseries)
print("This is the mode %s"/val2series.mode())
print(valseries+val2series)

print(valseries.median())
print(val2series.value_counts())

print(scimode)