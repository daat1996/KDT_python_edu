"""
Python 복습 과제
"""
# 1
hometown = "대구광역시"
blood_type = "B Rh+"
season = 'fall'
height = '167'
phone_number = "010-7301-9148"
country = "Korea"

# 2
mbti='INFP'
blood='A'
gender='M'
height=171.7
weight=77

# 2-1)여러데이터 출력
print('[ 신상 정보 ]')
print('MBTI :', mbti, '\t혈액형 :',blood,'\t성별 :',gender)
print('몸무게 :', weight, '\t\t키 :',height)


# 2-2)서식지정자 출력 방식
print('[ 신상 정보 ]')
print('MBTI : %s\t\t 혈액형 : %s\t\t 성별 : %s'%(mbti, blood, gender))
print('몸무게 : %.1f\t 키 : %f'%(height, weight))

# 2-3)F-스트링 출력 방식
print('[ 신상 정보 ]')
print(f'MBTI : {mbti}\t\t 혈액형 : {blood}\t\t 성별 : {gender}')
print(f'몸무게 : {weight}\t\t 키 : {height}')


# 3-1
a = 50
b = 0.91
c = "Winter"
d = False

print(f'데이터 {a}\t => {type(a)} 타입')
print(f'데이터 {b}\t => {type(b)} 타입')
print(f'데이터 {c}\t => {type(c)} 타입')
print(f'데이터 {d}\t => {type(d)} 타입')

# 3-2
weather = input("좋아하는 계절은?: ")
print(f'당신은 {weather}을 좋아하는 군요!')

english = input("봄은 영어로? ")
print(f'봄은 {english}입니다.')


# 4
'''
순서대로 힙영역
스택영역
'''

# 5-1
'''
int, float, string, bool
'''

# 5-2
'''
2진수, 8진수, 16진수
'''


# 6
garo = int(input("직육면체 가로길이(cm): "))
sero = int(input("직육면체 세로길이(cm): "))
h = int(input("직육면체 높이길이(cm): "))

s = garo * sero
v = s * h
print(f'직사각형 넓이: {s}')
print(f'직육면체 부피: {v}')