def alphabet(x):
    if x.isupper():
        print('♠')
    else:
        print('♤')

def num(a):
    print('◎'*(int(a)))

while True:
    alNum = input('숫자나 알파벳 입력: ')
    if alNum == 'q' or alNum == 'Q':
        print('종료합니다.')
        break
    if alNum.isalpha():
        alphabet(alNum)
    elif alNum.isdecimal():
        num(alNum)
    else:
        print('숫자나 알파벳을 입력하세요.')

# 유니코드 번호에서 알파벳 구분, 해당되는것 한정해서 코드 정하기