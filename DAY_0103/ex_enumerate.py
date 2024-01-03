# -------------------------------------------------------------------------------------------
# for 요소 in 시퀀스/반복 가능한객체:
# ==> for 인덱스 in range(len(변수)):
# ==> 내장함수 enumerate()
# - (번호, 요소) 튜플 묶음으로 반환(리턴)한다!!
# -------------------------------------------------------------------------------------------
datas = ['Apple', 'Banana', 'Orange']

# 리스트 안에 요소/원소 데이터 추출
for data in datas:
    print(data)

# 리스트 안에 요소/원소 (인덱스, 데이터) 추출
for data in enumerate(datas, start=100):        # 뒤에 start값 디폴트는 0이라 0부터 시작
    print(data)

x = ['std01', 'std02', 'std03']
y = [100 ,200, 300]

myDict = {}
for data in enumerate(x):
    myDict[data[1]] = y[data[0]]
print(f'{myDict}')


myDict2 = {}
for idx, key in enumerate(x):
    # idx = 0, key='std01'
    myDict2[key] = y[idx]
print(f'{myDict2}')


