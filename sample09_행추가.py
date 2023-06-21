import pandas as pd
import numpy as np

# 6. 행 추가 및 삭제
'''
   DataFrame 행(row) 추가

  1. 한번에 하나씩 추가 
    new_df = df._append(df2, ignore_index=True) --> 버전업 1.3.0 이후에는 _append로 바뀜

  2. 한번에 여러개 추가
    new_df = pd.concat([df,df2,..], axis=0 , ignore_index=True)


      DataFrame 행 삭제

   1. new_df = df.drop(index=[인덱스명, 인덱스명])

   2. new_df = df.drop([인덱스명, 인덱스명], axis=0)

'''

# 1. 한번에 하나씩 추가
info={"Name":["유관순","안중근"],"age":[18,31],"birthday":['1920/09/28','1910/03/26']}
df = pd.DataFrame(info)
print(df)
'''
  Name  age    birthday
0  유관순   18  1920/09/28
1  안중근   31  1910/03/26
'''
info2 = {"Name":["홍길동","강감찬"],"age":[22,43],"birthday":['1990/09/28','1980/03/26']}
df2 = pd.DataFrame(info2)
print(df2)
'''
  Name  age    birthday
0  홍길동   22  1990/09/28
1  강감찬   43  1980/03/26
'''

# 1. 한번에 하나씩 추가
new_df= df._append(df2, ignore_index=True)  # 바뀜
print(new_df)

# 2. 한번에 여러개 추가
new_df = pd.concat([df, df2], ignore_index=True)
print(new_df)
'''
  Name  age    birthday
0  유관순   18  1920/09/28
1  안중근   31  1910/03/26
2  홍길동   22  1990/09/28
3  강감찬   43  1980/03/26
'''

new_df = pd.concat([df, df2, df2, df2], ignore_index=True)
print(new_df)
'''
  Name  age    birthday
0  유관순   18  1920/09/28
1  안중근   31  1910/03/26
2  홍길동   22  1990/09/28
3  강감찬   43  1980/03/26
4  홍길동   22  1990/09/28
5  강감찬   43  1980/03/26
6  홍길동   22  1990/09/28
7  강감찬   43  1980/03/26
'''