# pip install cx_Oracle
#

import cx_Oracle

user = "SCOTT"
pw = "TIGER"
dsn = "localhost:1521/xe"

# connect 메서드: python과 oracle서버 연결
con = cx_Oracle.connect(user, pw, dsn, encoding="UTF-8")
print("Database version:", con.version)  # Database version: 11.2.0.2.0

# 1. 특정 레코드 하나 얻기. deptno = 10
with con.cursor() as cur:  # 자동으로 cursor close 됨
    cur.execute("select * from dept where deptno =:x", x=10)  # 바인딩 변수 ':변수' -> 커서에 데이터 하나 갖다 놓음
    res = cur.fetchone()
    print(res)  # (10, 'ACCOUNTING', 'NEW YORK')

# 2. 멀티 레코드 얻기
with con.cursor() as cur:
    cur.execute("select * from dept order by deptno")
    res = cur.fetchall()  # list로 반환
    print(res)  # [(10, 'ACCOUNTING', 'NEW YORK'), (20, 'RESEARCH', 'DALLAS'), (30, 'SALES', 'CHICAGO'), (40, 'OPERATIONS', 'BOSTON')]
    for row in res:
        print(row)
# (10, 'ACCOUNTING', 'NEW YORK')
# (20, 'RESEARCH', 'DALLAS')
# (30, 'SALES', 'CHICAGO')
# (40, 'OPERATIONS', 'BOSTON')

# 3. 단일 저장
# with con.cursor() as cur:
#     cur.execute( "insert into dept (deptno, dname, loc) values " \
#                  " (:deptno, :dname, :loc)", deptno=99, dname='개발', loc="서울")
#     print("저장된 레코드갯수:", cur.rowcount)  # 저장된 레코드갯수: 1
#     con.commit()

# 4. 멀티 저장
# with con.cursor() as cur:
#     rows = [(1, "개발","서울"), (2, "개발","서울")]
#
#     cur.executemany("insert into dept (deptno, dname, loc) values  (:1, :2, :3)", rows)
#     print("저장된 레코드갯수:", cur.rowcount)  # 저장된 레코드갯수: 2
#     con.commit()

# 6. 수정
with con.cursor() as cur:
    cur.execute("update dept set dname = :x, loc= :y "
                " where deptno = :z", x="개발부", y="서울시", z=1)
    print("수정된 레코드갯수:", cur.rowcount)
    con.commit()

# 7. 삭제
with con.cursor() as cur:
    cur.execute("delete from dept where deptno = :z", z=2)
    print("삭제된 레코드갯수:", cur.rowcount)
    con.commit()

con.close()  # 맨 마지막에 자원 반납