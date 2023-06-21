## 1. 정렬
'''
   DataFrame 정렬

   1. 정렬
      df.sort_values(by=컬럼명, ascending=True, inplace=False, ignore_index=False, kind="quicksort", na_position="last")
      df.sort_values(by=[컬럼명,컬럼명2], ascending=True, inplace=False, ignore_index=False, kind="quicksort", na_position="last")

   2. 행 라벨 및 컬럼 라벨 정렬
      new_df = df.sort_index(axis=0|1)

'''

import pandas as pd
import numpy as np
import seaborn as sns

df = sns.load_dataset("mpg")

print("1. DataFrame")
df = df.head(10)  # df.tail()은 뒤에 거
df.index = list('HDAFCBEGIJ')  # index 랜덤하게 한 후 정렬하기
# null 변경
df[df['name']=='ford torino'] = np.nan
print(df, df.shape)
'''
    mpg  cylinders  displacement  ...  model_year  origin                       name
H  18.0        8.0         307.0  ...        70.0     usa  chevrolet chevelle malibu
D  15.0        8.0         350.0  ...        70.0     usa          buick skylark 320
A  18.0        8.0         318.0  ...        70.0     usa         plymouth satellite
F  16.0        8.0         304.0  ...        70.0     usa              amc rebel sst
C   NaN        NaN           NaN  ...         NaN     NaN                        NaN
B  15.0        8.0         429.0  ...        70.0     usa           ford galaxie 500
E  14.0        8.0         454.0  ...        70.0     usa           chevrolet impala
G  14.0        8.0         440.0  ...        70.0     usa          plymouth fury iii
I  14.0        8.0         455.0  ...        70.0     usa           pontiac catalina
J  15.0        8.0         390.0  ...        70.0     usa         amc ambassador dpl

[10 rows x 9 columns] (10, 9)
'''

# 1. mpg 컬럼 기준 오름차순 정렬
new_df = df.sort_values(by='mpg', ascending=True, inplace=False, na_position="last")
print(new_df)
'''
    mpg  cylinders  displacement  ...  model_year  origin                       name
E  14.0        8.0         454.0  ...        70.0     usa           chevrolet impala
G  14.0        8.0         440.0  ...        70.0     usa          plymouth fury iii
I  14.0        8.0         455.0  ...        70.0     usa           pontiac catalina
D  15.0        8.0         350.0  ...        70.0     usa          buick skylark 320
B  15.0        8.0         429.0  ...        70.0     usa           ford galaxie 500
J  15.0        8.0         390.0  ...        70.0     usa         amc ambassador dpl
F  16.0        8.0         304.0  ...        70.0     usa              amc rebel sst
H  18.0        8.0         307.0  ...        70.0     usa  chevrolet chevelle malibu
A  18.0        8.0         318.0  ...        70.0     usa         plymouth satellite
C   NaN        NaN           NaN  ...         NaN     NaN                        NaN
'''

# 2. mpg, displacement 컬럼 기준 오름차순 정렬(다중정렬)
new_df = df.sort_values(by=['mpg', 'displacement'], ascending=True, inplace=False, na_position="last")
print(new_df)
'''
    mpg  cylinders  displacement  ...  model_year  origin                       name
G  14.0        8.0         440.0  ...        70.0     usa          plymouth fury iii
E  14.0        8.0         454.0  ...        70.0     usa           chevrolet impala
I  14.0        8.0         455.0  ...        70.0     usa           pontiac catalina
D  15.0        8.0         350.0  ...        70.0     usa          buick skylark 320
J  15.0        8.0         390.0  ...        70.0     usa         amc ambassador dpl
B  15.0        8.0         429.0  ...        70.0     usa           ford galaxie 500
F  16.0        8.0         304.0  ...        70.0     usa              amc rebel sst
H  18.0        8.0         307.0  ...        70.0     usa  chevrolet chevelle malibu
A  18.0        8.0         318.0  ...        70.0     usa         plymouth satellite
C   NaN        NaN           NaN  ...         NaN     NaN                        NaN
'''