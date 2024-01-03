# [실습] --------------------------------------------------------
# - 문자열 여러개와 실수 여러개를 두 줄로 입력력 받기 => input() 1개만 사용
# - 첫번째 입력 받은 값은 key
# - 두번째 입력 받은 값은 value
# - 딕셔너리로 저장해 주세요
# --------------------------------------------------------------
data = input("문자열과 실수 여러 개 입력 \n단, 문자열과 실수 갯수 동일(예:aa bb cc dd, 1.1 2.2 3.3 4) : ")

# 입력 형식이 맞을 경우만 딕셔너리에 저장
# - (1) 입력 "  ,  " 문자열 안에 ',' 존재해야함
# - (2) 문자열과 실수 갯수가 동일 해야함


if ',' in data:
    key, value = data.split(',')
    key = key.split()
    value = value.split()
    dataDict = {}
    if len(key) == len(value):
        for num in range(len(key)):
            dataDict[key[num]] = float(value[num])
        value = map(float, value)
        dataBict = dict(zip(key,value))     # value값은 리스트에서 들어갔기에 str 이 원소
        print(f'dataDict : {dataDict}')
        print(f'dataBict : {dataBict}')
    else:
        print("잘못된 입력")
else:
    print("잘못된 입력")


# --------------------------------------------------------------
# 내장함수 zip()
# --------------------------------------------------------------
x=[1,2,3,4,5]
y=[11,22,33,44,55]
z=[111,222,333,444,555]

result=zip(x,y,z)
print(f'result{type(result)}, {list(result)}')