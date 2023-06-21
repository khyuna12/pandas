## 2. DataFrame의 기술통계관련 함수
'''
  1. 최대(소)값         ==>  df.max(), df.min()
     누적최대(소)값,     ==>  df.cummax(), df.cummin()
      최대(소)값label   ==>  df.idxmax(), df.idxmin()
  2. (누적)합계         ==>  df.sum(), df.cumsum()
      평균              ==>  df.mean()
      중앙값            ==>  df.median()
      (누적)곱          ==>  df.prod(), df.cumprod()
  3. 사분위             ==>  df.quantile()
     분산               ==>  df.var()
      표준편차           ==>  df.std()
  4. count(갯수)         ==>  df.count()
  5. 통합 통계           ==>  df.describe()

'''

import pandas as pd
import numpy as np

# print(dir(df))
'''
['T', 'abs', 'add', 'add_prefix', 'add_suffix', 'agg', 'aggregate', 'align', 'all', 'any', 'apply', 'applymap', 
'asfreq', 'asof', 'assign', 'astype', 'at', 'at_time', 'attrs', 'axes', 'backfill', 'between_time', 
'bfill', 'bool', 'boxplot', 'clip', 'col1', 'col2', 'col3', 'columns', 'combine', 'combine_first', 
'compare', 'convert_dtypes', 'copy', 'corr', 'corrwith', 'count', 'cov', 'cummax', 'cummin', 'cumprod', 
'cumsum', 'describe', 'diff', 'div', 'divide', 'dot', 'drop', 'drop_duplicates', 'droplevel', 'dropna', 
'dtypes', 'duplicated', 'empty', 'eq', 'equals', 'eval', 'ewm', 'expanding', 'explode', 'ffill', 'fillna', 
'filter', 'first', 'first_valid_index', 'flags', 'floordiv', 'from_dict', 'from_records', 'ge', 'get', 'groupby', 
'gt', 'head', 'hist', 'iat', 'idxmax', 'idxmin', 'iloc', 'index', 'infer_objects', 'info', 'insert', 
'interpolate', 'isetitem', 'isin', 'isna', 'isnull', 'items', 'iterrows', 'itertuples', 'join', 'keys', 
'kurt', 'kurtosis', 'last', 'last_valid_index', 'le', 'loc', 'lt', 'mask', 'max', 'mean', 'median', 'melt', 
'memory_usage', 'merge', 'min', 'mod', 'mode', 'mul', 'multiply', 'ndim', 'ne', 'nlargest', 'notna', 'notnull', 
'nsmallest', 'nunique', 'pad', 'pct_change', 'pipe', 'pivot', 'pivot_table', 'plot', 'pop', 'pow', 'prod', 
'product', 'quantile', 'query', 'radd', 'rank', 'rdiv', 'reindex', 'reindex_like', 'rename', 'rename_axis', 
'reorder_levels', 'replace', 'resample', 'reset_index', 'rfloordiv', 'rmod', 'rmul', 'rolling', 'round', 
'rpow', 'rsub', 'rtruediv', 'sample', 'select_dtypes', 'sem', 'set_axis', 'set_flags', 'set_index', 'shape', 
'shift', 'size', 'skew', 'sort_index', 'sort_values', 'squeeze', 'stack', 'std', 'style', 'sub', 'subtract', 
'sum', 'swapaxes', 'swaplevel', 'tail', 'take', 'to_clipboard', 'to_csv', 'to_dict', 'to_excel', 'to_feather', 
'to_gbq', 'to_hdf', 'to_html', 'to_json', 'to_latex', 'to_markdown', 'to_numpy', 'to_orc', 'to_parquet', 
'to_period', 'to_pickle', 'to_records', 'to_sql', 'to_stata', 'to_string', 'to_timestamp', 'to_xarray', 
'to_xml', 'transform', 'transpose', 'truediv', 'truncate', 'tz_convert', 'tz_localize', 'unstack', 'update', 
'value_counts', 'values', 'var', 'where', 'xs']
'''

df = pd.DataFrame({"col1": [4, 6, 9, 5, 15],
                   "col2": [16, 8, np.nan, 6, 6],
                   "col3": [10, 11, 12, 12, 12]},
                  index=list("ABCDE"))
print(df)
'''
   col1  col2  col3
A     4  16.0    10
B     6   8.0    11
C     9   NaN    12
D     5   6.0    12
E    15   6.0    12
'''

# 1. 행을 축으로 최대/최소값 구하기
x = df.max(axis=0)  # axis=0 위/아래, axis=1 왼/오
x = df.min(axis=0)
print(x)
'''최대
col1     4.0
col2     6.0
col3    10.0
dtype: float64
'''

# 2. 컬럼을 축으로 최대/최소값 구하기
x = df.max(axis=1)
x = df.min(axis=1)
print(x)
'''최대
A    4.0
B    6.0
C    9.0
D    5.0
E    6.0
dtype: float64
'''

# 3. 행을 축으로 누적최대/누적최소값 구하기
x = df.cummax(axis=0)
x = df.cummin(axis=0)
print(x)
'''최대
   col1  col2  col3
A     4  16.0    10
B     6  16.0    11
C     9   NaN    12
D     9  16.0    12
E    15  16.0    12
'''

# 4. 컬럼을 축으로 누적최대/누적최소값 구하기
x = df.cummax(axis=1)
# x = df.cummin(axis=1)
print(x)
'''
   col1  col2  col3
A   4.0  16.0  16.0
B   6.0   8.0  11.0
C   9.0   NaN  12.0
D   5.0   6.0  12.0
E  15.0  15.0  15.0
'''

# 5. 행을 축으로 최대/최소값 라벨(인덱스라벨) 구하기 (컬럼별)
x = df.idxmax(axis=0)
# x = df.idxmin(axis=0)
print(x)
'''
col1    E
col2    A
col3    C
dtype: object
'''

# 6. 컬럼을 축으로 최대/최소값 라벨(컬럼명) 구하기 (행별)
x = df.idxmax(axis=1)
# x = df.idxmin(axis=1)
print(x)
'''
A    col2
B    col3
C    col3
D    col3
E    col1
dtype: object
'''

# 7. 행을 축으로 총합/누적총합 구하기 (컬럼별)
x = df.sum(axis=0)
x = df.cumsum(axis=0)
print(x)
'''
col1    39.0
col2    36.0
col3    57.0
dtype: float64
'''
'''
   col1  col2  col3
A     4  16.0    10
B    10  24.0    21
C    19   NaN    33
D    24  30.0    45
E    39  36.0    57
'''

# 8. 컬럼을 축으로 총합/누적총합 구하기 (행별)
x = df.sum(axis=1)
x = df.cumsum(axis=1)
print(x)
'''
A    30.0
B    25.0
C    21.0
D    23.0
E    33.0
dtype: float64
'''
'''
   col1  col2  col3
A   4.0  20.0  30.0
B   6.0  14.0  25.0
C   9.0   NaN  21.0
D   5.0  11.0  23.0
E  15.0  21.0  33.0
'''

# 9. 행/컬럼을 축으로 평균 구하기
x = df.mean(axis=0)
print(x)
'''
col1     7.8
col2     9.0
col3    11.4
dtype: float64
'''
x = df.mean(axis=1)
print(x)
'''
A    10.000000
B     8.333333
C    10.500000
D     7.666667
E    11.000000
dtype: float64
'''

# 10. 행/컬럼을 축으로 중앙값 구하기
x = df.median(axis=0)
print(x)
'''
col1     6.0
col2     7.0
col3    12.0
dtype: float64
'''
x = df.median(axis=1)
print(x)
'''
A    10.0
B     8.0
C    10.5
D     6.0
E    12.0
dtype: float64
'''

# 11. 행/컬럼을 축으로 곱연산 구하기
x = df.prod(axis=0)
print(x)
'''
col1     16200.0
col2      4608.0
col3    190080.0
dtype: float64
'''
x = df.prod(axis=1)
print(x)
'''
A     640.0
B     528.0
C     108.0
D     360.0
E    1080.0
dtype: float64
'''

# 12. 행/컬럼을 축으로 분산 구하기
x = df.var(axis=0)
x = df.var(axis=1)
print(x)
'''
col1    19.700000
col2    22.666667
col3     0.800000
dtype: float64
A    36.000000
B     6.333333
C     4.500000
D    14.333333
E    21.000000
dtype: float64
'''

# 13. 행/컬럼을 축으로 표준편차 구하기
x = df.std(axis=0)
x = df.std(axis=1)
print(x)
'''
col1    4.438468
col2    4.760952
col3    0.894427
dtype: float64
A    6.000000
B    2.516611
C    2.121320
D    3.785939
E    4.582576
dtype: float64
'''

# 14. 행/컬럼을 축으로 개수 구하기 (null 제외)
x = df.count(axis=0)
x = df.count(axis=1)
print(x)
'''
col1    5
col2    4
col3    5
dtype: int64
A    3
B    3
C    2
D    3
E    3
dtype: int64
'''

# 15. 통합 통계 데이터
print(df.describe())
'''
            col1       col2       col3
count   5.000000   4.000000   5.000000
mean    7.800000   9.000000  11.400000
std     4.438468   4.760952   0.894427
min     4.000000   6.000000  10.000000
25%     5.000000   6.000000  11.000000
50%     6.000000   7.000000  12.000000
75%     9.000000  10.000000  12.000000
max    15.000000  16.000000  12.000000
'''

print(df.info())  # SQL의 desc 테이블명과 비슷
'''
<class 'pandas.core.frame.DataFrame'>
Index: 5 entries, A to E
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   col1    5 non-null      int64  
 1   col2    4 non-null      float64
 2   col3    5 non-null      int64  
dtypes: float64(1), int64(2)
memory usage: 160.0+ bytes
None
'''