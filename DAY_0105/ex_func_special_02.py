# -----------------------------------------------------------------------------------
# 다양한 함수의 형태 - 특별한 함수(2)
# - 매개변수의 갯수를 유동적으로 가변으로 하는 함수
# - 키와 값의 덩어리 데이터
#
# - 형태: def 함수명( **data ):
# - 가변 인자 함수
# - 매개 변수 갯수 : 0개 ~ N개
# - 호출 : 함수명(키1=값1)
#          함수명(키1=값1, 키2=값2, 키3=값3)
#          함수명()
# -----------------------------------------------------------------------------------

aDict = {'name':'Hong','age':100}
aDict.update(job='학생')
aDict.update(job='학생', birth = '1112', blood='A')
# print(aDict)        # .update() 는 가변인자 **를 사용
aDict.update(점수1=100)



# -------------------------------------------------------------
# 함수 기능 : 회원 가입 기능(1)
# 함수 이름 : joinMember
# 매개 변수 : 이름, 전화 번호, 아이디, 이메일, 취미, 주소, 생일, ......
#            가변 + 데이터 정보 함께
#            키워드 파라미터 **member
#  반 환 값 : '가입 완료 되었습니다.' str
# -------------------------------------------------------------
def joinMember(**member):       # dict 값으로 들어온다. # **찍으면 dict가 풀려서 key = value 으로 들어간다
    print(member)
    # 멤버 저장소에 멤버 추가하기
    # members.append(member)        # list로 묶는 방법
    # for k, v in member.items():
    #     print(k, v)             # 이 방법으로는 .items()으로 쪼개서 zip으로 묶어서 다시 넣어야 하므로 복잡
    members[f"M{len(members) + 1}"]=member


# -------------------------------------------------------------
# 함수 사용 즉 호출
# -------------------------------------------------------------
# 가입된 회원들 저장 변수
members = {}
print(f'[Bf] : {members}')
# 회원가입 기능 함수 호출
joinMember(name='Hong', age=17, birth='2020/10/10')
joinMember(id='Hong84', phone='010-1111-2222', job='actor', blood='B')
joinMember(id='baby', birth='2024/01/01', blood='A')
print(f'[Af] : {members}')


# m={'name':'Hong', 'age':17}
# print(m.keys())
# print(m.values())
# print(m.items())



# -------------------------------------------------------------
# 함수 기능 : 회원 가입 기능(2)
# 함수 이름 : joinMember
# 매개 변수 : 필수 => id, pw
#            선택 => **option 이름, 전화 번호, 아이디, 이메일, 취미, 주소, 생일, ....
#            가변 + 데이터 정보 함께
#  반 환 값 : '가입 완료 되었습니다.' str
# -------------------------------------------------------------
def joinMember2(id, pw, **option):          # 가변인자는 무조건 뒤로 보내라
    print("ok")



# -------------------------------------------------------------
# 함수 사용 즉 호출
# -------------------------------------------------------------
# 가입된 회원들 저장 변수
members = {}
print(f'[Bf] : {members}')

# 회원가입 기능 함수 호출
joinMember2('h','ph')
joinMember2('h','ph', phone='010-1111-2222', blood='A')
# joinMember2(id='Hong84', phone='010-1111-2222', job='actor', blood='B')
# joinMember2(id='baby', birth='2024/01/01', blood='A')
print(f'[Af] : {members}')



# -------------------------------------------------------------
# 함수 기능 : 회원 가입 기능(3)
# 함수 이름 : joinMember
# 매개 변수 : 필수 => id, pw, loc, gender
#            선택 => **option 이름, 전화 번호, 아이디, 이메일, 취미, 주소, 생일, ....
#            가변 + 데이터 정보 함께
#  반 환 값 : '가입 완료 되었습니다.' str
# -------------------------------------------------------------
def joinMember3(id, pw, loc='내국인', gender='남자', **option):
    print(id, pw, loc, gender)
    # 키 => id
    # 값 => pw, loc='내국인', gender = '남자', **option
    #           {'pw':'123', 'loc':'내국인','gender':'남자', 'ect':{option}}
    valueDict = {}
    valueDict['pw']=pw
    valueDict['loc']=loc
    valueDict['gender']=gender
    valueDict['ect']=option
    members[id] = valueDict


# -------------------------------------------------------------
# 함수 사용 즉 호출
# -------------------------------------------------------------
# 가입된 회원들 저장 변수
members = {}
print(f'[Bf] : {members}')

# 회원가입 기능 함수 호출
joinMember3('h1','ph')
# joinMember3('h2','ph', '여자')
joinMember3('h3','ph', gender='여자')      # 디폴트 매개변수를 설정해서 놔둬야 함
joinMember3('h4','ph', phone='010-1111-2222', blood='A')
# joinMember2(id='Hong84', phone='010-1111-2222', job='actor', blood='B')
# joinMember2(id='baby', birth='2024/01/01', blood='A')
print(f'[Af] : {members}')
for m in members.items(): print(m)