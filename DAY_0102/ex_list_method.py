# ----------------------------------------------------------------------
# 메서드 => 특정 데이터 타입의 전용 함수를 메서드(method)라고 부름
# 메서드의 (self)는 무시
# 메서드의 None은 반환값 없음
# - 범용의 함수와 식별하기 위해서 지정한 호칭
# - 사용법 : 데이터.메서드명 또는 변수명.메서드명
# ----------------------------------------------------------------------
# List 전용 메서드 살펴보기 ===============================================
# [1] 리스트에 데이터 추가해주는 메서드 => append() 맨끝에 원소를 추가
nums = []
print(f'nums :  {len(nums)}개, {nums}')

nums.append("Faker")
nums.append(True)
nums.append(1)
print(f'nums :  {len(nums)}개, {nums}')

# [1] 리스트에 데이터 추가해주는 메서드 => insert(위치인덱스, 데이터) 지정 위치에 원소를 추가
nums.insert(0, 2024)
print(f'nums :  {len(nums)}개, {nums}')

nums.insert(-1, ["ABC", "DEF"])
print(f'nums :  {len(nums)}개, {nums}')  # 맨 뒤로 넣어도 true가 뒤로 밀린다.

# "DEF" 제거
del nums[-2][1]
print(f'nums :  {len(nums)}개, {nums}')

# 리스트 안에 모든 원소 삭제해서 빈 리스트 만들어주세요~
del nums[:]
print(f'nums :  {len(nums)}개, {nums}')

# 리스트 안에 원소/요소 정렬해주는 메서드 => sort() 오름차순 정렬
# - 오름차순 : 작은 데이터 >>> 큰 데이터
nums.append(98)
nums.append(-4)
nums.append(65)
nums.append(17)
nums.append(5.2)
print(f'nums :  {len(nums)}개, {nums}')


nums.sort()
print(f'nums :  {len(nums)}개, {nums}')
# 저장을 시키면 None 을 리턴하기에 None 값이 나옴
num = nums.sort()
print(num)


# 내림차순 : 큰 데이터 >> 작은 데이터 순서로
nums.sort(reverse=True) # 역순 매개변수값을 True 설정
print(f'nums : {len(nums)}개, {nums}')

# [3] 리스트 안에 원소/요소의 현재 위치를 반대로 뒤집어 주는 메서드 => sort() 오름차순 정렬
# 원소/요소 데이터 값 비교 안함!! 순서만 변경함
nums.reverse()
print(f'nums : {len(nums)}개, {nums}')

# [4] 리스트 안에 원소/요소를 삭제해주는 메서드 => remove()
# - 리스트에서 지정된 값의 원소 삭제(데이터 알때)
# - 없는 값/데이터 삭제 요청 시 Error 발생!!
nums.remove(17) # 가장 먼저 발견되는 1개만 삭제함
print(f'nums : {len(nums)}개, {nums}')
# nums.remove(17) 한번 더 하면 list안에 없다고 error 뜸
# print(f'nums : {len(nums)}개, {nums}')

# [5] 리스트 안에 모든 원소/요소를 삭제해주는 메서드 => clear()
nums.clear()
print(f'nums : {len(nums)}개, {nums}')


# [6] 리스트 에 모든 원소/요소를 꺼내는 메서드 => pop()
nums.append(10)
nums.append(-3)
nums.append(6)

# 제일 마지막 원소/요소 데이터 꺼내기 => pop()
nums.pop()
print(f'nums : {len(nums)}개, {nums}')

# 특정 위치에 원소/요소 데이터 꺼내기 => pop(인덱스)
nums.pop(0)     # 꺼내는 것이라 꺼낸값이 리턴됨
print(f'nums : {len(nums)}개, {nums}')

# [7] 리스트에서 특정 원소/요소 데이터가 몇 개 존재하는지 카운팅해주는 메서드 => 카운트(데이터)
print(nums.count('A'))
print(nums.count(-3))

a = [1, 2, 3, 2, 1, 1, ['A','c'],['A']]
print(a.count(["A"]))   # 리스트의 원소는 하나의 덩어리로 봐야한다 : 집합의 원소와 같음


# [8] 리스트를 확장시키는 메서드 => extend(여러개의 데이터 저장한 데이터 타입)
nums.extend([11,22,33])   # +와는 다르게 원본이 변경된다.
print(f'nums : {len(nums)}개, {nums}')

nums.extend([])
print(f'nums : {len(nums)}개, {nums}')   # 추가되는 데이터가 없음

nums.extend("새해 복 많이 받으세요")
print(f'nums : {len(nums)}개, {nums}')   # str 원소 하나하나 나눠져서 들어간다.

nums.extend(["새해 복 많이 받으세요"])
print(f'nums : {len(nums)}개, {nums}')   # 리스트 원소 하나가 통째로 들어간다.

# nums.extend(2024)     # 시퀀스 또는 반복가능한 데이터만 가능
# print(f'nums : {len(nums)}개, {nums}')   # int 는 원소가 하나도 없기에 error 발생

# [9] 리스트를 복사해주는 메서드 => 얕은 복사 copy()
nums.append([100, 200])
nums2 = nums.copy()     # 얕은 복사
print(f'nums : {len(nums)}개, {nums}')
print(f'nums2 : {len(nums2)}개, {nums2}')

# nums의 [-2]의 데이터를 2024로 변경
nums[-2] = 2024
print(f'nums : {len(nums)}개, {nums}')       # 변함
print(f'nums2 : {len(nums2)}개, {nums2}')    # 변하지 않음

# nums의 -1번 요소의 0번 요소의 데이터를 77로 변경
nums[-1][0] = 77
print(f'nums : {len(nums)}개, {nums}')
print(f'nums2 : {len(nums2)}개, {nums2}')    # 둘 다 변함


