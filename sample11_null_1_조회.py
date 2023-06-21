## 1. 널(null) 값 조회
'''
     널(null) 값 조회 : None, NaN or NA as null

    1.  Pandas 함수 이용
     1)  bool = pd.isna(스칼라|Series|df)
     2)  bool = pd.isnull(스칼라|Series|df)
     3)  bool = pd.notnull(스칼라|Series|df)

    2.  DataFrame 함수 이용
     1)  bool = df.isnull()
         bool = df[컬럼명].isnull()
         bool = df[[컬럼,컬럼2]].isnull()

'''

import pandas as pd
import numpy as np

df = pd.DataFrame({ "col1" : [1 ,1, 1, np.nan, 1],
                    "col2" : [2, 2, 2, 2, np.nan],
                    "col3" : [ np.nan, 3, 3, 3, 3],
                    "col4" : [ np.nan, np.nan, np.nan, np.nan, np.nan]},
                    index = [1, 2, 3, 4, 5])
print(df)
'''
   col1  col2  col3  col4
1   1.0   2.0   NaN   NaN
2   1.0   2.0   3.0   NaN
3   1.0   2.0   3.0   NaN
4   NaN   2.0   3.0   NaN
5   1.0   NaN   3.0   NaN
'''

# pandas의 함수
# 1. df 대상
print(pd.isna(df))  # null인 값 True
print(pd.isnull(df))
'''
    col1   col2   col3  col4
1  False  False   True  True
2  False  False  False  True
3  False  False  False  True
4   True  False  False  True
5  False   True  False  True
'''

print(pd.notnull(df))  # null 아닌 값이 True
print(~pd.isnull(df))
'''
    col1   col2   col3   col4
1   True   True  False  False
2   True   True   True  False
3   True   True   True  False
4  False   True   True  False
5   True  False   True  False
'''

# 2. 특정 컬럼(Series) 대상
print(pd.isna(df['col1']))
print(pd.isnull(df['col1']))
'''
1    False
2    False
3    False
4     True
5    False
Name: col1, dtype: bool
'''

print(pd.notnull(df['col1']))  # null 아닌 값이 True
print(~pd.isnull(df['col1']))
'''
1     True
2     True
3     True
4    False
5     True
Name: col1, dtype: bool
'''

# 2. 특정 컬럼들(DataFrame) 대상
print(pd.isna(df[['col1','col2']]))
print(pd.isnull(df[['col1','col2']]))
'''
    col1   col2
1  False  False
2  False  False
3  False  False
4   True  False
5  False   True
'''

print(pd.notnull(df[['col1','col2']])) # null 아닌 값이 True
print(~pd.isnull(df[['col1','col2']]))
'''
    col1   col2
1   True   True
2   True   True
3   True   True
4  False   True
5   True  False
'''

print("-"*100)

# DataFrame의 함수
# 1. df 대상
print(df.isnull())  # null인 값 True
print(df.isna())
'''
    col1   col2   col3  col4
1  False  False   True  True
2  False  False  False  True
3  False  False  False  True
4   True  False  False  True
5  False   True  False  True
'''

# 2. 특정 컬럼(Series) 대상
print(df['col1'].isnull())
'''
1    False
2    False
3    False
4     True
5    False
Name: col1, dtype: bool
'''

# 2. 특정 컬럼들(DataFrame) 대상
print(df[['col1','col2']].isnull())
'''
    col1   col2
1  False  False
2  False  False
3  False  False
4   True  False
5  False   True
'''

print(pd.notnull(df[['col1','col2']])) # null 아닌 값이 True
print(~pd.isnull(df[['col1','col2']]))
'''
    col1   col2
1   True   True
2   True   True
3   True   True
4  False   True
5   True  False
'''