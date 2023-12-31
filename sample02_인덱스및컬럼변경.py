
'''
   DataFrame 컬럼과 인덱스 변경

   1. 컬럼명 변경

   df.columns=[값, 값2, ...]

   2. 인덱스(라벨) 변경

        가. pd.DataFrame(..., index=[값, 값2, ...])
        나. df.index=[값, 값2, ...]
'''

import numpy as np
import pandas as pd

df = pd.DataFrame({"col1" : [4 ,5, 6],
                   "col2" : [7, 8, 9],
                   "col3" : [10, 11, 12]})

print(df)
'''
   col1  col2  col3
0     4     7    10
1     5     8    11
2     6     9    12
'''

# 1. 컬럼명 변경
df.columns = ['c1', 'c2', 'c3']
print(df)
'''
   c1  c2  c3
0   4   7  10
1   5   8  11
2   6   9  12
'''

# 2. 인덱스(라벨) 변경
df = pd.DataFrame({"col1" : [4 ,5, 6],
                   "col2" : [7, 8, 9],
                   "col3" : [10, 11, 12]}, index=['A', 'B', 'C'])
print(df)
'''
   col1  col2  col3
A     4     7    10
B     5     8    11
C     6     9    12
'''

df.index=[10,20,30]
print(df)
'''
    col1  col2  col3
10     4     7    10
20     5     8    11
30     6     9    12
'''