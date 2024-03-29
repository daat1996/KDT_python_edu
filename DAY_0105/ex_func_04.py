# -----------------------------------------------------------------------------------
# 다양한 함수의 형태 - (3) return 키워드
# - 함수 호출한 곳으로 돌아가게 하는 기능
#   결과값이 함께 있다면 결과값을 가지고 돌아감.
# 함수 기능 : 2개의 정수를 덧셈 후 출력해주는 기능
# 함수 이름 : addTwo
# 매개 변수 : x, y
#  반 환 값 : 없음
# -----------------------------------------------------------------------------------
def factorial(x):
    if not x:
        return 1            # 즉시 함수 종료 후 호출한 곳으로 반환,
    ret=1
    if x:
        for a in range(1,x+1): ret *= a        # for 문이 1줄이면 옆에 적어도 된다.
    return ret

print(factorial(5))
