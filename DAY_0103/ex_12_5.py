# [문제] --------------------------------------------------------
# - 문자열 여러개와 실수 숫자 여러개를 두 줄로 입력력 받기
# - 첫번째 입력 받은 값은 key
# - 두번째 입력 받은 값은 value
# - 딕셔너리로 저장해 주세요
# --------------------------------------------------------------

key = input("문자열 4~5개 입력").split()
value = input("문자열과 같은 수의 실수 입력").split()
# 입력 데이터 존재 여부 체크


if len(key) and len(value):
    print("입력 ok")
    if len(key) == len(value):
        if len(key) == 4:
            dict1 = dict({key[0]:value[0], key[1]:value[1], key[2]:value[2], key[3]:value[3]})
            print(dict1)
        elif len(key) == 5:
            dict1 = dict({key[0]: value[0], key[1]: value[1], key[2]: value[2], key[3]: value[3], key[4]: value[4]})
            print(dict1)
        else:
            print("문자열의 갯수가 4~5개가 아닙니다.")
    else:
        print("문자와 실수의 갯수가 다릅니다.")

else:
    print("입력된 데이터가 없습니다.")