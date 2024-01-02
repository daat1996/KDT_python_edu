# ------------------------------------------------------------------------------------
# 다양한 dict 자료형 => key:value  <= 데이터 덩어리
# - key로 데이터를 찾기/읽기/삭제/변경
# - key 중복 X => 마지막 데이터의 key의 값으로 저장
# ------------------------------------------------------------------------------------
# 이름, 점수 저장하기
jumsuDict = {'Hong':100, 'Park':98, 'Kim':88, 'Hong':50, 'Hong':77} # 중복 입력 시 마지막 key의 값으로 저장

# 'Hong' 키가 여러번 저장되면 제일 마지막 데이터가 저장됨!
print(f'jumsuDict => {jumsuDict}')

# 이름/학년을 키로 해서 점수를 저장 하기 -------------------------------------------------
# jumsuDict = {['Hong',1]:100, ['Park',3]:98, ['Kim',1]:88, ['Hong',4]:50, ['Hong',2]:77}

print(f'jumsuDict => {jumsuDict}')  # unhashable type list : list는 변경가능하기에 key는 바꾸면 안된다 -> 튜플사용
# error!

jumsuDict = {('Hong',1):100, ('Park',3):98, ('Kim',1):88, ('Hong',4):50, ('Hong',2):77}
print(f'jumsuDict => {jumsuDict}')

print(f'jumsuDict[("Hong",1)] => {jumsuDict[("Hong",1)]}')

print(f'jumsuDict[("Hong",2)] => {jumsuDict[("Hong",2)]}')


# 키의 데이터 타입 동일해야 하나요? 아니오
testDict ={1:'Hong', 2.0:'Kim', False:100, "name":'HongGilDong'}
print(f'testDict => {len(testDict)}개, {testDict}')

# 빈 딕셔너리 생성
emDict = {}
print(f'emDict => {type(emDict)}, {len(emDict)}')

print(bool(emDict))

