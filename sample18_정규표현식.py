'''
    정규 표현식(regular expression)
'''
import re
sentence = 'This is a sample string'

# 1) re.search( pattern, string,  flags ) 함수
print(bool(re.search(r"is", sentence)))  # True
print(bool(re.search(r"xyz", sentence)))  # False

# flag 사용하여 대소문자 무시
sentence = 'This is a sample string'
print(bool(re.search(r'this', sentence)))  # False
print(bool(re.search(r'this', sentence, flags=re.I)))  # True

# 2) re.compile( pattern,  flags ) 함수 사용 pattern 재사용
sentence = 'This is a sample string'
sentence2 = 'is This a sample string?'

# 패턴 중복
print(bool(re.search(r'this', sentence)))
print(bool(re.search(r'this', sentence2)))

pet = re.compile(r'this', flags=re.I)
print(bool(pet.search(sentence)))# True
print(bool(pet.search(sentence2)))# True

# 일치하는 패턴 존재여부 확인
#############################################

# 3) re.sub(search, rep, str ) 함수 사용한 치환
print(re.sub(r'A', 'X', "ABC")) # XBC

# 4) 패턴 한정
'''
     String anchors
     1. \A, ^:  문자열의 시작 부분으로 패턴 한정
     2. \Z, $ :  문자열의 끝 부분으로 패턴 한정
'''
# print(bool(re.search(r'\Acat', 'cater')))  # True
# print(bool(re.search(r'cat', 'concatenation')))  # True
# print(bool(re.search(r'\Acat', 'concatenation')))  # False

print(bool(re.search(r'^cat', 'cater')))  # True
print(bool(re.search(r'cat', 'concatenation')))  # True
print(bool(re.search(r'^cat', 'concatenation')))  # False

# print(bool(re.search(r'are\Z', 'spare')))    # True
# print(bool(re.search(r'are', 'nearest')))  # True
# print(bool(re.search(r'are\Z', 'nearest')))  # False

print(bool(re.search(r'are$', 'spare')))    # True
print(bool(re.search(r'are', 'nearest')))  # True
print(bool(re.search(r'are$', 'nearest')))  # False

# 5) 선택 ( Alternation ) 및 그룹화
'''
    선택 ( Alternation ) 

    1.  | 이용
    2. abd | acd = a(b|c)d

'''

pet = re.compile(r'cat|dog')
print(bool(pet.search('I like cats')))  # True
print(bool(pet.search('I like dogs')))  # True
print(bool(pet.search('I like parrots')))  # False

# without grouping
print(re.sub(r'reform|rest', 'X', 'red reform read arrest'))   # red X read arX
# with grouping
print(re.sub(r're(form|st)', 'X', 'red reform read arrest'))   # red X read arX

alt = re.compile(r're(form|st)')
print(alt.sub('X', 'red reform read arrest')) # red X read arX

# 6) dot
'''
         1. 줄바꿈 문자인 \n 제외한 모든 문자(하나)와 매치 ( 한글, 숫자 포함 )
         2.  .x  ==> x 앞에 어떤 문자가 있다.
'''
print(bool(re.search(r'a.b','axb'))) # true
print(bool(re.search(r'a.b','a0b'))) # true
print(bool(re.search(r'a.b','a홍b'))) # true
print(bool(re.search(r'a.b','axxb')) ) # False

print(bool(re.search(r'a[.]b','a.b')))  # a.b 와 매치 , true

# 6) +
# '''
#              1. 반복 처리
#              2.  x+  ==> x가 1번 이상 반복될 수 있다.
# '''
print(bool(re.search(r'ca+b','cb'))) # False
print(bool(re.search(r'ca+b','cab'))) # true
print(bool(re.search(r'ca+b','caaaab'))) # true
print(bool(re.search(r'ca+b','cacb')) ) # False

# 7) ?
# '''
#              1. 없거나 1번 있거나
#              2.  x?  ==> x가 1번 나오거나 안나올수 있다.
# '''
print(bool(re.search(r'ca?b','cb'))) # true
print(bool(re.search(r'ca?b','cab'))) # true
print(bool(re.search(r'ca?b','caab'))) # False
print(bool(re.search(r'ca?b','caaab')) ) # False

# 8) *
# '''
#              1. 없거나  여러번 있거나
#              2.  x*  ==> x가 없거나 여러번 나올수 있다.
# '''
print(bool(re.search(r'ca*b','cb'))) # true
print(bool(re.search(r'ca*b','cab'))) # true
print(bool(re.search(r'ca*b','caaaab'))) # true

# 9) {n,[m]}
# '''
#               x{n}: n번 반복
#               x{n, } : n번 이상 반복
#               x{,m} : 없거나 m번 이하 반복
#               x{n,m} : n번 이상 m 번 이하 반복
# '''
#  a가 3번 반복
print(bool(re.search(r'ca{3}b','cb'))) # False
print(bool(re.search(r'ca{3}b','cab'))) # False
print(bool(re.search(r'ca{3}b','caaab'))) # true

#  a가 2번 이상 반복
print(bool(re.search(r'ca{2,}b','cb'))) # False
print(bool(re.search(r'ca{2,}b','cab'))) # False
print(bool(re.search(r'ca{2,}b','caab'))) # true
print(bool(re.search(r'ca{2,}b','caaab'))) # true

#  a가 1번 이상 2번 이하 반복
print(bool(re.search(r'ca{1,2}b','cb'))) # False
print(bool(re.search(r'ca{1,2}b','cab'))) # true
print(bool(re.search(r'ca{1,2}b','caab'))) # true
print(bool(re.search(r'ca{1,2}b','caaab'))) # False

# 10) x[ab]
# '''
#   [] 안의 문자중 하나, 만약  a-b 사용하면 from ~ to 의미
#
#              [bts] : b 또는 t 또는 s
#              [a-z] : 알파벳 소문자 하나
#              [A-Z] : 알파벳 대문자 하나
#              [0-9] : 숫자 하나
#              [가-힣]: 한글 하나
#              [a-zA-Z0-9] : 알파벳 대/소, 숫자중 하나
# '''

#  1. 문자중 하나
print(bool(re.search(r'[abc]' , "abcx"))) # true
print(bool(re.search(r'[abc]' , "xyz"))) # False

# 2. 범위중 하나
print(bool(re.search(r'[a-d]', "xdbc"))) # true
print(bool(re.search(r'[a-d]', "xyz"))) # False
print(bool(re.search(r'[A-Z]',"Abc"))) # true
print(bool(re.search(r'[0-9]',"9Abc"))) # true
print(bool(re.search(r'[a-zA-Z]',"xAbc"))) # true
print(bool(re.search(r'[a-zA-Z0-9가-힣]',"99xAbc"))) # true

# findall() : 정규식과 일치하는 모든 문자열을 찾아서 list 로 반환
result = re.findall(r'[a-zA-Z]',"99xAbc") # ['x', 'A', 'b', 'c']
result = re.findall(r'[가-힣]',"홍99박xAbc제주") # ['홍', '박', '제', '주']
print(result)

# 11) x[^ab]
# '''
#  1. [^] : [] 안에 ^이 사용되면 시작문자가 아닌 부정의 의미
#
#              [^bts] : b 또는 t 또는 s 가 아닌것
#              [^a-z] : 알파벳 소문자 하나가 아닌것
#              [^A-Z] : 알파벳 대문자 하나가 아닌것
#              [^0-9] : 숫자 하나가 아닌것
#              [^가-힣]: 한글 하나가 아닌것
#              [^a-zA-Z0-9] : 알파벳 대/소, 숫자중 하나가 아닌것
# '''

# 12) escape 문자
# '''
#    \d :   [0-9]와 동일
#    \D :   [^0-9]와 동일
#    \s :   whitespace 문자와 일치
#    \S :   whitespace 문자가 아닌 문자와 일치
#    \w :   [a-zA-Z0-9가-힣_]와  동일
#    \W :   [^a-zA-Z0-9가-힣_]와  동일
#    \. :   . 문자와 동일
#    \* :   * 문자와 동일
#    \+ :   + 문자와 동일
#    \? :   ? 문자와 동일
#    \$ :   $ 문자와 동일
# '''

result = re.search(r'\d',"9Abc") # [0-9]와 동일
result = re.search(r'\D', "Abc")  # [^0-9]와 동일
result = re.search(r'\s', ' 9Abc') # [ \n\t\r\f\v]와  동일, 즉 whitespace 문자와 일치
result = re.search(r'\s', '9 Abc') # [ \n\t\r\f\v]와  동일, 즉 whitespace 문자와 일치
result = re.search(r'\S','9Abc') # [^ \n\t\r\f\v]와  동일,
result = re.search(r'\w', '홍9Abc') # [a-zA-Z0-9가-힣_]와  동일, 문자,숫자와 일치 ==> 한글포함
result = re.search(r'\w', '홍길동') # [a-zA-Z0-9가-힣_]와  동일, 문자,숫자와 일치 ==> 한글포함
result = re.search(r'\W', '9Abc') # None, [^a-zA-Z0-9가-힣_]와  동일,
result = re.search(r'\W', '9Abc%$') #  [^a-zA-Z0-9가-힣_]와  동일,
result = re.search(r'\.', '9Ab.c')  #  . 문자와 동일
result = re.search(r'\*', '9Ab*c')  #  * 문자와 동일
result = re.search(r'\+', '9A+b*c') #  + 문자와 동일
result = re.search(r'\?', '9A+b*c?') # ? 문자와 동일
result = re.search(r'\$', '9$A+b*c?') # $ 문자와 동일
print(bool(result))