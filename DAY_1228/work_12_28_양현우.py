"""
python 복습 과제
12 28
"""
# 1

mail = "kim1234@naver.com"
site = "http://www.naver.com"
name = "홍길동"
what = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRr"
mix = "ABC1DEF2GHI3JKL4MNO5PQR6STU7VWX8YZ"
num = "881120-1068234"

print(mail[:7])
print(site[11:])
print(name[1:])
print(what[::2], what[1::2])
print(mix[3::4])
print(num[:6],'\n',num[7:],sep='')


# 2
num1 = int(input("정수 입력 : "))
print(f'10진수 {num1}')
print(f'16진수 {hex(num1)}')  # 반환 타입은 문자열
print(f'8진수 {oct(num1)}')
print(f'2진수 {bin(num1)}')


# 3
word1 = input("첫 번째 단어를 입력하세요: ")
word2 = input("두 번째 단어를 입력하세요: ")
word3 = input("세 번째 단어를 입력하세요: ")
max_ord = max(word1, word2, word3)  # 문자열의 max, min 함수는 코드 값으로 비교하여 크기를 정한다
min_ord = min(word1, word2, word3)

print(f'코드 값이 가장 큰 단어 : {max_ord}')
print(f'코드 값이 가장 작은 단어 : {min_ord}')


# 4
msg = "8년째 장사하고 있는 식당을 보니 문득 10년간 정상에 서 있는 페이커가 새삼 대단하게 느껴진다."
word4 = input("단어 입력 : ")
print(f'\'{word4}\' 단어 메세지 존재 여부: {word4 in msg}')



# 5
word5 = input("단어 입력 : ")
print(bin(ord(word5[0])), bin(ord(word5[1]))[2:], bin(ord(word5[2]))[2:])
