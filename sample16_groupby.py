
'''
    groupby

    # 1. 기본
    df.groupby('그룹으로 묶을 컬럼명')['선택컬럼'].그룹함수
    예> emp.groupby(by="deptno")['sal'].sum()

    # 2. apply/agg/aggregate함수
    df.groupby('그룹으로 묶을 컬럼명')['선택컬럼'].agg(함수명)
'''

import numpy as np
import pandas as pd
import seaborn as sns

# 5. df.groupby 이용
df = sns.load_dataset("mpg")
print(df.head(10))
'''
    mpg  cylinders  displacement  ...  model_year  origin                       name
0  18.0          8         307.0  ...          70     usa  chevrolet chevelle malibu
1  15.0          8         350.0  ...          70     usa          buick skylark 320
2  18.0          8         318.0  ...          70     usa         plymouth satellite
3  16.0          8         304.0  ...          70     usa              amc rebel sst
4  17.0          8         302.0  ...          70     usa                ford torino
5  15.0          8         429.0  ...          70     usa           ford galaxie 500
6  14.0          8         454.0  ...          70     usa           chevrolet impala
7  14.0          8         440.0  ...          70     usa          plymouth fury iii
8  14.0          8         455.0  ...          70     usa           pontiac catalina
9  15.0          8         390.0  ...          70     usa         amc ambassador dpl
'''

print(df['origin'].value_counts())  # 어떤 종류가 있고 종류별 인덱스 개수 알고 싶을 때 많이 씀(중요!)
'''
origin
usa       249
japan      79
europe     70
Name: count, dtype: int64
'''

gb = df.groupby("origin")
print(gb)  # <pandas.core.groupby.generic.DataFrameGroupBy object at 0x000001376BB64A60>

'''
select deptno, sum()
from emp
group by deptno

df.group("deptno")
'''

department = {"deptno":[10,20,30,40],'dname':['개발','인사','영업','관리'],'loc':['서울','부산','제주','광주']}
employee = {"empno":['A1','A2','A3','A4','A5'],"ename":['홍길동','유관순','안중근','강감찬','이순신'],
            "sal":[1000,1500,2300,3400,4500],"hireday":['2019/01/02','2018/01/02','2017/01/02','2016/01/02','2015/01/02'],
            "deptno":[10,20,10,30,10]}
dept = pd.DataFrame(department)
emp = pd.DataFrame(employee)
print(dept)
'''
   deptno dname loc
0      10    개발  서울
1      20    인사  부산
2      30    영업  제주
3      40    관리  광주
'''
print(emp)
'''
  empno ename   sal     hireday  deptno
0    A1   홍길동  1000  2019/01/02      10
1    A2   유관순  1500  2018/01/02      20
2    A3   안중근  2300  2017/01/02      10
3    A4   강감찬  3400  2016/01/02      30
4    A5   이순신  4500  2015/01/02      10
'''

# 1. 부서별 sal 합, 평균, 최대, 최소, 개수
xxx = emp.groupby(by="deptno")['sal'].sum()  # by 안 써도 똑같음
print(xxx)
'''
deptno
10    7800
20    1500
30    3400
Name: sal, dtype: int64
'''
xxx = emp.groupby(by="deptno")['sal'].mean()
print(xxx)
'''
deptno
10    2600.0
20    1500.0
30    3400.0
Name: sal, dtype: float64
'''
xxx = emp.groupby(by="deptno")['sal'].max()
print(xxx)
'''
deptno
10    4500
20    1500
30    3400
Name: sal, dtype: int64
'''
xxx = emp.groupby(by="deptno")['sal'].min()
print(xxx)
'''
deptno
10    1000
20    1500
30    3400
Name: sal, dtype: int64
'''
xxx = emp.groupby(by="deptno")['sal'].count()
print(xxx)
'''
deptno
10    3
20    1
30    1
'''
print(pd.DataFrame(xxx))
'''
        sal
deptno     
10        3
20        1
30        1
'''

# 2. apply 또는 agg 함수
def my_mean(v):
    print(">>", v)  # deptno별 sal 값 전달됨
    n= len(v)
    sum=0
    for k in v:
        sum+=k
    return sum/n

xxx = emp.groupby(by="deptno")['sal'].agg(my_mean)  # 사용자 정의함수
xxx = emp.groupby(by="deptno")['sal'].agg(np.mean)  # numpy의 그룹함수
xxx = emp.groupby(by="deptno")['sal'].agg("mean")  # python의 그룹함수
print(xxx)
'''
deptno
10    2600.0
20    1500.0
30    3400.0
Name: sal, dtype: float64
'''

# 2. apply 또는 agg 함수 적용 - 멀티함수 적용
xxx = emp.groupby(by="deptno")['sal'].agg([np.sum, np.mean, np.max, np.size])  # numpy의 그룹함수
print(xxx)
'''
         sum    mean  amax  size
deptno                          
10      7800  2600.0  4500     3
20      1500  1500.0  1500     1
30      3400  3400.0  3400     1
'''
xxx = emp.groupby(by="deptno")['sal'].agg(["sum", "mean", "max", "count"])  # python의 그룹함수
print(xxx)
'''
        sum    mean   max  count
deptno                           
10      7800  2600.0  4500      3
20      1500  1500.0  1500      1
30      3400  3400.0  3400      1
'''