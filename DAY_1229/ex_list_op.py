# -----------------------------------------------------------------------------------
# list 자료형의 연산 살펴보기
# - 산술연산
# - 비교연산
# - 멤버연산자
# -----------------------------------------------------------------------------------
# 1~50 범위의 2의 배수로 구성된 리스트 생성
twoNum = list(range(2,51,2))

# 산술연산 => 덧셈(+), 곱셈(*)  -------------------------------------------------------
print(twoNum + ["a","b"])

# list + list => 새로운 list
datas = twoNum + ["a","b"]
print(datas)

# list + str => list + list(str)        캐스팅 시키면 가능
print(twoNum + list("ABC"))
# list + str => str(list) + str         list가 그냥 하나의 문자열이 됨
print(str(twoNum) + "ABC")
datas = str(twoNum) + "ABC"
print(type(datas))
print(datas[0])    # 0행이 [ 다



# list * int => int만큼 원소를 반복해서 하나의 list
print(twoNum*3)

# 멤버 연산 => in / not in ---------------------------------------------
#          => 결과 : True/False
print("C" in datas)
print("1" in datas)

