
# 4.  index 과 index 이용한 병합
'''
 index 이용한 병합

     pd.merge(df, df2,  left_on=“인덱스”, right_on=“인덱스” )

      pd.merge(df, df2,  left_on=“인덱스”, right_index=True )

      pd.merge(df, df2,  right_on=“인덱스”, left_index=True )

      pd.merge(df, df2,  left_index=True, right_index=True )
'''

import pandas as pd

df1 = pd.DataFrame({"key": ['a', 'b', 'a', 'a', 'b', 'c'],
                    "value": range(6)},
                   index=list('KBSMVC'))
print(df1)
'''
  key  value
K   a      0
B   b      1
S   a      2
M   a      3
V   b      4
C   c      5
'''

df2 = pd.DataFrame({"g_value": [3.5, 7]},
                   index=['K', 'S'])
print(df2)
'''
   g_value
K      3.5
S      7.0
'''

new_df = pd.merge(df1, df2, how="inner", left_on=df1.index, right_on=df2.index)
new_df = pd.merge(df1, df2, how="inner", left_on=df1.index, right_index=True)

new_df = pd.merge(df1, df2, how="inner", left_index=True, right_on=df2.index)
new_df = pd.merge(df1, df2, how="inner", left_index=True, right_index=True)
print(new_df)
'''
  key_0 key  value  g_value
0     K   a      0      3.5
1     S   a      2      7.0
'''