"""
for 변수 in reversed(range(시작, 끝, 증가폭))

"""

# 입력받은 수가 최대 가로 길이가 되도록하는 마름모 만들기

# num = int(input("홀수를 입력하시오: "))
# for a in range(1,num+1):
#     if a <= (num+1)/2:
#         print(f'{(2*a-1) * "*":^101}')
#     else:
#         print(f'{(2*(num-a)+1)*"*":^101}')

# range 거꾸로 출력
for i in reversed(range(10)):
    print('Hello World', i)

# 시퀀스 객체로 반복하기

a = [10, 20, 30, 40, 50]
for i in a:
    print(i)

for letter in 'Python':
    print(letter, end=' ')
print()


# 16.5 연습문제
x = [49, -17, 25, 102, 8, 62, 21]

for i in x:
    print(i*10, end=' ')

# 16.6 심사문제:구구단
num = int(input())

if 1 <= num <= 9:
    for a in range(1, 10):
        print(f'{num} * {a} = {num*a}')
else:
    print("입력한 숫자의 범위가 1~9가 아닙니다.")

# 19.1 중첩 루프 사용
for i in range(5):
    for j in range(5):
        print('j:', j, sep='', end=' ')
    print('i:', i, '\\n', sep='')

# 19.2.1 사각형 모양 바꾸기
for i in range(3):
    for j in range(7):
        print('*', end='')
    print()

# 19.3.1 대각선으로 별 출력하기
for i in range(5):
    for j in range(5):
        if i == j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

# 19.5 연습문제 : 역삼각형모양으로 별 출력하기
for i in range(5):
    for j in range(5):
        if j >= i:
            print('*',end='')
        else:
            print(' ',end='')
    print()

# 19.6 심사문제 : 산모양으로 별 출력하기
num = int(input("홀수를 입력하시오: "))
for a in range(1,num+1):
    print(' '*(num-a), '*'*(2*a-1), sep='')

# 중첩사용해서 (일부러 더 어렵게) 만들기
num = int(input("홀수 : "))
for a in range(num):
    for b in range(1, 2*num):
        if b > num+a or num-a > b:
            print(' ',end='')
        else:
            print('*',end='')
    print()

# 22.1.3

a= [10, 20, 30]
a.append([500,600])
print(a)
print(len(a))

# 22.1.4 리스트 확장하기
# extend(리스트)
a = [10, 20, 30]
a.extend([500,600])

# insert(인덱스, 요소)
a.insert(3,400)
print(a)
# insert 마지막 인덱스보다 큰 값을 지정하면 리스트 끝에 요소하나 추가 가능
# insert 없이 중간에 요소 여러개 추가
a = [10, 20, 30]
a[1:1] = [500, 600]
print(a)
# 인덱스가 겹치면 겹친 부분이 덮어씌워지고 나머지는 그대로
a = [10, 20, 30]
a[1:2] = [500, 600]
print(a)

a = [10, 20, 30]
a[1:3] = [500, 600]
print(a)

# pop()은 리스트의 마지막 요소를 삭제한 후 그 값을 리턴
a = [10, 20, 30]
print(a.pop())
print(a)

a = [10, 20, 30]
print(a.pop(1))
print(a)

# del도 가능하나 del은 리턴은 없음
a = [10, 20, 30]
del a[1]
print(a)

# .index : 리스트에서 특정값의 인덱스 구하기
# .count : 리스트에서 특정값의 rotn 구하기

# 리스트의 순서를 뒤집기(통쨰로) : .reverse()
a = [10, 20, 30, 80, 70, 60]
a.reverse()
print(a)

# 리스트 요소 정렬 : .sort()
a = [10, 20, 30, 80, 70, 60]
a.sort()
print(a)

# 리스트의 범위를 벗어난 인덱스로 리스트를 추가하기
a = [10, 20, 30, 80, 70, 60]
a[len(a):] = [500]
print(a)

# 리스트는 빈 리스트인지 아닌지 bool값으로 구분 가능

# a와 b 는 같은 주소를 갖는 같은 리스트
a = [0, 0, 0, 0, 0]
b = a

b[2] = 99
print(a, b)

a = [0, 0, 0, 0, 0]
b = a.copy()    # 리스트 a의 요소가 b로 복사되긴하나 리스트 주소는 다름

b[2] = 99
print(a, b,sep='\n')

# 22.3 enumerate(리스트) : (인덱스, 리스트요소) 의 리스트 생성
a = [23, 12, 39, 48, 29]
for index, value in enumerate(a):
    print(index, value)

a = [23, 12, 39, 48, 29]
for index, value in enumerate(a):
    print(index+1, value)

a = [23, 12, 39, 48, 29]
for index, value in enumerate(a, 1):
    print(index, value)

# 22.4 요소의 합계
a = [10, 10, 10, 10, 10]
x = 0
for i in a:
    x += i
print(x)
# sum(리스트) 이 더 편하다

# 22.5.리스트 컴프리핸션(comprehension)
a = []
for i in range(10):
    a.append(i)
# 이것을 한 문장으로
a = [i for i in range(10)]
#또는
b = list(i for i in range(10))

# 22.5.1 리스트 표현식 if 사용
a = [i for i in range(10) if i % 2 == 0]        # 0~9 숫자 중 짝수로만 리스트 생성

# 22.5.2 for반복문과 if 조건문을 여러번 사용
# 2~9단까지 구구단을 리스트 생성
a = [i * j for j in range(2, 10) for i in range(1,10)]
# 처리 순서는 뒤의 for가 먼저 시작

# 22.6 리스트에 map 사용
a = [1.2, 2.5, 3.7]
for i in range(len(a)):
    a[i] = int(a[i])
# map 사용시
a = list(map(int, a))

# 22.9 연습문제
a =['alpha', 'bravo','charlie','delta','echo','foxtrot','golf','hotel','india']
b = [i for i in a if len(i) == 5]
print(b)

# 22.10 심사문제:
i1, i2 = map(int, input().split())
list1 = []
for a in range(i1,i2+1):
    list1.append(2**a)
list1[1:len(list1)-2] = list1[2:len(list1)-3]

# list1.pop(1)
# list1.pop(-2)
print(list1)

# comprehension 사용
i1, i2 = map(int, input().split())
list1 = [2**a for a in range(i1, i2+1)]
list1.pop(1)
list1.pop(-2)
print(list1)