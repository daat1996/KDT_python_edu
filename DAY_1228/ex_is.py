'''
객체비교 연산자 살펴보기
    => 메모리 힙 영역에 존재하는 데이터 => 객체(object)
    => 클래스 데이터의 설명서/명세서에 해당하는 클래스(class)를 기반으로 객체 생성함!
    => 파이썬은 모든 데이터는 객체(object)!!
    => is 는 개체
    => == 은 값
'''

# print(10 is 10)

no1 = 10
no2 = 10
no3 = 20
print(no1 is no2)
print(no1 is no3)

no1 = no3
print(no1 is no3)
print(no1 is no2)