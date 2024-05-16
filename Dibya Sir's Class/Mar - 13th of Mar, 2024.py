# How to import a package in python

# "." is membership operator
# "*" kleen star is a 

import pandas as pd
import numpy as np

s1 = pd.Series(np.random.rand(5))
print(s1)
print(s1[2])
print(s1[:3])


import pandas as pd

upa1 = {
        "id" : [1, 2, 3],
        "name" : ['Sagar', 'Upa', 'Tamang'],
        "place" : ['KTM', 'Ghy', 'Tbt'],
        }

df1 = pd.DataFrame(upa1)
print(df1)

df2 = pd.DataFrame {}

