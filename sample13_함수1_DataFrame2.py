## 3. DataFrame의 기본 함수
import numpy as np
import pandas as pd

'''
   1. 값 변경                                  ==>  df.replace()
   2. 컬럼명 및 인덱스명 변경                     ==> df.rename(columns|index)
   3. 모든(특정) 컬럼(행)값의 참/거짓 여부          ==>  df.any() , df.all()
   4. 중복조회 및 제거                           ==>  df.duplicated(),  df.drop_duplicates()

   5. 임의의 함수 적용 ==> df.apply(함수, axis=0|1)
      임의의 함수를 한번에 DataFrame의 행과 열에 적용.

   6. 값이 있으면 True, 아니면 False ==> df.isin(집합형)

    7. unique한 값의 갯수 ==> df.nunique(dropna=True)
                            dropna=False 면 nan 포함해서 갯수 반환
                            
        df.nunique ==> 개수
        series.unique ==> 값
'''

df = pd.DataFrame({"a": [0, 10, 100],
                   "b": [2, 20, 200],
                   "c": [3, 20, 300]},
                  index=list('ABC'))

print("1. DataFrame")
print(df)
'''
     a    b    c
A    0    2    3
B   10   20   20
C  100  200  300
'''

# 1. df.replace(dict, new값) ==> dict에 지정된 값을 new값으로 치환
new_df = df.replace({'a':100, 'b':2, 'c':30}, 999)
print(new_df)
'''
     a    b    c
A    0  999    3
B   10   20  999
C  999  200  300
'''

# 2. df.replace(dict) ==> {old:new, old:new}
new_df = df.replace({20:2000, 3:3000})
print(new_df)
'''
     a     b     c
A    0     2  3000
B   10  2000  2000
C  100   200   300
'''

# 3. 컬럼명 및 인덱스명 변경
new_df = df.rename(columns={'a':'col1', 'b':'col2', 'c':'col3'})
new_df = df.rename(index={'A':'row1', 'B':'row2', 'C':'row3'})
print(new_df)
'''
   col1  col2  col3
A     0     2     3
B    10    20    20
C   100   200   300
        a    b    c
row1    0    2    3
row2   10   20   20
row3  100  200  300
'''

# 4. 모든(특정) 컬럼(행)값의 참/거짓 여부
x = df.all(axis=0)  # 모든 컬럼값이 참인지
print(x)
'''
a    False
b     True
c     True
dtype: bool
'''
x = df.all(axis=1)  # 모든 행값이 참인지
print(x)
'''
A    False
B     True
C     True
dtype: bool
'''
x = df.any(axis=0)
print(x)
'''
a    True
b    True
c    True
dtype: bool
'''
x = df.any(axis=1)
print(x)
'''
A    True
B    True
C    True
dtype: bool
'''


df = pd.DataFrame({"k1":['one']*3 + ['two']*4,
                  "k2":[1,1,2,3,3,4,4] })
print(df)
'''
    k1  k2
0  one   1
1  one   1
2  one   2
3  two   3
4  two   3
5  two   4
6  two   4
'''

# 5. 중복 여부
x = df.duplicated()  # df에 중복된 행인지
print(x)
'''
0    False
1     True
2    False
3    False
4     True
5    False
6     True
dtype: bool
'''

# 6. 중복된 행 제거 후 반환
new_df = df.drop_duplicates()
print(new_df)
'''
    k1  k2
0  one   1
2  one   2
3  two   3
5  two   4
'''
new_df = df.drop_duplicates(ignore_index=True)
print(new_df)
'''
    k1  k2
0  one   1
1  one   2
2  two   3
3  two   4
'''


df = pd.DataFrame({"국어":[50,60,70,80,90],"수학":[100,100,100,100,100]})
print(df)
'''
  국어  수학
0  50  100
1  60  100
2  70  100
3  80  100
4  90  100
'''

# 7. df에 임의의 함수 적용 ==> 콜백함수
x = df.apply(np.sum, axis=0)
print(x)
'''
국어    350
수학    500
'''
x = df.apply(sum, axis=1)
print(x)
'''
0    150
1    160
2    170
3    180
4    190
'''

# 8. df.isin(집합형) - 중요, SQL의 in연산자와 비슷
new_df = df.isin([60,80])
print(new_df)
'''
    국어    수학
0  False  False
1   True  False
2  False  False
3   True  False
4  False  False
'''
new_df = df.isin({"국어": [60,80]})  # 국어에서만 60 또는 80이 있는지



df = pd.DataFrame({ "col1" : [1 ,2, 3, None, 1],
                    "col2" : [2, 3, 2, 2, np.nan],
                    "col3" : [ np.nan, 3, 2, 3, 3],
                    "col4" : [ np.nan, np.nan, np.nan, np.nan, np.nan]},
                    index = [1, 2, 3, 4, 5])
print(df)
'''
   col1  col2  col3  col4
1   1.0   2.0   NaN   NaN
2   2.0   3.0   3.0   NaN
3   3.0   2.0   2.0   NaN
4   NaN   2.0   3.0   NaN
5   1.0   NaN   3.0   NaN
'''

# 9. unique한 값의 개수 반환 - 기본적으로 null 제외
x = df.nunique(axis=0)
print(x)
'''
col1    3
col2    2
col3    2
col4    0
dtype: int64
'''
x = df.nunique(axis=1)
print(x)
'''
1    2
2    2
3    2
4    2
5    2
dtype: int64
'''

x = df.nunique(axis=0, dropna=False)  # null값 포함
print(x)
'''
col1    4
col2    3
col3    3
col4    1
dtype: int64
'''

# 10. 필터링: df.query(조건식)
df = pd.DataFrame({"국어":[50,60,70,80,90],"수학":[100,60,100,100,80]})
print(df)
'''
  국어  수학
0  50  100
1  60  60
2  70  100
3  80  100
4  90  80
'''
new_df = df.query("국어 > 70")
print(new_df)
'''
   국어   수학
3  80  100
4  90  80
'''
new_df = df.query("국어 in [50,80,90]")
print(new_df)
'''
   국어   수학
0  50  100
3  80  100
4  90  80
'''
new_df = df.query("국어 in [50,80,90] and 수학 > 90")
print(new_df)
'''
   국어   수학
0  50  100
3  80  100
'''
new_df = df.query("국어 < 수학")
print(new_df)
'''
   국어   수학
0  50  100
2  70  100
3  80  100
'''