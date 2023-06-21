# 1. DataFrame 생성 방법
'''
   DataFrame 생성 방법

   1. dict 이용
     df = pd.DataFrame(dict)

   2. 중첩 리스트 이용
     df = pd.DataFrame(중첩리스트, index=[], columns=[])

   3. np.Series(리스트) 이용
      - df = pd.DataFrame([series, series,....])

      - (하나의) Series는 DataFrame으로 변경 가능
         df = series.to_frame(이름)

'''
# pip install pandas
import numpy as np
import pandas as pd

print(dir(pd))
'''
['ArrowDtype', 'BooleanDtype', 'Categorical', 'CategoricalDtype', 'CategoricalIndex', 
'DataFrame', 'DateOffset', 'DatetimeIndex', 'DatetimeTZDtype', 'ExcelFile', 'ExcelWriter', 
'Flags', 'Float32Dtype', 'Float64Dtype', 'Grouper', 'HDFStore', 'Index', 'IndexSlice', 
'Int16Dtype', 'Int32Dtype', 'Int64Dtype', 'Int8Dtype', 'Interval', 'IntervalDtype', 'IntervalIndex', 
'MultiIndex', 'NA', 'NaT', 'NamedAgg', 'Period', 'PeriodDtype', 'PeriodIndex', 'RangeIndex', 
'Series', 'SparseDtype', 'StringDtype', 'Timedelta', 'TimedeltaIndex', 'Timestamp', 
'UInt16Dtype', 'UInt32Dtype', 'UInt64Dtype', 'UInt8Dtype', 
'__all__', '__builtins__', '__cached__', '__doc__', '__docformat__', '__file__', '__git_version__', '__loader__', '__name__', 
'__package__', '__path__', '__spec__', '__version__', '_config', '_is_numpy_dev', '_libs', '_testing', '_typing', '_version', 
'annotations', 'api', 'array', 'arrays', 'bdate_range', 'compat', 'concat', 'core', 'crosstab', 'cut', 
'date_range', 'describe_option', 'errors', 'eval', 'factorize', 'from_dummies', 'get_dummies', 'get_option', 
'infer_freq', 'interval_range', 'io', 'isna', 'isnull', 'json_normalize', 'lreshape', 'melt', 'merge', 
'merge_asof', 'merge_ordered', 'notna', 'notnull', 'offsets', 'option_context', 'options', 'pandas', 'period_range', 
'pivot', 'pivot_table', 'plotting', 'qcut', 'read_clipboard', 'read_csv', 'read_excel', 'read_feather', 'read_fwf', 
'read_gbq', 'read_hdf', 'read_html', 'read_json', 'read_orc', 'read_parquet', 'read_pickle', 'read_sas', 'read_spss', 
'read_sql', 'read_sql_query', 'read_sql_table', 'read_stata', 'read_table', 'read_xml', 'reset_option', 
'set_eng_float_format', 'set_option', 'show_versions', 'test', 'testing', 'timedelta_range', 'to_datetime', 
'to_numeric', 'to_pickle', 'to_timedelta', 'tseries', 'unique', 'util', 'value_counts', 'wide_to_long']
'''

# 1. dict 이용
print("1. dict 이용한 DataFrame 생성")
df = pd.DataFrame({"col1" : [4 ,5, 6],
                   "col2" : [7, 8, 9],
                   "col3" : [10, 11, 12]})
print(df, type(df))
'''
   col1  col2  col3
0     4     7    10
1     5     8    11
2     6     9    12 <class 'pandas.core.frame.DataFrame'>
'''

# 2. 중첩 리스트 이용한 DataFrame 생성 => ndarray도 가능
print("2. 중첩 리스트 이용")
df = pd.DataFrame([[4, 7, 10],
                   [5, 8, 11],
                   [6, 9, 12]],
                  index=[1, 2, 3],
                  columns=['col1', 'col2', 'col3'])
print(df)
'''
   col1  col2  col3
1     4     7    10
2     5     8    11
3     6     9    12
'''

# 3.  DataFrame 생성 - Series 사용
print("3. DataFrame 생성")
name =     pd.Series(["유관순","안중근"])
age =      pd.Series([18,31])
birthday = pd.Series(['1920/09/28','1910/03/26'])

hero = pd.DataFrame([name,age,birthday])
hero.columns =["hero1", "hero2"]
hero.index =["이름","나이","생일"]
print(hero)
'''
         hero1       hero2
이름         유관순         안중근
나이          18          31
생일  1920/09/28  1910/03/26
'''
print(hero.T)  # 행열 바꾸기
'''
        이름  나이          생일
hero1  유관순  18  1920/09/28
hero2  안중근  31  1910/03/26
'''

# 4. 외부 파일에서 읽기 read_csv, read_table, ...