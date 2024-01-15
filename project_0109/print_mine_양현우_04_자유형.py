from random import randint, shuffle
from copy import deepcopy
from time import sleep

c = '██'
d = '  '
def makeMine():     # 1. 지뢰를 만든다.
    matrix = []
    for sero in range(9):
        matseries = []
        for garo in range(9):
            num = randint(1, 8)
            if num%8 == 0:
                matseries.append('**')
            else:
                matseries.append(' 0')
        matrix.append(matseries)
    # print(matrix)
    return matrix


def makeMine2(a=9,b=9,c=10):        # 지뢰만들기 ver.2
    matrix = []
    mIne = ['**'] * c + [' 0'] * (a * b - c)
    shuffle(mIne)
    for sero in range(a):
        matseries = []
        for garo in range(b):
            matseries.append(mIne.pop())
        matrix.append(matseries)
    return matrix






def makeframe(mineList,a=9,b=9):       # 2. 액자틀 입력
    for k in range(a):
        mineList[k].insert(0, chr(ord('①')+k))              # 내부 앞, 뒤 틀 입력
        mineList[k].append(chr(ord('①')+k))
    listF = []
    for j in range(b+2):                                 # 위 아래 틀 입력
        if not j or j==b+1:
            listF.append(chr(ord('ⓞ')))
        else:
            listF.append(chr(ord('①')+j-1))
    mineList.insert(0, listF)
    mineList.append(listF)
    # print(mineList)
    return mineList


def makeAnswer(mat0):           # 3. 해답지 설정
    answer = deepcopy(mat0)         # 깊은 복사로 해답리스트(answer) 생성 및 리턴
    for x in range(1, len(mat0)-1):
        for y in range(1, len(mat0[0])-1):
            if mat0[x][y] != '**':
                answer[x][y] = ' ' + str(mat0[x - 1][y - 1:y + 2].count('**') + mat0[x][y - 1].count('**') +
                                   mat0[x][y + 1].count('**') + mat0[x + 1][y - 1:y + 2].count('**'))
    # print(answer)
    return answer


def bombZero(a,b):                  # 4. 0찾고 연쇄 폭발 리턴
    global mat1
    global answ
    for alph in range(-1, 2):
        for bett in range(-1, 2):
            mat1[a-alph][b-bett] = answ[a-alph][b-bett]
            if alph!=0 or bett!=0:
                if answ[a-alph][b-bett] == ' 0':             # '0'을 쓴땅(사각형)으로 바꿈
                    answ[a - alph][b - bett] = '  '
                    bombZero(a-alph, b-bett)
    return mat1


def makeQuiz(mat0):                 # 4.5 문제집 풀이 리턴 - 수정 필요
    for i in mat0:
        print(i)


def makeQuiz1(mat0):                 # 4.5 문제집 풀이 리턴 - 수정1 (리스트 없이 간격 조절)
    for y1 in range(len(mat0)):
        for yh in range(len(mat0[0])):
            print(f'{mat0[y1][yh]}',end=' ' if yh < len(mat0[0])-1 else '\n')


def countMine(mat0):                # 5. 해답지의 지뢰 카운트(전체)
    mineNum = 0
    for kh in mat0:
        mineNum += kh.count('**')
    return mineNum


def countGround(mat0):              # 6. 문제지의 지뢰 카운트(현재)
    groundNum = 0
    for nk in mat0:
        groundNum += nk.count('██')
    return groundNum


def printQuiz(mat0):
    for a in range(1,len(mat0)-1):
        for b in range(1,len(mat0[0])-1):
            global c
            mat0[a][b] = c
    return mat0

def manual():                       # 7. 시작 메뉴얼
    print("*" * 30)
    print("*" * 30)
    print("[지뢰 찾기]")
    print("*" * 30)
    print("0. 게임방법                 **")
    print("1. 쉬움                     **")
    print("2. 중간                     **")
    print("3. 딱딱한                   **")
    print("r. 리셋                     **")
    print("q. 종료                     **")
    print("*" * 30)


def correct(listX):
    global mat1
    if len(listX) == 2:
        n1, n2 = listX
        if (n1.isdigit()) and (n2.isdigit()):
            n1, n2 = list(map(int,listX))
            if 0<n1<len(mat1)-1 and 0<n2<len(mat1[0])-1:
                return True
            elif n1==0 and n2==0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def manualList(press):
    global key1
    if press == '0':
        sleep(0.5)
        print('세로축, 가로축 순서로 원하는 좌표를 입력하여')
        sleep(0.5)
        print('지뢰가 아닌 땅을 찾으세요!')
        sleep(1)

    elif press == '1':
        print()
        print("게임시작!")
        sleep(1)
        key1 = 2
    elif press == '2' or press == '3':
        print("정식판을 구매해주세요")
        print()
    elif press == 'q' or press == 'Q':
        print("게임을 종료합니다.")
        sleep(1)
        key1 = 0
    elif press == 'r' or press == 'R':
        print('다시 시작합니다')
        sleep(1)
        print()
    else:
        print("해당하는 메뉴는 존재하지 않습니다.")
        sleep(0.5)






def saveMine(mat0):
    wor = ''
    for nf in range(len(mat0)):
        for nnf in range(len(mat0[0])):
            wor += mat0[nf][nnf] + (',' if nnf < len(mat0[0])-1 else '\n')
    with open('save_mine.txt', mode='w', encoding='utf-8') as f:
        f.write(wor)


def loadMine(filename):
    with open('save_mine.txt', mode='r', encoding='utf-8') as f:
        readData = f.readlines
    for nf in readData:
        pass




key1 = 1
key2 = 1
filename = 'save_mine.txt'
while True:
    while key1==1:
        manual()
        press = input("원하는 메뉴를 입력하세요 : ")

        if press == '0':
            sleep(0.5)
            print('세로축, 가로축 순서로 원하는 좌표를 입력하여')
            sleep(0.5)
            print('지뢰가 아닌 땅을 찾으세요!')
            sleep(1)

        elif press == '1':
            print()
            print("게임시작!")
            sleep(1)
            key1 = 2
            key2 = 1
        elif press == '2':
            print()
            print("게임시작!")
            sleep(1)
            key1 = 2
            key2 = 2
        elif press == '3':
            print()
            print("게임시작!")
            sleep(1)
            key1 = 2
            key2 = 3
        elif press == 'q' or press == 'Q':
            print("게임을 종료합니다.")
            sleep(1)
            key1 = 0
        elif press == 'r' or press == 'R':
            print('다시 시작합니다')
            sleep(1)
            print()
        else:
            print("해당하는 메뉴는 존재하지 않습니다.")
            sleep(0.5)

    if key2 == 1:               # 1. 지뢰 배치
        mat1 = makeMine2()
        mat1 = makeframe(mat1)          # 2. 액자 추가 + 숫자 입력
    elif key2 == 2:
        mat1 = makeMine2(12,12,23)
        mat1 = makeframe(mat1,12,12)          # 2. 액자 추가 + 숫자 입력
    elif key2 == 3:
        mat1 = makeMine2(16,16,40)
        mat1 = makeframe(mat1,16,16)  # 2. 액자 추가 + 숫자 입력
    elif key2 == 4:
        mat1 = makeMine()
        mat1 = makeframe(mat1)  # 2. 액자 추가 + 숫자 입력
        pass
    else:
        mat1 = makeMine()
        mat1 = makeframe(mat1)  # 2. 액자 추가 + 숫자 입력



    answ = makeAnswer(mat1)         # 3. 해답지 생성(깊은 복사로 배치가 같은 리스트 answ 생성)
    printQuiz(mat1)                 # 4. 문제지 출력


    while key1==2:
        print()
        makeQuiz1(mat1)
        saveMine(answ)
        # print(f'남은 지뢰: {countMine(answ)}')
        # print(f'남은 땅: {countGround(mat1)}')

        if countMine(answ) == countGround(mat1) or countMine(answ) == countMine(mat1):
            print('Game Clear!')
            key1 = 0

        else:
            print(f'지뢰 갯수 : {countMine(answ)}')
            rad1 = input('q(종료) / s(저장 후 메뉴로 돌아가기) / r(메뉴로 가기)\n좌표 입력(2번째 줄 8번째 칸 = 2 8) : ')
            if rad1 == 'q' or rad1 == 'Q':
                print('게임을 종료합니다.')
                key1 = 0

            elif rad1 == 's' or rad1 == 'S':
                saveMine(answ)
                print('저장중입니다.')
                # sleep(1)
                # print('저장중입니다..')
                # sleep(1)
                print('메뉴로 돌아갑니다.')
                key1 = 1
            elif rad1 == 'r' or rad1 == 'R':
                print('메뉴로 돌아갑니다.')
                key1 = 1

            else:
                rad2 = rad1.split()
                if correct(rad2):
                    n1, n2 = map(int, rad2)      # 좌표 확인 필요
                else:
                    print('잘못된 좌표입니다.')
                    continue

                if n1 ==0 and n2 == 0:          # 디버깅용 해답(삭제필요)
                    for ta in range(1,len(mat1)-1):      #
                        for tb in range(1,len(mat1[0])-1):  #
                            bombZero(ta,tb)     #
                else:                           #
                    if answ[n1][n2] != '**':
                        mat1[n1][n2] = answ[n1][n2]
                        if answ[n1][n2] == ' 0':
                            bombZero(n1, n2)
                    else:
                        makeQuiz1(answ)
                        print("Game over")
                        key1 = 0
        saveMine(answ)
    if not key1:
        break
