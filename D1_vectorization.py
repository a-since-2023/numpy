# to normalize a data set of 1million feature values with vectorization instead of looping

import numpy as np


#uniform makes sure value is within given range 
data = np.random.uniform(10.0,50.0,size=1_000_000)

print(data)

max = data.max()
min = data.min()

normalize = (data - min)/ (max - min)

print(normalize)