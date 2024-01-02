# --------------------------------------------------------
# 다양한 리스트 생성
# --------------------------------------------------------
# 실수 데이터로 구성된 리스트 생성
floatNums = [4., 3.1, 6.3, 5.01]

# str 데이터로 구성된 리스트 생성
strNums = ['44', '56', '98']

# bool 데이터로 구성된 리스트 생성
boolNums = [False, False, True, True, False]

# 다양한 데이터 타입으로 구성된 리스트 생성
nums=['100', 98, False, 7.12, 'Apple', True]

# 빈 리스트 생성
nums = []

# 리스트 안에 리스트 데이터로 구성된 리스트 생성
nums2 = [10, 20, 30, ["A", "B"], 200, 100]
#        0    1   2       3       4    5


# 리스트의 요소 출력
print(f'nums2[0] => {nums2[0]}, {type(nums2[0])}')
print(f'nums2[1] => {nums2[1]}, {type(nums2[1])}')
print(f'nums2[2] => {nums2[2]}, {type(nums2[2])}')
print(f'nums2[3] => {nums2[3]}, {type(nums2[3])}')
print(f'nums2[4] => {nums2[4]}, {type(nums2[4])}')
print(f'nums2[5] => {nums2[5]}, {type(nums2[5])}')

print(f'nums2[3]에서 [1]요소 => {nums2[3][1]}, {type(nums2[3][1])}')

data2 = [[[1,2,3]], 'A']
print(data2[0])
print(data2[0][0])
print(data2[0][0][0])
print(data2[1])


