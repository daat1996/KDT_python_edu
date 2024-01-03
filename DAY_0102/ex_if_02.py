# [실습1] -------------------------------------------------------------------
# 좋아하는 정수를 하나 저장 한 후 짝수면 '??는 짝수입니다.'
# 홀수면 '??는 홀수입니다.' 를 출력해주세요

num = 91
# num = int(input("정수를 하나 입력하시오 : "))


# 숫자 %2 == 0 : 짝수, 숫자 % 1 == 1 : 홀수

if num % 2 == 0:
    print(f"{num}은 짝수입니다.")
else:
    print(f'{num}은 홀수입니다.')


if num % 2 :        # 자동으로 형변환 시키기 때문에 결과가 0이 나오면(짝수) 거짓(False)
    print(f"{num}은 홀수입니다.")
else:
    print(f'{num}은 짝수입니다.')


# [실습2] -------------------------------------------------------------------
# 좋아하는 정수를 하나 저장 한 후 양수면 '??는 양수입니다.'
# 음수면 '??는 음입니다.'
# 0이면 '??는 0입니다' 출력하세요
# ---------------------------------------------------------------------------
# 다중 조건문 => 조건문이 2개 이상 되는 경우
if num>0:
    print(f'{num}는 양수입니다')
elif num<0:
    print(f'{num}는 음수입니다.')
else:
    print(f'{num}는 0입니다')


# [실습2] -------------------------------------------------------------------
# 좋아하는 정수를 하나 저장 한 후 양수면 '??는 양수입니다.'
# 음수면 '??는 음입니다.'
# 0이면 '??는 0입니다' 출력하세요
# ---------------------------------------------------------------------------
# 중첩 조건문 => 조건문 안에 조건문이 존재하는 경우

if num == 0:
    print(f'{num} 영')
else:
    if num>0:
        print(f'{num} 양수')
    else:
        print(f'{num} 음수')


if num:
    if num>0:
        print(f'{num} 양수')
    else:
        print(f'{num} 음수')
else:
    print(f'{num} 영')