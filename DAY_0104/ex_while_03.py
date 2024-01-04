# -------------------------------------------------------------------------
# 반복문 - 2 while 반복문
# - 반복의 횟수 정해 지지 않은 경우
# -------------------------------------------------------------------------
# [요청] 사용자가 'x' 입력 전까지 입력 받은 데이터 저장해 주세요.
# => 몇 번 입력할지 알 수없음 => 무한 입력 받기
# => 종료 조건 ===> 사용자가 'x' 입력
Debug = False

if Debug:
    while True:
        data = input("저장하고 싶은 데이터 입력 (종료 x) : ")
        # 종료 검사  => break : 키워드가 있는 부분에서 바로 반복 종료, 아래 코드 실행 안됨
        # if data == 'x' or data == 'X':
        if data in ('x','X'): break              # 튜플이라 포함되어도 종료 안됨
                   # 가장 가까운 키워드(while)를 빠져나옴    조건문이 하나라면 바로 뒤에 사용 가능

        print('OK')

    print("프로그램 종료")

# -----------------------------------------------------------------------------------------
# [요청] 사용자로부터 x/X 입력 전까지 계속 정수를 입력
#       입력 받은 정수 만큼 알파벳을 출력
# [예시] 출력 원하는 알파벳 수 입력 : 5
#        abcde
#       출력 원하는 알파벳 수 입력 : 1
#        a
#       출력 원하는 알파벳 수 입력 : 10
#        abcdefghij
#       출력 원하는 알파벳 수 입력 : 27
#        abcdefghijklmnopqrstuvwxyz 종료
#       출력 원하는 알파벳 수 입력 : x
#        종료
# -----------------------------------------------------------------------------------------
if Debug:
    while True:
        num = input("출력 원하는 알파벳 수 입력 : ")
        # 무한 입력 반복 종료 조건
        if num in ('x', "X"):
            print("종료합니다.")
            break
        if num.isdecimal():
            num = int(num)
            aCode = ord('a')
            for a in range(num):
                a += aCode
                print(chr(a),end='')
                if a == ord('z'):
                    print("종료")
                    break
            print()
        else:
            print("잘못된 입력입니다.")



isEnd = False       # flag 변수를 사용하여 전체 프로그램을 정지시킨다(break는 하나의 반복문만 정지)

for n in range(100):
    if isEnd:
        print("프로그램 종료합니다. ")
        break
    print(f"out -> {n}")

    for n2 in range(100):
        if n2>10:
            isEnd = True
            break
        print(f'in -> {n2} ====> {n}번째')


# while 문으로 위의 프로그램 만들기
# n = 0
# n2 = 0
# while True:
#     print(f'out -> {n}')
#
#     while n2<=10:
#         print(f'in -> {n2} ====> {n}번째')
#         n2 += 1
#     n += 1
#     break
#

# [요청] 내부에 반복문에서 데이터가 10초과되면 프로그램 종료 ------
outNum = 1
isEnd = False

while outNum <= 100:
    # 종료조건
    if isEnd:
        print("프로그램 종료")
        break
    print(f'outNum => {outNum}')

    # 내부 while
    inNum = 1
    while inNum <=100:
        if inNum >10:
            print("내부 while 종료")
            isEnd = True
            break
        print(f'inNum => {inNum} ===> [{outNum}번째]')
        inNum += 1

    outNum += 1

