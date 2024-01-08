from random import randint, sample
from copy import deepcopy


def makeMine():     # 1. 지뢰를 만든다.
    matrix = []
    for sero in range(9):
        matseries = []
        for garo in range(9):
            num = randint(1, 8)
            if num%8 == 0:
                matseries.append('*')
            else:
                matseries.append('0')
        matrix.append(matseries)
    print(matrix)
    return matrix


def makeframe(mineList):       # 2. 액자틀 입력
    for k in range(9):
        mineList[k].insert(0, '■')
        mineList[k].append('■')
    mineList.insert(0, ['■'] * 11)
    mineList.append(['■'] * 11)
    print(mineList)
    return mineList


def makeAnswer(mat1):           # 3. 해답지 설정
    answer = deepcopy(mat1)         # 깊은 복사로 해답리스트(answer) 생성 및 리턴
    for x in range(1, 10):
        for y in range(1, 10):
            if mat1[x][y] != '*':
                answer[x][y] = str(mat1[x - 1][y - 1:y + 2].count('*') + mat1[x][y - 1].count('*') +
                                   mat1[x][y + 1].count('*') + mat1[x + 1][y - 1:y + 2].count('*'))
    print(answer)
    return answer


def bombZero(a,b):                  # 4. 0찾고 연쇄 폭발 리턴
    for alph in range(-1, 2):
        for bett in range(-1, 2):
            mat1[a-alph][b-bett] = answ[a-alph][b-bett]
            if alph!=0 or bett!=0:
                if answ[a-alph][b-bett] == '0':
                    answ[a - alph][b - bett] = '□'
                    bombZero(a-alph, b-bett)
    return mat1


def makeQuiz(mat0):                 # 4.5 문제집 리턴
    for xh in mat0:
        print(xh)




makeMine()
mat1 = makeMine()
print(mat1)
# 액자 추가 + 숫자 입력
mat1 = makeframe(mat1)
answ = makeAnswer(mat1)
print(mat1)

# 4. 문제지 출력
c = '■'
d = '□'
for a in range(1,10):
    for b in range(1,10):
        mat1[a][b] = c

for i in mat1:
    print(i)

while True:
    n1, n2 = map(int, input('좌표 입력 : ').split())
    if answ[n1][n2] != '*':
        mat1[n1][n2] = answ[n1][n2]
        if answ[n1][n2] == '0':
            bombZero(n1, n2)
    else:
        print(answ)
        print("Game over")
        break
    makeQuiz(mat1)