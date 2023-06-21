import numpy as np
import pandas as pd

'''
3. 조회

    * 행과 컬럼 조회  
    나.  .loc :  label만을 사용한다. ( 기본적으로 index의 label로 인식 )
               label은 single, list, slice 형태 모두 가능하다.
               행과 열을 동시에 조회할 수 있다. df.loc[행,열]
               행과 컬럼 모두 label 만 사용 가능하다.
               
    다.  .iloc :   loc와 유사하지만 정수위치값만을 사용한다.
                  행과 컬럼 모두 위치값 만 사용 가능하다.
'''

## 3) 행 및 컬럼 조회
'''
   DataFrame 의 행과 컬럼 조회 

    1. 행 인덱스의 label 이용 
      ==> 기본 문법은 df.loc[행label, 컬럼label]
      ==> 행label은 인덱스라벨,fancy,슬라이싱,boolean 모두 가능 
      ==> 컬럼label은 인덱스라벨,fancy,슬라이싱,boolean 모두 가능 

    2. 행 인덱스의 위치 이용
    ==> 기본 문법은 df.iloc[행위치, 컬럼위치]

'''
import pandas as pd
import numpy as np

df = pd.DataFrame({"col1": [4, 5, 6, 6, 1],
                   "col2": [7, 8, 9, 9, 2],
                   "col3": [10, 11, 12, 12, 10]},
                  index=list("ABCDE"))
print(df)
'''
   col1  col2  col3
A     4     7    10
B     5     8    11
C     6     9    12
D     6     9    12
E     1     2    10

'''

# 1. 인덱싱
print(df.iloc[0,0])  # 4 (스칼라값)

# 2. 인덱싱 + fancy
print(df.iloc[[0,1], 0])  # Series 반환
'''
A    4
B    5
'''

# 3. fancy + fancy
print(df.iloc[[0,1], [0,1]])  # DataFrame 반환
'''
   col1  col2
A     4     7
B     5     8
'''

# 4. slice + fancy
print(df.iloc[1:, [0,1]])  # DataFrame 반환
'''
   col1  col2
B     5     8
C     6     9
D     6     9
E     1     2
'''

# 5. slice + slice
print(df.iloc[1:, 0:])  # DataFrame 반환
'''
   col1  col2  col3
B     5     8    11
C     6     9    12
D     6     9    12
E     1     2    10

'''

# 6. boolean + slice
print(df.iloc[[True,False,True,False,True], 1:])  # DataFrame 반환
'''
   col2  col3
A     7    10
C     9    12
E     2    10

'''
