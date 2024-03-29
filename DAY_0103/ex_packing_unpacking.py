# --------------------------------------------------------------------------
# 팩킹(Packing) & 언팩킹(Unpacking)
# --------------------------------------------------------------------------
msg = "Happy New Year"
msgList = msg.split()
# Happy만 출력하는 법

# 팩킹(Packing) 방식
print(msgList[0])

# 언팩킹(Unpacking) 방식
# 데이터수와 변수 수가 동일해야함

m1, m2, m3 = msg.split()
print(m1, m2, m3)

# 데이터와 변수 수가 달라서 에러 발생
# m1, m2 = msg.split()
# print(m1, m2)

# 변수를 여러 개 생성하는 경우 -------------------------------------------------
age = 12
name = "Hong"
job = "학생"

# 튜플을 언팩킹으로 생성 가능
age1, name1, job1 = 12, "Hong", "학생"
info = (12, "Hong", '학생')

age2, name2, job2 = info
print(age2, name2, job2)
