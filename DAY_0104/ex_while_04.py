# ---------------------------------------------------------------------------------
# continue => 계속해서
# - 키원드 아래 코드 실행 안됨
# - 반복 상단으로 이동
# ---------------------------------------------------------------------------------
# 1~ 30으로 구성된 리스트 생성하세요.
numList = list(range(1,31))


# 리스트에 요소 중에서 짝수인 경우만 화면에 출력해 주세요~
# for data in numList:
#     if not data%2:
#         print(data)
#
# for data in numList:
#     if data%2:
#         continue
#     print(data)
#
# while----------------------------------------------------------------------------
idx = 0
while idx<29:
    idx += 1
    if numList[idx]%2:
        continue
    print(numList[idx])
# 계속 진행된다.


idx = -1
while idx<29:
    idx += 1
    if numList[idx]%2:
        continue
    print(numList[idx])


