import numpy as np
import pandas as pd

import pandas as pd
import numpy as np

# 4. 컬럼 추가 및 삽입
'''
   DataFrame에 컬럼 추가
   ==> 기존 컬럼 값을 가지고 추가 정보를 얻을 떄

  1.  df['컬럼명'] = 리스트
      df['컬럼명'] = Series
      
  2.  new_df = df.assign(컬럼명=리스트)
  3.  new_df = df.assign(컬럼명=함수, 컬럼명=함수)
  4.  new_df = pd.concat([df,df2], axis=1)

  DataFrame에 컬럼 삽입

   1. df.insert(idx, 컬럼명, 값 )

'''

df = pd.DataFrame({"이름": ['홍길동', '이순신', '유관순', '강감찬'],
                   "국어": [30, 26, 11, 10],
                   "수학": [20, 12, 20, 12]
                   }, index=[1, 2, 3, 4])
print("1. DataFrame")
print(df)
'''
    이름  국어  수학
1  홍길동  30  20
2  이순신  26  12
3  유관순  11  20
4  강감찬  10  12
'''

# 2. new_df = df.assign(컬럼명=리스트)
new_df = df.assign(영어=[50,60,70,80])
print(df)  # 변함없음, 원본 수정하려면 df = df.assign(영어=[50,60,70,80])
print(new_df)
'''
    이름  국어  수학  영어
1  홍길동  30  20  50
2  이순신  26  12  60
3  유관순  11  20  70
4  강감찬  10  12  80
'''

df = df.assign(영어=[50,60,70,80])  # 따옴표 안씀

# 3.  new_df = df.assign(컬럼명=함수, 컬럼명=함수)
#                            콜백함수
# def total(x):
#     return x["국어"] + x["수학"] + x["영어"]
#
# total = lambda x: x["국어"] + x["수학"] + x["영어"]
# df = df.assign(총합=total)

df = df.assign(총합=lambda x: x["국어"] + x["수학"] + x["영어"])
print(df)
'''
    이름  국어  수학  영어   총합
1  홍길동  30  20  50  100
2  이순신  26  12  60   98
3  유관순  11  20  70  101
4  강감찬  10  12  80  102
'''

# 평균 컬럼 추가하기
df = df.assign(평균=lambda x: np.round(x['총합']/3,1))
print(df)