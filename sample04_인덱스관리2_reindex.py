# 2. 인덱스 관리

import numpy as np
import pandas as pd

'''
    인덱스 관리
    
    1. df.set_index(기존컬럼, inplace=True|False)
    
       df.reset_index(drop=False, inplace=True) # 기존 index를 컬럼으로 변경하고 새로운 index 생성
       df.reset_index(drop=True, inplace=True) # 기존 index를 삭제하고 새로운 index 생성
           
       df.reindex(index=값)  # 기존 index 재배치
'''

df = pd.DataFrame({    "date":['2021','2022','2023','2024','2025'],
                       "City": ["Seoul", "Seoul", "Seoul", "Seoul", "Seoul"],
                       "Temperature": [32, 34, 33, 32, 35]
                       }, index=list('AECBD'))
print(df)
'''
   date   City  Temperature
A  2021  Seoul           32
B  2022  Seoul           34
C  2023  Seoul           33
D  2024  Seoul           32
E  2025  Seoul           35

'''

# 3. 인덱스 재배치
new_df = df.reindex(index=list('ABCDE'))  # inplace 없음
print(df)
'''
   date   City  Temperature
A  2021  Seoul           32
E  2022  Seoul           34
C  2023  Seoul           33
B  2024  Seoul           32
D  2025  Seoul           35
'''
print(new_df)
'''
   date   City  Temperature
A  2021  Seoul           32
B  2024  Seoul           32
C  2023  Seoul           33
D  2025  Seoul           35
E  2022  Seoul           34
'''
