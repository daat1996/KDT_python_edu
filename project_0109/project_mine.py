
def manual():                       # 7. 시작 메뉴얼
    print("*" * 100)
    print("[지뢰 찾기]")
    print("*" * 100)
    print("1. 쉬움")
    print("2. 중간")
    print("3. 딱딱한")
    print("r. 리셋")
    print("q. 종료")


while True:
    manual()
    press = input("원하는 메뉴를 입력하세요 : ")
    if press == '1':
        pass
    elif press == '2' or press == '3':
        print("정식판을 구매해주세요")
    elif press == 'q' or press == 'Q':
        print("게임을 종료합니다.")
        break
    elif press == 'r' or press == 'R':

        pass
    else:
        print("해당하는 메뉴는 존재하지 않습니다.")
        pass


