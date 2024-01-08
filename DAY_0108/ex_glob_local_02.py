# ---------------------------------------------------------------------
# 전역 변수(Global Variable)와 지역변수(Local Variable)
# - 함수 내에서 전역 변수 값 변경 하고자 하는 경우는 추가 코드 필요
# - 추가 코드 : global 전역 변수명
# -> 주의: 전역변수 값이 언제든지 함수로 변경될수 있는 상황 사용시에 주의 필요함
# 사용자 정의 함수 -------------------------------------------------------

def currentData(year, month, day):
    # year, month, day => 지역 변수
    print(f'Today: {year}/{month:0>2}/{day:0>2}')

def currentData2(month, day):
    # month, day => 지역 변수
    global year
    # 함수 내에서 전역변수 값을 변경하고자 하는 경우는 =lo=avl
    # year => 전액 변수
    print(f'Today: {year}/{month:0>2}/{day:0>2}')



def currentData3(month, day, week):
    # year, month, day => 지역 변수
    print(f'Today: {year}/{month:0>2}/{day:0>2}/{week}요일')

# 전역 변수 -----------------------------------------------------------------------------------
year, month, day = 2024, -1 ,8

# 함수 사용 즉 함수 호출 -----------------------------------------------------------------------
currentData3(month, day, 'Friday')

# 변수 값 확인 출력
print(f'year: {year}, month : {month}, day : {day}')

# 함수의 변수인 지역변수는 함수 밖에서 사용 불가------------------------------------------------------------
# print(f'week: {week}')
