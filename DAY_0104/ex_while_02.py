# --------------------------------------------------------------------
# 반복문 -2while 반복문
# - 반복의 횟수가 정해진 경우 사용 가능함
# --------------------------------------------------------------------
# [요청] 사용자가 알고 싶어하는 단을 입력받아서 해당 단의 구구단을 출력
#       단, while 반복문 사용하기
# [예시] 알고 싶은 단 입력 : 3
#           --- 3단 ---
#
#
debug = False
if debug:
    num = int(input("알고싶은 단은?"))
    num1 = 0
    while num1 < 10:
        if num1 == 0:
            print(f'--- {num}단 ---')
        else:
            print(f'{num} * {num1} = {num*num1}')
        num1 += 1

# 2단 ~ 9단 while 반복문 사용 해서 출력 (세로 버전)
num = 0
dan = 2
while dan < 10:
    while num < 10:
        print(f'--- {dan}단 ---' if not num else f'{dan} * {num} = {dan*num:2}')
        num += 1
    num = 0
    dan += 1

# 2단 ~ 9단 while 반복문 사용 해서 출력 (가로 버전)
num = 0
dan = 2
while num < 10:
    while dan < 10:
        print(f'--- {dan}단 ---'if not num else f'{dan} * {num} = {dan*num}', end='\t' if dan <9 else '\n')
        dan += 1
    dan = 2
    num += 1


