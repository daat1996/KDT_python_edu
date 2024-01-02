# ----------------------------------------------
# 문자/문자열 데이터 살펴보기 => str 데이터 타입
# - 규칙/문법 ==> '데이터', "데이터", '''데이터''', """데이터"""
#
# ----------------------------------------------
msg = "Happy New Year 2024!"
# 한글자 하나하나를 원소/요소 라고 부르자
# 각 문자는 개별로 주소를 갖는다. msg[0] == H
# 출력
print(msg)

# ----------------------------------------------
# 문자/글자 안에서 일부분만 추출해서 다루기 => 인덱싱(indexing)
# - 왼쪽 ==> 오른쪽 : 0, 1, .....
# - 오른쪽 ==> 왼쪽 : -1, -2, ...
# - 원소/요소 추출 규칙/문법 => 변수명[인덱스]
# ----------------------------------------------
print(msg)

print(f'0번 원소 => {msg[0]}')
print(f'1번 원소 => {msg[1]}')
print(f'19번 원소 => {msg[19]}')
print(f'-1번 원소 => {msg[-1]}')
# print(f'20번 원소 => {msg[20]}')
# index out of range : 인덱스 범위 벗어 나면 오류 발생
# exit code 1 은 비정상 종료, code 0는 정상종료

# Happy만 화면에 출력하기
print(msg[0], msg[1], msg[2], msg[3], msg[4], sep='')

# 2024!만 화면에 출력하기
print(msg[15], msg[16], msg[17], msg[18], msg[19], sep='')
print(msg[-5], msg[-4], msg[-3], msg[-2], msg[-1], sep='')


# ----------------------------------------------
# 문자/글자 안에서 일부분만 추출해서 다루기 => 슬라이싱(slicing)
# - 원소/요소 추출 규칙/문법 => 변수명[시작인덱스:끝인덱스+1:간격]
# - 조건 : 연속된 인덱스 또는 규칙이 있는 인덱스
# ----------------------------------------------
# Happy만 화면에 출력하기 => 슬라이싱으로 출력하기
print(msg[0:5])     # 0~ 4
print(f'msg[0:4] => {msg[0:4]}')    # 마지막은 포함 안 된다.
print(f'msg[0:5] => {msg[0:5]}')

# 2024!만 화면에 출력하기 => 슬라이싱으로 출력하기
print(f'msg[15:20] => {msg[15:20]}')
print(f'msg[-5:0] => {msg[-5:0]}')  # 0전까지라 아무것도 안나옴
print(f'msg[-5:-1] => {msg[-5:-1]}')    # -1 전까지라 ! 안나옴
print(f'msg[-5:20] => {msg[-5:20]}')    # 그냥 20 넣어도 됨

# 첫번째 부터 시작하는 경우 시작인덱스 생략 가능
print(f'msg[0:5] => {msg[0:5]} , msg[:5] => {msg[:5]}')

# 마지막번째 까지 인 경우 마지막인덱스 생략 가능
print(f'msg[-5:20] => {msg[-5:20]} , msg[-5:] => {msg[-5:]}')

# 처음부터 끝까지 출력하기
print(f' msg[0:20] => {msg[0:20]}, msg[:] => {msg[:]}')

# ----------------------------------------------------------------
# 연속적이지 않지만 규칙이 있는 경우의 슬라이싱
# - 변수명[시작인덱스:끝인덱스+1:간격/규칙]
# ----------------------------------------------------------------
msg = "123456789"
#      012345678
# msg 안에서 2, 4, 6, 8 요소만 출력
print(msg[1], msg[3], msg[5], msg[7], sep='')
# 규칙 => 인덱스 연속 X, 인덱스 간격 2씩 증가
print(msg[1::2])
# msg 안에서 3의 배수만 출력
print(msg[2::3])

