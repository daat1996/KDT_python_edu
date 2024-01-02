'''
논리 연산자 => and, or, not
- 결과 : True, False
- 동작방식
    * and => A and B : A, B 모두 True일 때만 True
    * or => A or B : A, B 중 하나 이상 True가 되면 True
    * not => not A : 현재 A의 상태를 반대로 => not True --> false, not false --> True : 토글(toggle)
'''
no1, no2 = 10, 3


# and 연산자 --------------------------------------------------------
# no1은 no2보다 크고 그리고 100보다 큰 수
print(no1>no2, no1>100)
print(no1>no2 and no1>100)
print(no1>no2 and no1>100 and no1>0)

# or 연산자 ---------------------------------------------------------
# 1개 이상만 True가 되면 True 로 결정
print(no1>no2, no1>100)
print(no1>no2 or no1>100)
print(no1>no2 or no1>100 or no1>0)

# not 연산자 -------------------------------------------------------
# 현재 값을 반대로 즉, True => False, False => True
# False = 0, True =1 / 0이 아닌 모든 숫자

print(not False, not True)
print(not 0, not 1)
print(not 2, not -3)

"""
객체 비교 연산자 -> is, is not
- 결과 : True, False
- 동선방식 
- not 0 이 아니면 전부 False
"""
# 1
num1 = int(input("첫 번째 숫자를 입력하세요: "))
num2 = int(input("두 번째 숫자를 입력하세요: "))

print(f'{num1} + {num2} = {num1+num2}')
print(f'{num1} - {num2} = {num1-num2}')
print(f'{num1} * {num2} = {num1*num2}')
print(f'{num1} / {num2} = {num1/num2}')
print(f'{num1} // {num2} = {num1//num2}')
print(f'{num1} % {num2} = {num1%num2}')
print(f'{num1} ** {num2} = {num1**num2}')

#2
print(f'{num1} > {num2}     => {num1>num2}')
print(f'{num1} < {num2}     => {num1<num2}')
print(f'{num1} >= {num2}    => {num1>=num2}')
print(f'{num1} <= {num2}     => {num1<=num2}')
print(f'{num1} == {num2}     => {num1==num2}')
print(f'{num1} != {num2}     => {num1!=num2}')

#3
max3 = int(input("최댓값을 입력하세요: "))
min4 = int(input("최솟값을 입력하세요: "))

print(f'{num1}>{num2} and {num1}>{max3}     => {num1>num2 and num1>max3}')
print(f'{num1}>{num2} and {num1}>{min4}     => {num1>num2 and num1>min4}')
print(f'not {num1}           => {not num1}')
