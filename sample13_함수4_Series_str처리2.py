
import numpy as np
import pandas as pd

from pandas import Series
print(dir(Series.str))
'''
['capitalize', 'casefold', 'cat', 'center', 'contains', 'count', 
'decode', 'encode', 'endswith', 'extract', 'extractall', 
'find', 'findall', 'fullmatch', 'get', 'get_dummies', 
'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'islower', 
'isnumeric', 'isspace', 'istitle', 'isupper', 'join', 'len', 'ljust', 'lower', 'lstrip', 
'match', 'normalize', 'pad', 'partition', 'removeprefix', 'removesuffix', 'repeat', 
'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 
'slice', 'slice_replace', 'split', 'startswith', 'strip', 'swapcase', 
'title', 'translate', 'upper', 'wrap', 'zfill']
'''
info={"name":["Hello","Happy","Cat"],
      "age":[18,31, 33],
      "birthday":['1920/09/28','1910/03/26','2020/03/26']}
df = pd.DataFrame(info)
print(df)
'''
    name  age    birthday
0  Hello   18  1920/09/28
1  Happy   31  1910/03/26
2    Cat   33  2020/03/26
'''

# 1. series.str.replace(old, new)
df['name1'] = df['name'].str.replace("Hello", "hello")
print(df)
'''
    name  age    birthday  name1
0  Hello   18  1920/09/28  hello
1  Happy   31  1910/03/26  Happy
2    Cat   33  2020/03/26    Cat
'''

# 2. 인덱싱 및 slice
df['name2'] = df['name'].str[::-1]
print(df)
'''
    name  age    birthday  name1  name2
0  Hello   18  1920/09/28  hello  olleH
1  Happy   31  1910/03/26  Happy  yppaH
2    Cat   33  2020/03/26    Cat    taC
'''

df['name3'] = df['name'].str[1:]
print(df)
'''
   name  age    birthday  name1  name2 name3
0  Hello   18  1920/09/28  hello  olleH  ello
1  Happy   31  1910/03/26  Happy  yppaH  appy
2    Cat   33  2020/03/26    Cat    taC    at
'''

# 3. upper, lower
df['name4'] = df['name'].str.upper()
df['name5'] = df['name'].str.lower()
print(df)
'''
    name  age    birthday  name1  name2 name3  name4  name5
0  Hello   18  1920/09/28  hello  olleH  ello  HELLO  hello
1  Happy   31  1910/03/26  Happy  yppaH  appy  HAPPY  happy
2    Cat   33  2020/03/26    Cat    taC    at    CAT    cat
'''

# 4. contains
df['name6'] = df['name'].str.contains('a')
print(df)
'''
    name  age    birthday  name1  name2 name3  name4  name5  name6
0  Hello   18  1920/09/28  hello  olleH  ello  HELLO  hello  False
1  Happy   31  1910/03/26  Happy  yppaH  appy  HAPPY  happy   True
2    Cat   33  2020/03/26    Cat    taC    at    CAT    cat   True
'''

df['name7'] = df['name'].str.contains('a|e')
print(df)
'''
    name  age    birthday  name1  name2 name3  name4  name5  name6  name7
0  Hello   18  1920/09/28  hello  olleH  ello  HELLO  hello  False   True
1  Happy   31  1910/03/26  Happy  yppaH  appy  HAPPY  happy   True   True
2    Cat   33  2020/03/26    Cat    taC    at    CAT    cat   True   True
'''