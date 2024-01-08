# -------------------------------------------------------------------
# 함수와 클래스
# -------------------------------------------------------------------
# 변수에 어떤 데이터를 저장하고 있는지 확인하는 함수 => type(변수명)
data = 1

print(f'data Type => {type(data)}')

data = 'Good'
print(f'data Type => {type(data)}')

# 함수명의 타입
print(f'id().Type => {type(id)}')       # 내장함수 id 의 type

# 사용자 정의 함수 생성 ------------------------------------------------
# 함수 기능 : 2개 정수 더한 후 결과 출력 기능
# 함수 이름 : addTwo
# 매개 변수 : n1, n2
# 함수 결과 : 없음
# --------------------------------------------------------------------

def addTwo(n1 ,n2):
    print(n1+n2)

# 함수의 타입 출력 ===> type() 내장함수 사용 => class function
print(type(addTwo))

# -------------------------------------------------------
# 함수와 변수
# - 함수명은 코드의 시작주소를 저장하고 있음
# - 함수명을 변수에 대입 가능
# -------------------------------------------------------

test=addTwo

print(f' test -> {id(test)}, {type(test)}')
print(f' addTwo -> {id(addTwo)}, {type(addTwo)}')

test(10, 20)        # addTwo 함수처럼 동작한다.
addTwo(5, 1)

# -------------------------------------------------------
# [활용예]
# - 1~ 10 범위에서 임의의 정수 5개를 저장
# - 중복된 정수 저장 가능
# -------------------------------------------------------

numlist = []
import random
for a in range(5):
    numlist.append(random.randint(1,10))
print(numlist)

# 5개의 정수에서 최댓값, 최솟값, 내림차순 정렬된 값, 합계, 갯수 출력하기

print(f' 최댓값 : {max(numlist)}')
print(f' 최솟값 : {min(numlist)}')
print(f' 정 렬 : {sorted(numlist, reverse=True)}')
print(f' 합 계 : {sum(numlist)}')
print(f' 갯 수  : {len(numlist)}')

# 여러개의 함수이름을 변수에 저장 => 리스트 사용함
funs = [max,min,sorted, sum, len]   # 함수도 변수에 담을 수 있다.
for f in funs:
    if f == sorted:
        print(f(numlist, reverse=True))
    else:
        print(f(numlist))
# ------------------------------------------------------------------------------------
funcs = {'최댓값':max, '최솟값':min, '정 렬':sorted, '합 계':sum, '갯 수':len}
for a, b in funcs.items():
    if b == sorted:
        print(f'{a} : {b(numlist, reverse=True)}')
    else:
        print(f'{a} : {b(numlist)}')

