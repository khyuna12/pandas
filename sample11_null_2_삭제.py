## 2. 널(null) 값 삭제 및 변경
'''
     null 값 삭제 및 변경

     1. 행 삭제
        new_df = df.dropna(axis=0|'index', inplace=False)
        new_df = df.dropna(axis=0|'index', how="any|all" , inplace=False))


     2. 열 삭제
        new_df = df.dropna(axis=1|'column', inplace=False)
        new_df = df.dropna(axis=1|'column', how="any|all" , inplace=False))
'''

import pandas as pd
import numpy as np

df = pd.DataFrame({ "col1" : [1 ,1, 1, 1, 1],
                    "col2" : [2, 2, 2, 2, np.nan],
                    "col3" : [3, np.nan, np.nan, np.nan, np.nan],
                    "col4" : [ 2, np.nan, np.nan, np.nan, np.nan]},
                    index = [1, 2, 3, 4, 5])
print(df)
'''
   col1  col2  col3  col4
1     1   2.0   3.0   2.0
2     1   2.0   NaN   NaN
3     1   2.0   NaN   NaN
4     1   2.0   NaN   NaN
5     1   NaN   NaN   NaN

'''

# 1. 행삭제
new_df = df.dropna(axis=0)
print(new_df)
'''
   col1  col2  col3  col4
1     1   2.0   3.0   2.0
'''

new_df = df.dropna(axis=0, how="all")  # 전체가 NaN인 행만 삭제됨
print(new_df)
'''
   col1  col2  col3  col4
1     1   2.0   3.0   2.0
2     1   2.0   NaN   NaN
3     1   2.0   NaN   NaN
4     1   2.0   NaN   NaN
5     1   NaN   NaN   NaN
'''

# 2. 열삭제
new_df = df.dropna(axis=1)
print(new_df)
'''
   col1
1     1
2     1
3     1
4     1
5     1
'''

new_df = df.dropna(axis=1, how="all")  # 전체가 NaN인 행만 삭제됨
print(new_df)