## 4. Series 및 DataFrame 의 기술통계관련 함수

import numpy as np
import pandas as pd

'''

  1. 최대(소)값         ==>  df[[컬럼,컬럼2]].max(), df[[컬럼,컬럼2]].min()
     누적최대(소)값,     ==>  df[[컬럼,컬럼2]].cummax(), df[[컬럼,컬럼2]].cummin()
      최대(소)값label  ==>  df[[컬럼,컬럼2]].idxmax(), df[[컬럼,컬럼2]].idxmin()
  2. (누적)합계         ==>  df[[컬럼,컬럼2]].sum(), df[[컬럼,컬럼2]].cumsum()
      평균             ==>  df[[컬럼,컬럼2]].mean()
      중앙값            ==>  df[[컬럼,컬럼2]].median()
      (누적)곱          ==>  df[[컬럼,컬럼2]].prod(), df[[컬럼,컬럼2]].cumprod()
  3. 사분위             ==>  df[[컬럼,컬럼2]].quantile()
     분산               ==>  df[[컬럼,컬럼2]].var()
      표준편차           ==>  df[[컬럼,컬럼2]].std()
  4. count(갯수)         ==>  df[[컬럼,컬럼2]].count()
  5. 통합 통계           ==>  df[[컬럼,컬럼2]].describe()

'''
df = pd.DataFrame({"col1" : [4 ,6, 9, 5, 15],
                   "col2" : [16, 8, np.nan, 6, 6],
                   "col3" : [10, 11, 12, 12, 12]},
                    index = list("ABCDE"))
print(df)
'''
   col1  col2  col3
A     4  16.0    10
B     6   8.0    11
C     9   NaN    12
D     5   6.0    12
E    15   6.0    12
'''

# 1. 행을 축으로 최대/최소값 구하기 (컬럼별)
x = df['col1'].max(axis=0)  # axis=0 위/아래, axis=1 왼/오
# x = df['col1'].min(axis=0)
print(x)  # 15

# 2. 행을 축으로 누적최대/누적최소값 구하기
x = df['col2'].cummax(axis=0)
# x = df['col2'].cummin(axis=0)
print(x)
'''
A    16.0
B    16.0
C     NaN
D    16.0
E    16.0
'''

# 3. 행을 축으로 최대/최소값 라벨(인덱스라벨) 구하기 (컬럼별)
x = df['col1'].idxmax(axis=0)
# x = df['col1'].idxmin(axis=0)
print(x)  # E

# 4. 행을 축으로 총합/누적총합 구하기 (컬럼별)
x = df['col1'].sum(axis=0)
x = df['col1'].cumsum(axis=0)
print(x)  # 39
'''
A     4
B    10
C    19
D    24
E    39
Name: col1, dtype: int64
'''

# 5. 행/컬럼을 축으로 평균 구하기
x = df['col1'].mean(axis=0)
print(x)  # 7.8

# 6. 행/컬럼을 축으로 중앙값 구하기
x = df['col1'].median(axis=0)
print(x)  # 6

# 7. 행/컬럼을 축으로 곱연산 구하기
x = df['col1'].prod(axis=0)
print(x)  # 16200

# 8. 행/컬럼을 축으로 분산 구하기
x = df['col1'].var(axis=0)
print(x)  # 19.700000000000003

# 9. 행/컬럼을 축으로 표준편차 구하기
x = df['col1'].std(axis=0)
print(x)  # 4.43846820423443

# 10. 행/컬럼을 축으로 개수 구하기 (null 제외)
x = df['col1'].count()
print(x)  # 5
