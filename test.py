import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)
df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(df)


print(np.arange(10,51))
print(np.eye(3))
print(np.random.rand(1))
print(np.random.rand(30))
print(np.arange(10,100,3))
print('************ this will create a series of number from 10 to 100 ************ ')
print(np.arange(10,100))
print('************************************ END ************************************ ')