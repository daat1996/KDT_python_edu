# -------------------------------------------------------------------
# filter(함수명, 반복 가능 객체)
# - 조건에 맞는 데이터만 반환
# -------------------------------------------------------------------
# 예) 5초과 10 미만 데이터만 추출
import random                   # random.py 파일에 모든 변수, 함수, 클레스 가져오기
from random import randint, random      # random.py 파일에서 randint 함수만 가져오기   (1개만 들고옴)
from functools import reduce


a = [8,3,2,10,15,7,1,9,0,11]
def check(data):
    return data > 5 and data < 10

a = list(filter(check, a))
print(a)

randint(1,10)
random()

def f(x,y):
    return x+y

print(reduce(f, a))

print(reduce(lambda  x, y : x+y, a))