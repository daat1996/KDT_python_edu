"""
조건문 if
"""

# 13.6 연슴문제

x = 5

if x!=10:
    print("oK")

# 13.7 심사문제

# cost = int(input())
# coupon = input()
#
# if coupon == 'Cash3000':
#     print(cost-3000)
# if coupon == 'Cash5000':
#     print(cost-5000)
#
#
# 14.4
x = 10
y = 20
if x == 10 and y ==20:
    print('참')
else:
    print('거짓')


# 14.6 연습문제
written_test = 80
coding_test = True

if written_test >= 80 and coding_test:
    print('합격')
else:
    print('불합격')

# 14.7 심사문제
# score = input().split()
score = ['98','79','68','82']
score = list(map(int, score))
# avg = (int(score[0])+int(score[1])+int(score[2])+int(score[3]))/4
avg = sum(score)
print(avg)
if max(score)<100 and min(score)>0:
    if avg >= 80:
        print('합격')
    else:
        print('불합격')
else:
    print("잘못된 점수")

# 15.3 연습문제:if, elif,else 모두 사용하기
x = int(input())
if 11 <= x <= 20:
    print("11~20")
elif 21 <= x <= 30:
    print('21~30')
else:
    print('아무것도 해당하지 않음')

# 15.4 심사문제
age = int(input())
balance = 9000      # 교통카드 잔액
if 7 <= age <= 12:
    balance -= 650
elif 13 <= age <= 18:
    balance -= 1050
else:
    balance -= 1250
print(balance)

