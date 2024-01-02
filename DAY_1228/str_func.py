'''
str 데이터 타입과 관련된 내장함수
'''
# 원소/요소의 갯수를 알려주는 내장함수 => length의 약자 len()
msg = "Christmas2023!"

print(f'len(msg) => {len(msg)}개')
# print(f'len(2024) => {len(2024)}개') # TypeError 숫자 데이터는 길이 즉 원소/요소 없음
# 정수(int)는 길이를 가지지 않는다!

# 문자의 코드값을 알려주는 내장 함수 => ord(문자1개) ======================================
# 문자 --->> 코드 : 인코딩(encoding)
print(f"ord('a') => {ord('a')}")

# Hello의 코드값 출력하기
code_H=ord('H')
code_e=ord('e')
code_l=ord('l')
code_o=ord('o')

print(f'Hello의 코드값 =>{code_H} {code_e} {code_l} {code_l} {code_o}')
print(f'Hello의 코드값 =>{bin(code_H)} {bin(code_e)} {bin(code_l)} {bin(code_l)} {bin(code_o)}')
print(f'Hello의 코드값 =>{bin(code_H)[2:]} {bin(code_e)[2:]} {bin(code_l)[2:]} {bin(code_l)[2:]} {bin(code_o)[2:]}')


# 코드값에 해당하는 문자를 반환해주는 내장 함수 => chr(코드값) ======================================
# 코드값 --->> 문자어 : 디코딩(decoding)
# 코드값 65에 해당하는 문자 반환
print(f'chr(65) => {chr(65)}')

