## 3. Series의 기본 함수
import numpy as np
import pandas as pd

'''
   1. 값 변경                                  ==> df[컬럼].replace()
   2. 컬럼명 및 인덱스명 변경                     ==> df[컬럼].rename(columns|index)
   3. 모든(특정) 컬럼(행)값의 참/거짓 여부          ==> df[컬럼].any() , df[컬럼].all()
   4. 중복조회 및 제거                           ==> df[컬럼].duplicated(),  df[컬럼].drop_duplicates()

   5. 임의의 함수 적용 ==> df[컬럼].apply(함수, axis=0|1)
      임의의 함수를 한번에 DataFrame의 행과 열에 적용.

   6. 값이 있으면 True, 아니면 False ==> df[컬럼].isin(집합형)

    7. df['col1].unique ==> 유니크 값 반환, series만 사용가능
    
    8. df['col1'].value_counts() ==> 값의 빈도수 반환
    
    9. df['col1'].between(start, end) ==> 범위에 있으면 True, 없으면 False
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

# 1. 값 변경
new_df = df['a'].replace({0:-1, 10:-2})
print(new_df)
'''
A     -1
B     -2
C    100
'''

# 2. 컬럼명 변경
x = df['a'].rename("col1")
print(x)
'''
A      0
B     10
C    100
Name: col1, dtype: int64
'''

# 3. 참/거짓 여부
x = df['a'].all()
print(x)  # False(0 있음)
x = df['a'].any()
print(x)  # True

# a 컬럼 값이 모두 10보다 큰지 확인
x = (df['a']>10).all(0)
print(x)  # False



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

# 4. 중복여부
x = df['k1'].duplicated()
print(x)
'''
0    False
1     True
2     True
3    False
4     True
5     True
6     True
Name: k1, dtype: bool
'''

# 5. 중복 제거 후 반환
x = df['k1'].drop_duplicates(ignore_index=True)
print(x)
'''
0    one
1    two
Name: k1, dtype: object
'''



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

# 6. df에 임의의 함수 적용 ==> 콜백함수
x = df['국어'].apply(np.sum)  # np.sum 연산은 했으나 결과값은 동일. 그룹함수 적용 가능
x = df['국어'].apply(lambda n: n+1)  #lambda 적용가능
print(x)

# 7. df['국어'].isin(집합형) - 중요, SQL의 in연산자와 비슷
new_df = df['국어'].isin([60,80])
print(new_df)
'''
0    False
1     True
2    False
3     True
4    False
'''



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
x = df['col1'].nunique()
print(x)  # 3

x = df['col1'].nunique(dropna=False)
print(x)  # 4

# 10. df['col1'].unique()  ==> 유니크 값 반환
x = df['col1'].unique()
print(x)  # [ 1.  2.  3. nan]

# 11. df['col1'].value_counts() ==> 값의 빈도수 반환
x = df['col1'].value_counts()
x = df['col2'].value_counts(ascending=True)
print(x)
'''
col2
3.0    1
2.0    3
Name: count, dtype: int64
'''
x = df['col2'].value_counts(ascending=True, dropna=False)
print(x)
'''
col2
3.0    1
NaN    1
2.0    3
Name: count, dtype: int64
'''


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

# 12. df['col1'].between(start, end) (Series에만)
x = df['국어'].between(70,100)
print(x)
'''
0    False
1    False
2     True
3     True
4     True
Name: 국어, dtype: bool
'''