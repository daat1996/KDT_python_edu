# ---------------------------------------------------------------------
# 전역 변수(Global Variable)와 지역변수(Local Variable)
# - 함수 내에서 전역 변수 값 변경 하고자 하는 경우는 추가 코드 필요
# - 추가 코드 : global 전역 변수명
# -> 주의: 전역변수 값이 언제든지 함수로 변경될수 있는 상황 사용시에 주의 필요함
# 사용자 정의 함수 -------------------------------------------------------

def currentDate(todays):
    # todays => 년, 월, 일 을 원소로 담고 있는 데이터 타입, 리스트
    print(f'Today: {todays[0]}/{todays[1]:0>2}/{todays[2]:0>2}')

def currentData2(month, day):
    # month, day => 지역 변수

    global year
    # 함수 내에서 전역변수 값을 변경하고자 하는 경우는 global
    # year => 전액 변수
    print(f'Today: {year}/{month:0>2}/{day:0>2}')



# 전역 변수 -----------------------------------------------------------------------------------
year, month, day = 2024, -1 ,8
todayList=[year, month, day]

# 함수 사용 즉 함수 호출 -----------------------------------------------------------------------

# 변수 값 확인 출력
print(f'year: {year}, month : {month}, day : {day}')

currentDate(todayList)
print(f'year: {year}, month : {month}, day : {day}')
# 함수의 변수인 지역변수는 함수 밖에서 사용 불가------------------------------------------------------------
# print(f'week: {week}')
